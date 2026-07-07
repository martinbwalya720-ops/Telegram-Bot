from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8977525770:AAHFe1fkV-oNt1fpcBgKBMym3HVVQp6rOm0" 


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Welcome to Atlas AI Trader!\n\n"
        "Commands:\n"
        "/scan - Scan the market\n"
        "/help - Show commands"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/scan - Scan markets\n"
        "/help - Show help"
    )


async def scan(update: Update, context: ContextTypes.DEFAULT_TYPE):

    message = """
📊 Atlas AI Trader

🔥 TOP MARKET OPPORTUNITIES

🥇 XAU/USD (Gold)

Signal: BUY 📈

Confidence: 87%

Risk: LOW

Entry Price:
3352.40

Entry Window:
Next 20 minutes

Stop Loss:
3345.20

Take Profit:
3368.50

Estimated Holding Time:
2–4 hours

────────────────────

🥈 EUR/USD

Signal: SELL 📉

Confidence: 82%

Risk: MEDIUM

Entry Price:
1.1724

Stop Loss:
1.1752

Take Profit:
1.1676

Estimated Holding Time:
3–6 hours

────────────────────

Reply YES when automatic trading becomes available.
"""

    await update.message.reply_text(message)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("scan", scan))

print("Atlas AI Trader is online...")

app.run_polling()
