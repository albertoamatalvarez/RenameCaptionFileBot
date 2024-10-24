from decouple import config
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler

from handler.handler import start, handle_video

# Define tu token de bot
TOKEN = config('TELEGRAM_TOKEN')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Añadimos el comando start
    app.add_handler(CommandHandler('start', start))
    # Añadimos el manejador para archivos de tipo video
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))
    # Iniciamos el bot
    app.run_polling()
