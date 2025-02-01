import logging
from os.path import splitext

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update, context):
    logger.info("Received /start command from user %s", update.effective_user["username"])
    await update.message.reply_text(
        "Hola! Reenviame uno o varios videos y trataré de renombrar el caption según su filename"
    )


# Función que maneja los archivos recibidos
async def handle_video(update, context):
    video = update.message.video
    file_name = splitext(video.file_name)[0].replace('_', ' ') if video.file_name else 'Sin nombre'
    logger.info("Received video %s from user %s", file_name, update.effective_user["username"])
    await update.message.delete()
    await update.message.reply_video(video.file_id, caption=file_name)


