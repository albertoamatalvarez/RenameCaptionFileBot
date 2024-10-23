from os.path import splitext


async def start(update, context):
    await update.message.reply_text(
        "Hola! Reenviame uno o varios videos y trataré de renombrar el caption según su filename"
    )


# Función que maneja los archivos recibidos
async def handle_video(update, context):
    video = update.message.video
    file_name = splitext(video.file_name)[0] if video.file_name else 'Sin nombre'
    await update.message.reply_video(video.file_id, caption=file_name)
