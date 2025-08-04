from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes, JobQueue, Application
)
from db import init_db, add_user

TOKEN = "8330315706:AAHoBJVsJ5P0fx1Vq0qKSONFo_oRO60hNCI"
REFERRAL_URL = "https://freebitco.in/?r=55455882"
CHANNEL_URL = "https://t.me/+8WHsVgaJkJc0NDFl"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)

    # Schedule hourly reminder
    context.job_queue.run_repeating(
        send_hourly_reminder,
        interval=3600,
        first=0,
        chat_id=user_id,
        name=str(user_id)
    )

    keyboard = [
        [InlineKeyboardButton("🎯 Start Earning BTC", url=REFERRAL_URL)],
        [InlineKeyboardButton("📢 Join Our Channel", url=CHANNEL_URL)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 You're now registered for hourly reminders!\nClick below to roll and earn free BTC 💰",
        reply_markup=reply_markup
    )

async def send_hourly_reminder(context: ContextTypes.DEFAULT_TYPE):
    user_id = context.job.chat_id
    await context.bot.send_message(
        chat_id=user_id,
        text="⏰ Reminder: Don't forget to roll and earn free BTC!\n" + REFERRAL_URL
    )

def main():
    init_db()

    # Set up the Application with job queue enabled
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ Bot is running. Open Telegram and send /start")
    app.run_polling()

if __name__ == "__main__":
    main()
