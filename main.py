import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'SECRET.ENV'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Hola te Saluda Ecuabyte Innovations ")
    except Exception as e:
        logger.error(f"Error al iniciar la conversacion: {e}")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        help_text = (
            "¡Hola! Soy tu asistente.\n\n"
            "/start: Inicia una conversación conmigo.\n"
            "/services: Muestra los Servicios Ofrecidos\n"
            "/contact: Muestra el correo de contacto\n"
            "/help: Muestra este mensaje de ayuda."
        )
        await update.message.reply_text(help_text)
    except Exception as e:
        logger.error(f"Error al seleccionar: {e}")


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_text("Puedes contactarnos en: gv8536892@gmail.com")
    except Exception as e:
        logger.error(f"Error while replying to the user: {e}")


async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        keyboard = [
            [
                InlineKeyboardButton("Software Rapid Secure", url='https://rapidsecure.duckdns.org'),
                InlineKeyboardButton("EcuaByte Innovations"
                                     "", url='https://ecubyte-innovations.duckdns.org')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            "Ecuabyte Innovations ofrece los siguientes servicios:",
            reply_markup=reply_markup
        )
    except Exception as e:
        logger.error(f"Error while replying to the user: {e}")

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    service = query.data

    if service == 'RapidSecure':
        response = "Software para Monitorear y Reportar problemas de Red"
    elif service == 'Software':
        response = "Desarrollo e Implementacion de Software a Medida"
    else:
        response = "Lo siento, no reconozco esa opción."

    await query.answer()
    await query.edit_message_text(text=response)


def main():
    """Start the bot and set up handlers."""
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help))
    application.add_handler(CommandHandler('contact', contact))
    application.add_handler(CommandHandler('services', services))
    application.add_handler(CallbackQueryHandler(button))

    logger.info("Bot started!")
    application.run_polling()


if __name__ == "__main__":
    main()
