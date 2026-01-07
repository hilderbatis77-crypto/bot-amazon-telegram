import os
import time
from telegram import Bot

TOKEN = os.getenv("TELEGRAM_TOKEN")

# ID do seu chat privado
CHAT_ID = 6974326371

bot = Bot(token=TOKEN)

# envia mensagem de teste
bot.send_message(
    chat_id=CHAT_ID,
    text="✅ Teste OK! Bot conectado e funcionando no Render 🚀"
)

# mantém o bot rodando
while True:
    time.sleep(60)
