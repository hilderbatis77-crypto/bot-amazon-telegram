import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

async def encaminhar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    texto = update.message.text

    if "amazon." in texto or "amzn.to" in texto:
        mensagem = (
            "🔥 ACHADO NA AMAZON 🔥\n\n"
            "🛒 Produto recomendado\n"
            f"👉 {texto}\n\n"
            "⚡ Oferta por tempo limitado!"
        )

        await context.bot.send_message(
            chat_id=CHANNEL_ID,
            text=mensagem
        )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, encaminhar))
    print("🤖 Bot iniciado com sucesso")
    app.run_polling()

if __name__ == "__main__":
    main()
