import os
import time
import random
import schedule
from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
TAG = os.getenv("AMAZON_TAG")

bot = Bot(token=BOT_TOKEN)

# Lista inicial de mensagens (simula achados)
PRODUTOS = [
    {
        "nome": "Fone Bluetooth JBL",
        "preco": "R$ 129,90",
        "link": f"https://www.amazon.com.br/?tag={TAG}"
    },
    {
        "nome": "Echo Dot Alexa",
        "preco": "R$ 279,00",
        "link": f"https://www.amazon.com.br/?tag={TAG}"
    },
    {
        "nome": "Smartwatch Xiaomi",
        "preco": "R$ 199,90",
        "link": f"https://www.amazon.com.br/?tag={TAG}"
    }
]

def postar_oferta():
    produto = random.choice(PRODUTOS)

    mensagem = (
        "🔥 ACHADO AMAZON 🔥\n\n"
        f"📦 *{produto['nome']}*\n"
        f"💰 *{produto['preco']}*\n\n"
        f"🛒 Confira aqui:\n{produto['link']}\n\n"
        "⚡ Promoção por tempo limitado!"
    )

    bot.send_message(
        chat_id=CHANNEL_ID,
        text=mensagem,
        parse_mode="Markdown"
    )

    print("Post enviado com sucesso!")

# Agenda: a cada 30 minutos
schedule.every(30).minutes.do(postar_oferta)

print("🤖 Bot iniciado e rodando...")

while True:
    schedule.run_pending()
    time.sleep(5)
