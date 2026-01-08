import asyncio
from telegram import Bot

BOT_TOKEN = "8525612178:AAHon74pKlOfLYfu3meUmOKhlmES3-trIIY"
CHANNEL_ID = "@achadosdokick"

async def main():
    bot = Bot(token=BOT_TOKEN)

    # Envia apenas UMA mensagem de teste
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text="✅ BOT ONLINE E ESTÁVEL\n\nMensagem enviada com sucesso pelo Railway 🚀"
    )

    # Mantém o bot rodando (evita crash no Railway)
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
