import asyncio
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

BOT_TOKEN = "8525612178:AAHon74pKlOfLYfu3meUmOKhlmES3-trIIY"
CHANNEL_ID = "@achadosdokick"

async def receber_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if "amazon." in texto or "amzn.to" in texto:
        mensagem = (
            "🔥 OFERTA IMPERDÍVEL 🔥\n\n"
            "👉 Aproveite essa oferta na Amazon:\n"
            f"{texto}\n\n"
            "⚡ Corre que pode acabar a qualquer momento!\n\n"
            "#Amazon #Achados #Promoção"
        )

        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=mensagem,
            disable_web_page_preview=False
        )

        await update.message.reply_text("✅ Link enviado para o canal com sucesso!")
    else:
        await update.message.reply_text("❌ Envie apenas links da Amazon.")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, receber_link)
    )

    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
