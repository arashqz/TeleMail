from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
import smtplib
import os

print("Bot started")

# /start command
def start(update, context):
    help_text = """
به ربات ارسال ایمیل خوش آمدید!

لطفا پیام خود را دقیقا در 4 خط ارسال کنید:

sender@example.com
receiver@example.com
موضوع ایمیل
متن ایمیل
"""
    update.message.reply_text(help_text)


def send_email(update, context):
    try:
        sender_email, receiver_email, subject, text = update.message.text.split('\n', 3)
    except ValueError:
        update.message.reply_text("❌ فرمت پیام اشتباه است.")
        return

    smtp_host = os.getenv("SMTP_HOST")
    smtp_port = int(os.getenv("SMTP_PORT", 587))
    smtp_username = os.getenv("SMTP_USERNAME")
    smtp_password = os.getenv("SMTP_PASSWORD")

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(smtp_username, smtp_password)

            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(text, "plain", "utf-8"))

            smtp.send_message(message)

        update.message.reply_text("✅ ایمیل با موفقیت ارسال شد!")

        with open("emails_log.txt", "a", encoding="utf-8") as file:
            file.write(f"Sender ID: {update.effective_user.id}\n")
            file.write(f"Username: {update.effective_user.username}\n")
            file.write(f"Receiver: {receiver_email}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"Time: {datetime.now()}\n")
            file.write("------\n")

    except Exception as e:
        update.message.reply_text("❌ خطا در ارسال ایمیل")
        print(e)


def main():
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")

    updater = Updater(telegram_token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, send_email))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
