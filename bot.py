from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import yfinance as yf

BOT_TOKEN = "8977525770:AAHFe1fkV-oNt1fpcBgKBMym3HVVQp6rOm0" 


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to Atlas AI Trader!\n\n"
        "Commands:\n"
        "/scan - Demo market scan\n"
        "/gold - Live Gold price"
    )


async def gold(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        gold = yf.Ticker("GC=F")
        price = gold.history(period="1d")

        current_price = price["Close"].iloc[-1]

        await update.message.reply_text(
            f"🥇 Live Gold Price\n\n"
            f"${current_price:.2f}\n\n"
            f"Powered by Atlas AI Trader"
        )

    except Exception as e:
        await update.message.reply_text(f"Error getting gold price:\n{e}")


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚧 Live market scanner is under construction.\n"
        "Coming next!"
    )


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gold", gold))
app.add_handler(CommandHandler("scan", scan))

print("Atlas AI Trader is online...")

app.run_polling()
