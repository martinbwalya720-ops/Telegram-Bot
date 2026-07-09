from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)
import random

BOT_TOKEN = "8977525770:AAHssx3RhFjpROpDwxCNStItPn8mhUWb0bE" 


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📊 Scan Markets", callback_data="scan")],
        [InlineKeyboardButton("🥇 Gold", callback_data="gold")],
        [InlineKeyboardButton("💱 Forex", callback_data="forex")],
        [InlineKeyboardButton("₿ Crypto", callback_data="crypto")],
        [InlineKeyboardButton("📈 Live Signals", callback_data="signals")],
        [InlineKeyboardButton("📰 Market News", callback_data="news")],
        [InlineKeyboardButton("📅 Economic Calendar", callback_data="calendar")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "━━━━━━━━━━━━━━━━━━━━━━━\n"
        "🤖 ATLAS AI TRADER PRO\n"
        "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Welcome!\n\n"
        "Choose an option below.",
        reply_markup=reply_markup,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "scan":

        assets = [
            ("🥇 XAU/USD (Gold)", "🟢 BUY", 92),
            ("💶 EUR/USD", "🔴 SELL", 88),
            ("💷 GBP/USD", "🟢 BUY", 84),
            ("₿ BTC/USD", "🟡 WAIT", 79),
            ("Ξ ETH/USD", "🟢 BUY", 82),
        ]

        random.shuffle(assets)
        assets.sort(key=lambda x: x[2], reverse=True)

        text = "━━━━━━━━━━━━━━━━━━━━━━━\n"
        text += "🔥 TOP MARKET OPPORTUNITIES 🔥\n"
        text += "━━━━━━━━━━━━━━━━━━━━━━━\n\n"

        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]

        for i, asset in enumerate(assets):
            text += (
                f"{medals[i]} {asset[0]}\n"
                f"{asset[1]}\n"
                f"💎 Confidence: {asset[2]}%\n\n"
            )

        text += "━━━━━━━━━━━━━━━━━━━━━━━\n"
        text += "🤖 AI Recommendation\n"
        text += "Gold currently has the strongest setup."

    elif query.data == "gold":

        text = (
            "━━━━━━━━━━━━━━━━━━━━━━━\n"
            "🥇 GOLD ANALYSIS\n"
            "━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "📈 Trend: Bullish\n"
            "💎 Confidence: 92%\n"
            "⚠️ Risk: Medium\n\n"
            "💰 Entry Price\n"
            "Coming Soon...\n\n"
            "🛑 Stop Loss\n"
            "Coming Soon...\n\n"
            "🎯 Take Profit\n"
            "Coming Soon...\n\n"
            "⏳ Entry Window\n"
            "Coming Soon..."
        )

    elif query.data == "forex":

        text = (
            "💱 FOREX\n\n"
            "Live Forex scanner is under development."
        )

    elif query.data == "crypto":

        text = (
            "₿ CRYPTO\n\n"
            "Live Crypto scanner is under development."
        )

    elif query.data == "signals":

        text = (
            "📈 LIVE SIGNALS\n\n"
            "No active high-confidence signals."
        )

    elif query.data == "news":

        text = (
            "📰 MARKET NEWS\n\n"
            "News integration coming soon."
        )

    elif query.data == "calendar":

        text = (
            "📅 ECONOMIC CALENDAR\n\n"
            "Economic calendar coming soon."
        )

    elif query.data == "settings":

        text = (
            "⚙️ SETTINGS\n\n"
            "Settings panel coming soon."
        )

    else:

        text = "Unknown option."

    await query.edit_message_text(text)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("🚀 Atlas AI Trader PRO is online...")

app.run_polling() 
