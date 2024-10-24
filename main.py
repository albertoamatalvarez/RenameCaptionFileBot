from decouple import config
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler

from handler.handler import start, handle_video, handle_photo

# Define tu token de bot
TOKEN = config('TELEGRAM_TOKEN')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Añadimos el comando start
    app.add_handler(CommandHandler('start', start))
    # Añadimos el manejador para archivos de tipo video
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))
    # Añadimos el manejador para archivos de tipo imagen
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    # Iniciamos el bot
    app.run_polling()
