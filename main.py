from telegram import Bot
import time

BOT_TOKEN = "8525612178:AAHon74pKlOfLYfu3meUmOKhlmES3-trIIY"
CHANNEL_ID = "@achadosdokick"

bot = Bot(token=BOT_TOKEN)

async def main():
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text="🚀 TESTE OK!\n\nMensagem enviada pelo Railway com sucesso."
    )

if __name__ == "__main__":
    asyncio.run(main())
