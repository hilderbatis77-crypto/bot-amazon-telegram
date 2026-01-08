import asyncio
import os
from telegram import Bot

BOT_TOKEN = "8525612178:AAHon74pKlOfLYfu3meUmOKhlmES3-trIIY"
CHANNEL_ID = "@achadosdokick"

# Arquivo de trava para evitar mensagens duplicadas
LOCK_FILE = "/tmp/telegram_bot_lock.txt"

async def main():
    # Se já enviou mensagem, não envia de novo
    if not os.path.exists(LOCK_FILE):
        bot = Bot(token=BOT_TOKEN)
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text="✅ BOT ONLINE E ESTÁVEL\n\nMensagem enviada com sucesso pelo Railway 🚀"
        )

        # Cria o lock
        with open(LOCK_FILE, "w") as f:
            f.write("sent")

    # Mantém o processo vivo (Railway não crasha)
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
