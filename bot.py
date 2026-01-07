import os
import time
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")
CANAL_ID = os.getenv("CANAL_ID")

bot = Bot(token=TOKEN)

# envia mensagem de teste
bot.send_message(
    chat_id=CANAL_ID,
    text="✅ Bot conectado com sucesso! Render funcionando 🚀"
)

# mantém o bot vivo no Render
while True:
    time.sleep(60)
