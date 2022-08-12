
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
# updater = Updater('5379686390:AAFIiCXzN0uNNIOeRUl5riDTXrzfSA3n3b8')
app = ApplicationBuilder().token("5379686390:AAFIiCXzN0uNNIOeRUl5riDTXrzfSA3n3b8").build()
app.add_handler(CommandHandler("hello", hi_command))
# app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", hi_command))
app.add_handler(CommandHandler("start", hi_command))
app.add_handler(CommandHandler("calc", calc_command))

app.run_polling()
