import os
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CANAL_ID = os.getenv("CANAL_ID")

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CANAL_ID, text="🚀 Bot online no Render!")
