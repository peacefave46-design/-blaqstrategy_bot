import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# --- Configuration ---
# Get token from environment variable (for Railway)
BOT_TOKEN = os.environ.get('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

# Your channel link
CHANNEL_LINK = 'https://t.me/blaqmarqetnotify'

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# --- Command Handlers ---

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message with a button to the channel."""
    user = update.effective_user
    welcome_message = (
        f"👋 Hello {user.first_name}!\n\n"
        "Welcome to BLAQSTRATEGY. 🚀\n\n"
        "I provide educational insights on digital advertising systems, "
        "campaign organization, and workflow optimization for marketers.\n\n"
        "🔽 **Click the button below to join our channel and start learning!**"
    )

    # Create an inline keyboard with one button
    keyboard = [
        [InlineKeyboardButton("📢 Join BLAQSTRATEGY Channel", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a help message."""
    help_text = (
        "Here's how to use me:\n"
        "/start - Get the welcome message and join link\n"
        "/help - Show this help message\n"
        "/channel - Get the channel link directly\n\n"
        f"Or click here: {CHANNEL_LINK}"
    )
    await update.message.reply_text(help_text)

async def channel_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the channel link directly."""
    keyboard = [
        [InlineKeyboardButton("📢 Go to Channel", url=CHANNEL_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        f"Click the button below to join BLAQSTRATEGY:",
        reply_markup=reply_markup
    )

# --- Main Function ---

def main() -> None:
    """Start the bot."""
    if not BOT_TOKEN or BOT_TOKEN == 'YOUR_BOT_TOKEN_HERE':
        logger.error("❌ BOT_TOKEN not set! Please set it in Railway environment variables.")
        return

    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("channel", channel_command))

    # Start the Bot
    logger.info("🤖 Bot is starting...")
    logger.info(f"📢 Channel link: {CHANNEL_LINK}")
    logger.info("✅ Bot is running!")

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
