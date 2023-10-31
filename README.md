# בוט להעלאת קבצים ל-Google Drive דרך טלגרם
**בוט טלגרם להעלאת קבצים מטלגרם או מקישורים ישירים ל-Google Drive.**
- אפשר למצוא אותו בטלגרם בשם [Google Drive Uploader](https://t.me/uploadgdrivebot)

## תכונות
- [X] תמיכה בקבצים מטלגרם.
- [X] תמיכה בקישורים ישירים.
- [X] ספריית העלאה מותאמת אישית.
- [X] תמיכה ב-TeamDrive.
- [X] שיבוט/העתקת קבצים ב-Google Drive.
- [X] מחיקת קבצים ב-Google Drive.
- [X] ריקון סל המחזור ב-Google Drive.
- [X] תמיכה ב-youtube-dl.

## משימות עתידיות
- [ ] טיפול בשגיאות נוספות.
- [ ] תמיכה ב-LOGGER.
- [ ] תמיכה בחשבון שירות.
- [ ] פקודת עדכון.

## הצטרפות

### הפעלה על [Heroku](https://heroku.com)
[![הפעלה](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### התקנה
- התקן מודולים נדרשים.
```sh
apt install -y git python3 ffmpeg
```
- שכפל את המאגר של Git הזה.
```sh 
git clone https://github.com/viperadnan-git/google-drive-telegram-bot
```
- שנה את התיקיה
```sh 
cd google-drive-telegram-bot
```
- התקן דרישות עם pip3
```sh 
pip3 install -r requirements.txt
```

### הגדרה
**ישנם שני אופנים להגדיר את הבוט.**
1. הוסף ערכים למשתני הסביבה (Environment Variables). והוסף משתנה `ENV` לכל משתנה שברצונך להפעיל.
2. הוסף ערכים ב-[config.py](./bot/config.py). וודא שאין משתני `ENV` קיימים.

### ערכי ההגדרה
- `BOT_TOKEN` - ניתן לקבל אותו על ידי יצירת קשר עם [BotFather](https://t.me/botfather)
- `APP_ID` - ניתן לקבל אותו על ידי יצירת אפליקציה ב-[my.telegram.org](https://my.telegram.org/apps)
- `API_HASH` - ניתן לקבל אותו על ידי יצירת אפליקציה ב-[my.telegram.org](https://my.telegram.org/apps)
- `SUDO_USERS` - רשימת מזהים משתמשי Telegram של מנהלי המערכת, מופרדים ברווח.
- `SUPPORT_CHAT_LINK` - קישור לצ'אט התמיכה ב-Telegram.
- `DATABASE_URL` - כתובת מסד נתונים של Postgres.
- `DOWNLOAD_DIRECTORY` - נתיב מותאם אישית להורדות. יש לסיים בסלש קדמי `/`. (ברירת המחדל: `./downloads/`)

### התקנה
```sh 
python3 -m bot
```

## קרדיטים
- [Dan](https://github.com/delivrance) על יצירת [PyroGram](https://pyrogram.org)
- [Spechide](https://github.com/Spechide) על [gDriveDB.py](./bot/helpers/sql_helper/gDriveDB.py)
- [Shivam Jha](https://github.com/lzzy12) על תכונת השיבוט (Clone Feature) מתוך [python-aria-mirror-bot](https://github.com/lzzy12/python-aria-mirror-bot)

## זכויות יוצרים ורישיון
- כל הזכויות שמורות (©) 2020 על ידי [Adnan Ahmad](https://github.com/viperadnan-git)
- מרשמים תחת תנאי [רישיון ה-GNU הציבורי הכללי, גרסה 3, 29 ביוני 2007](./LICENSE)
