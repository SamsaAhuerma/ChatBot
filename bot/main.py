from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, JobQueue
from bot.handlers import start, menu_callback, handle_message
from bot.weather import check_temperature
from dotenv import load_dotenv
import os


load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
OWM_API_KEY = os.getenv("OWM_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configuración principal del bot!
def main():

    application = Application.builder().token(BOT_TOKEN).build()

    job_queue = application.job_queue
    job_queue.run_repeating(check_temperature, interval=600, first=0)


    print("BOT IS RUNNING\n")
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(menu_callback))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
   

    application.run_polling()

if __name__ == '__main__':
    main()