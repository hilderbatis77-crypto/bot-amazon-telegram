import requests
import hashlib
import hmac
import datetime
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

# ================== CONFIGURAÇÕES ==================
BOT_TOKEN = "8525612178:AAFaZe_Qj75LDSfZbHSwe9U8v0LSASLjP7M"
CHANNEL_ID = "@achadosdokick"

AMAZON_ACCESS_KEY = "AKPAJ1OA781767773612"
AMAZON_SECRET_KEY = "AKPAJSH5YS1767773541"
AMAZON_ASSOCIATE_TAG = "hildemarbatis-20"
REGION = "us-east-1"
SERVICE = "ProductAdvertisingAPI"
HOST = "webservices.amazon.com.br"
ENDPOINT = f"https://{HOST}/paapi5/getitems"

# ================== ASSINATURA AMAZON ==================
def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def get_signature_key(key, date, region, service):
    k_date = sign(("AWS4" + key).encode("utf-8"), date)
    k_region = sign(k_date, region)
    k_service = sign(k_region, service)
    k_signing = sign(k_service, "aws4_request")
    return k_signing

# ================== BUSCAR PRODUTO ==================
def buscar_produto(asin):
    payload = {
        "ItemIds": [asin],
        "Resources": [
            "Images.Primary.Large",
            "ItemInfo.Title",
            "Offers.Listings.Price",
            "Offers.Listings.SavingBasis",
        ],
        "PartnerTag": AMAZON_ASSOCIATE_TAG,
        "PartnerType": "Associates",
        "Marketplace": "www.amazon.com.br",
    }

    amz_date = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    date_stamp = datetime.datetime.utcnow().strftime("%Y%m%d")

    payload_hash = hashlib.sha256(str(payload).encode("utf-8")).hexdigest()

    canonical_headers = (
        "content-encoding:amz-1.0\n"
        "content-type:application/json; charset=utf-8\n"
        f"host:{HOST}\n"
        f"x-amz-date:{amz_date}\n"
    )

    signed_headers = "content-encoding;content-type;host;x-amz-date"

    canonical_request = (
        "POST\n"
        "/paapi5/getitems\n\n"
        f"{canonical_headers}\n"
        f"{signed_headers}\n"
        f"{payload_hash}"
    )

    algorithm = "AWS4-HMAC-SHA256"
    credential_scope = f"{date_stamp}/{REGION}/{SERVICE}/aws4_request"

    string_to_sign = (
        f"{algorithm}\n"
        f"{amz_date}\n"
        f"{credential_scope}\n"
        f"{hashlib.sha256(canonical_request.encode('utf-8')).hexdigest()}"
    )

    signing_key = get_signature_key(
        AMAZON_SECRET_KEY, date_stamp, REGION, SERVICE
    )

    signature = hmac.new(
        signing_key,
        string_to_sign.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()

    authorization_header = (
        f"{algorithm} "
        f"Credential={AMAZON_ACCESS_KEY}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, "
        f"Signature={signature}"
    )

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Content-Encoding": "amz-1.0",
        "X-Amz-Date": amz_date,
        "Authorization": authorization_header,
    }

    r = requests.post(ENDPOINT, json=payload, headers=headers, timeout=20)
    return r.json()

# ================== BOT ==================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot online! Envie um link da Amazon.")

async def receber_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.strip()

    if "amazon" not in texto and "amzn.to" not in texto:
        await update.message.reply_text("❌ Envie apenas links da Amazon.")
        return

    asin = texto.split("/")[-1].split("?")[0]

    try:
        dados = buscar_produto(asin)

        item = dados["ItemsResult"]["Items"][0]
        titulo = item["ItemInfo"]["Title"]["DisplayValue"]
        preco_atual = item["Offers"]["Listings"][0]["Price"]["Amount"]
        preco_antigo = item["Offers"]["Listings"][0]["SavingBasis"]["Amount"]
        imagem = item["Images"]["Primary"]["Large"]["URL"]

        desconto = int(100 - (preco_atual / preco_antigo * 100))

        mensagem = (
            "🔥💥 OFERTA IMPERDÍVEL 💥🔥\n\n"
            f"🛒 *{titulo}*\n\n"
            f"❌ De: R$ {preco_antigo:.2f}\n"
            f"✅ Por: *R$ {preco_atual:.2f}*\n"
            f"🎯 Desconto: *{desconto}% OFF*\n\n"
            f"👉 Compre aqui:\n{texto}\n\n"
            "⏰ Corre que pode acabar a qualquer momento!"
        )

        await context.bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=imagem,
            caption=mensagem,
            parse_mode="Markdown",
        )

        await update.message.reply_text("✅ Oferta postada com sucesso!")

    except Exception:
        await update.message.reply_text(
            "❌ Não foi possível obter os dados do produto."
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, receber_link)
    )

    app.run_polling()

if __name__ == "__main__":
    main()
