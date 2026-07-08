from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = "8977525770:AAHFe1fkV-oNt1fpcBgKBMym3HVVQp6rOm0" 


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📊 Scan Markets", callback_data="scan")],
        [InlineKeyboardButton("🥇 Gold", callback_data="gold")],
        [InlineKeyboardButton("💱 Forex", callback_data="forex")],
        [InlineKeyboardButton("₿ Crypto", callback_data="crypto")],
        [InlineKeyboardButton("📰 Market News", callback_data="news")],
        [InlineKeyboardButton("📅 Economic Calendar", callback_data="calendar")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="settings")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🤖 Welcome to Atlas AI Trader\n\nChoose an option:",
        reply_markup=reply_markup,
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    if query.data == "scan":
        text = "📊 Market Scanner\n\n🚧 Live market scanner coming next."

    elif query.data == "gold":
        text = "🥇 Gold Analysis\n\n🚧 Live Gold analysis coming next."

    elif query.data == "forex":
        text = "💱 Forex Analysis\n\n🚧 Live Forex analysis coming next."

    elif query.data == "crypto":
        text = "₿ Crypto Analysis\n\n🚧 Live Crypto analysis coming next."

    elif query.data == "news":
        text = "📰 Market News\n\n🚧 News module coming next."

    elif query.data == "calendar":
        text = "📅 Economic Calendar\n\n🚧 Calendar module coming next."

    elif query.data == "settings":
        text = "⚙️ Settings\n\n🚧 Settings module coming next."

    else:
        text = "Unknown option."

    await query.edit_message_text(text)


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("Atlas AI Trader is online...")

app.run_polling()
