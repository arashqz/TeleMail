# TeleMailBot

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg) ![Telegram](https://img.shields.io/badge/Telegram-Bot-green.svg)

---

## 📌 درباره (فارسی) / About (English)

**TeleMailBot** یک ربات تلگرامی حرفه‌ای برای ارسال ایمیل از طریق SMTP است.  
این ربات از **Environment Variables** برای نگهداری امن اطلاعات حساس استفاده می‌کند و تمامی پیام‌های ارسال شده را لاگ می‌کند.

**TeleMailBot** is a professional Telegram bot for sending emails via SMTP.  
It uses **Environment Variables** to securely store credentials and logs all sent messages.

---

## 🚀 ویژگی‌ها / Features

- ارسال ایمیل امن و ساده / Secure and simple email sending  
- لاگینگ پیام‌ها / Message logging  
- استفاده از Environment Variables برای رمزها / Environment variable configuration for credentials  
- مناسب برای گیت‌هاب و پروژه‌های متن‌باز / Perfect for GitHub and open-source projects  

---

## 👤 سازنده / Author

**arashqz**  
تلگرام / Telegram: [@arashqz](https://t.me/arashqz)

---

## ⚡ نصب و اجرا / Installation & Run

1. کلون کردن ریپوزیتوری / Clone the repo:
```bash
git clone https://github.com/arashqz/TeleMail.git
cd telemail-bot
```

2. نصب پیش‌نیازها / Install requirements:
```bash
pip install -r requirements.txt
```

3. ساخت فایل `.env` بر اساس `.env.example` / Create `.env` based on `.env.example`:
```env
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
SMTP_HOST=mail.example.com
SMTP_PORT=587
SMTP_USERNAME=your_email@example.com
SMTP_PASSWORD=your_password
```

4. اجرای ربات / Run the bot:
```bash
python bot.py
```

---

## 📝 نحوه استفاده / How to Use

پیام خود را در **۴ خط** به ربات ارسال کنید / Send your message in **4 lines**:

```
sender@example.com
receiver@example.com
موضوع ایمیل / Subject
متن ایمیل / Text
```

مثال / Example:

```
sender@example.com
someone@example.com
سلام
امیدوارم حالتان خوب باشد
```

---

## ⚠️ نکات امنیتی / Security Notes

- هرگز اطلاعات حساس را مستقیم در کد ننویسید / Never put sensitive info directly in code  
- فایل `.env` را به گیت‌هاب کامیت نکنید / Do not commit `.env` to GitHub  
- فایل‌های لاگ (`emails_log.txt`) در `.gitignore` قرار دارند / Log files are included in `.gitignore`  

---

## 📂 ساختار پروژه / Project Structure

```
telemail-bot/
│
├─ bot.py           # کد اصلی ربات / Main bot code
├─ .env.example     # نمونه فایل محیطی / Example environment file
├─ requirements.txt # پیش‌نیازهای پایتون / Python requirements
├─ .gitignore       # فایل نادیده‌گیری گیت / Git ignore file
└─ emails_log.txt   # فایل لاگ پیام‌ها / Message log file
```

---

**TeleMailBot** – ربات تلگرامی امن و حرفه‌ای برای ارسال ایمیل  
**Author:** `arashqz` | Telegram: [@arashqz](https://t.me/arashqz)
