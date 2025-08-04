import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to FreeBitco.in Reminder Bot! I'll remind you to roll every hour. 🔔")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I will remind you to roll at FreeBitco.in every hour. You can leave me running!")

async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏰ Time to roll at https://freebitco.in/?r=YOUR_REFERRAL_CODE")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("remind", remind))

    app.run_polling()

if __name__ == '__main__':
    main()
