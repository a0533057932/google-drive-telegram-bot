import re
import json
from httplib2 import Http
from bot import LOGGER, G_DRIVE_CLIENT_ID, G_DRIVE_CLIENT_SECRET
from bot.config import Messages
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from oauth2client.client import OAuth2WebServerFlow, FlowExchangeError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from bot.helpers.sql_helper import gDriveDB
from bot.config import BotCommands
from bot.helpers.utils import CustomFilters

OAUTH_SCOPE = "https://www.googleapis.com/auth/drive"
REDIRECT_URI = "http://localhost/"

flow = None

@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Authorize))
async def _auth(client, message):
    """
    Handles the authorization process. If the user is already authorized, refreshes the credentials.
    If not, generates an authorization URL and sends it to the user.
    """
    user_id = message.from_user.id
    creds = gDriveDB.search(user_id)
    if creds is not None:
        creds.refresh(Http())
        gDriveDB._set(user_id, creds)
        await message.reply_text(Messages.ALREADY_AUTH, quote=True)
    else:
        global flow
        try:
            flow = OAuth2WebServerFlow(
                G_DRIVE_CLIENT_ID,
                G_DRIVE_CLIENT_SECRET,
                OAUTH_SCOPE,
                redirect_uri=REDIRECT_URI,
                response_type='code',
                access_type='offline',
                prompt='consent'
            )
            auth_url = flow.step1_get_authorize_url()
            LOGGER.info(f'AuthURL:{user_id}')
            await message.reply_text(
                text=Messages.AUTH_TEXT.format(auth_url),
                quote=True,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("Authorization URL", url=auth_url)]]
                )
            )
        except Exception as e:
            await message.reply_text(f"**ERROR:** ```{e}```", quote=True)

@Client.on_message(filters.private & filters.incoming & filters.command(BotCommands.Revoke) & CustomFilters.auth_users)
async def _revoke(client, message):
    """
    Handles the revocation of authorization. Clears the user's credentials from the database.
    """
    user_id = message.from_user.id
    try:
        gDriveDB._clear(user_id)
        LOGGER.info(f'Revoked:{user_id}')
        await message.reply_text(Messages.REVOKED, quote=True)
    except Exception as e:
        await message.reply_text(f"**ERROR:** ```{e}```", quote=True)

@Client.on_message(filters.private & filters.incoming & filters.text & ~CustomFilters.auth_users)
async def _token(client, message):
    """
    Handles the token exchange process. Retrieves the code from the message and exchanges it for credentials.
    """
    code = message.text.split("?code=")[1].split("&")[0]
    token = code.split()[-1]
    WORD = len(token)
    if WORD == 73 and token[1] == "/":
        creds = None
        global flow
        if flow:
            try:
                user_id = message.from_user.id
                sent_message = await message.reply_text("🕵️**Checking received code...**", quote=True)
                creds = flow.step2_exchange(code)
                gDriveDB._set(user_id, creds)
                LOGGER.info(f'AuthSuccess: {user_id}')
                await sent_message.edit(Messages.AUTH_SUCCESSFULLY)
                flow = None
            except FlowExchangeError:
                await sent_message.edit(Messages.INVALID_AUTH_CODE)
            except Exception as e:
                await sent_message.edit(f"**ERROR:** ```{e}```")
        else:
            await sent_message.edit(Messages.FLOW_IS_NONE, quote=True)
