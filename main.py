import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

#Debugeamos
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = ''

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the /start command."""
    try:
        await update.message.reply_text("Hola")
    except Exception as e:
        logger.error(f"Error while replying to the user: {e}")

def main():
    """Start the bot and set up handlers."""
    application = Application.builder().token(TOKEN).build()

    # Con start llamas la funcion
    application.add_handler(CommandHandler('start', start))

    # Info
    logger.info("Bot started!")
    application.run_polling()

if __name__ == "__main__":
    main()
