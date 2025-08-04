import asyncio
from telegram import Bot
from db import get_all_users

TOKEN = "8330315706:AAHoBJVsJ5P0fx1Vq0qKSONFo_oRO60hNCI"
REFERRAL_URL = "https://freebitco.in/?r=55455882"

async def send_reminders():
    bot = Bot(token=TOKEN)
    while True:
        users = get_all_users()
        for user_id in users:
            try:
                await bot.send_message(
                    chat_id=user_id,
                    text=f"⏰ It's time to roll and earn more BTC!\n👉 {REFERRAL_URL}"
                )
            except Exception as e:
                print(f"Failed to send to {user_id}: {e}")
        await asyncio.sleep(3660)  # Wait 61 minutes

if __name__ == "__main__":
    asyncio.run(send_reminders())
