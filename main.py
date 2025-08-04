from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Get token from environment variable (set this in Render dashboard)
TOKEN = os.getenv("TOKEN")

# Define the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! 🤖 This is your FreeBitco.in reminder bot.")

# Define a /remind command
async def remind(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏰ Don’t forget to ROLL every hour on FreeBitco.in!")

# You can add more commands like /balance or /channel here
# Just define a new async function and add another CommandHandler

# Main function to run the bot
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("remind", remind))

    # Start polling
    app.run_polling()

# Run it
if __name__ == "__main__":
    main()
