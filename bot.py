import os
from telegram import Bot

TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = "-1003319815831"  # seu ID do canal

bot = Bot(token=TOKEN)

bot.send_message(
    chat_id=CHAT_ID,
    text="🔥 Bot conectado com sucesso no Railway!"
)
