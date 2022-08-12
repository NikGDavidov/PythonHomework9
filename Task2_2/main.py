from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler,ConversationHandler,filters
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *
import bot_commands
import logging
import telegram
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)

from uuid import uuid4

from telegram import  InputTextMessageContent
from telegram.ext import Updater, CommandHandler, filters, MessageHandler, ConversationHandler
import logging
import subprocess 


app = ApplicationBuilder().token("5569969152:AAEuxm6002_Ju-VwYxX9eSANeh6U_RGI5uk").build()

# bot_commands.arr = []

app.add_handler(CommandHandler("hello", hi_command))
app.add_handler(CommandHandler("help", hi_command))
app.add_handler(CommandHandler("start", hi_command))
app.add_handler(CommandHandler("1", printAll_command))
app.add_handler(CommandHandler("2", find_command))
app.add_handler(CommandHandler("3", write_command))
app.add_handler(CommandHandler("4", delete_command))
app.add_handler(CommandHandler("del", delete_rows_command))
app.run_polling()
