import asyncio
from telegram.ext import ApplicationBuilder

TOKEN = "SEU_TOKEN_AQUI"

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    await app.initialize()
    await app.start()
    await app.bot.send_message(
        chat_id="@achadosdokick",
        text="🚀 Bot iniciado com sucesso!"
    )
    await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
