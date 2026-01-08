from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "SEU_TOKEN_DO_BOT"
CHANNEL_ID = "@seucanal"

async def encaminhar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text

    if "amazon." in texto or "amzn.to" in texto:
        msg = f"""🔥 ACHADO NA AMAZON 🔥

🛒 Produto recomendado
👉 {texto}

⚡ Oferta por tempo limitado!
"""
        await context.bot.send_message(chat_id=CHANNEL_ID, text=msg)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, encaminhar))
app.run_polling()
