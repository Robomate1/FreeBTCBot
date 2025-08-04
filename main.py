import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

TOKEN = os.getenv("TOKEN") or "8330315706:AAHoBJVsJ5P0fx1Vq0qKSONFo_oRO60hNCI"
REFERRAL_URL = "https://freebitco.in/?r=55455882"
CHANNEL_URL = "https://t.me/+8WHsVgaJkJc0NDFl"

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎯 Start Earning BTC", url=REFERRAL_URL)],
        [InlineKeyboardButton("📢 Join Our Channel", url=CHANNEL_URL)],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 Welcome! Click below to roll and earn free BTC 💰", reply_markup=reply_markup
    )

# Main function
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
