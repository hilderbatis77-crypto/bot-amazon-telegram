import asyncio
from telegram import Bot

BOT_TOKEN = "8525612178:AAHon74pKlOfLYfu3meUmOKhlmES3-trIIY"
CHANNEL_ID = "@achadosdokick"

async def main():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHANNEL_ID,
        text="🚀 TESTE OK!\n\nMensagem enviada corretamente com async."
    )

if _name_=="-main_":
asyncio.run(main())
