from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from telegram.ext import Updater, CommandHandler, CallbackContext
from Task1 import calc

async def hi_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')
    await update.message.reply_text("Введите команду /calc и через пробел математическое выражение, например /calc -1*2+9/(4-1)+5 ")
    log(update, context)

# def hi_command(update: Update, context: CallbackContext):
#  log(update, context)
# #  update.message.reply_text(f'Hi {update.effective_user.first_name}!')
# async def help_command(update: Update, context: CallbackContext):
#  log(update, context)
#  await update.message.reply_text(f'/hi\n/time\n/help\n/calc')
# async def time_command(update: Update, context: CallbackContext):
#  log(update, context)
#  await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def calc_command(update: Update, context: CallbackContext):
 log(update, context)
 msg = update.message.text

 items = msg.split() 

 result = calc(items[1])
 await update.message.reply_text(result)
