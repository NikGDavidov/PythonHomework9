from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from spy import *

from telegram.ext import Updater, CommandHandler, CallbackContext, ContextTypes

from import_input import write_data

from export_output import read_data

from find_name import find_name

from delete import delete

# global arr

async def hi_command (update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')
    await update.message.reply_text(f'Выберите действие')
    await update.message.reply_text(f'\n/1 ->вывод всего справочника\n/2 текст -> поиск текста в справочнике\n/3 имя фамилия телефон описание -> добавление контакта;\n /4 текст -> удаление контакта')
    
    log(update, context)

# 1 (вывод в чат всего справочника)
async def printAll_command(update: Update, context: CallbackContext):
 log(update, context)
 dt = read_data()
 if len(dt)>0 : await print_data(dt,update,context)
 else :
       await update.message.reply_text(f'{"Данные пока не заведены. Можете добавить данные выбрав опцию 3."}')

# вывод в чат
async def print_data(dt,update:Update, context:CallbackContext):
   
    if len(dt) > 0:
       
        await update.message.reply_text (f"Фамилия  Имя Телефон  Описание")
       
        for el in dt:
            s = ''
            for item in el:
                s += f"{item}  "
            
            await update.message.reply_text (s)
    else:
         await update.message.reply_text (f"Справочник пока не содержит данных")


# 2 (поиск)
async def find_command(update: Update, context: CallbackContext):
 log(update, context)

#  await update.message.reply_text(f'Введите данные для поиска')
 msg = update.message.text
 
 items = msg.split() 
 info= items[1]
 data = read_data()
 el = find_name(info, data)
 if len(el)>0:
            await update.message.reply_text("Нашлись следующие данные:")
            await print_data(el, update, context )
            
 else:
          await update.message.reply_text ("Данные не обнаружены")

# 3 (добавление контакта)
async def write_command (update: Update, context: CallbackContext):
  msg = update.message.text
  items = msg.split() 
  items.pop(0)
  write_data(items,',')

# 4 (удаление контакта)

async def delete_command (update: Update, context: CallbackContext):
  global arr
  arr =[]
  msg = update.message.text
  items = msg.split()
  info = items[1]
  data = read_data()
  arr = find_name(info, data)
  if len(arr)>0:
            await update.message.reply_text ("Нашлись следующие данные для удаления:")
            await print_data(arr, update, context )
            await update.message.reply_text("Введите команду /del и через пробел индексы строк, которые вы хотите удалить (индекс верхней строчки = 0). ")
            await update.message.reply_text("например /del 0 2) ")
            # indexDel =st.split()
            # listDel =[]
            # for i in indexDel:
            #     x = int(i)
            #     if x>=0 and x< len(el): listDel.append(el[x])
            # delete(listDel)
  else:
            await update.message.reply_text("Данные не обнаружены.")


async def delete_rows_command (update: Update, context: CallbackContext):
  print(f'arr  {arr}')
  msg = update.message.text
  indexDel = msg.split()
  indexDel.pop(0)
  listDel =[]
  for i in indexDel:
      x = int(i)
      if x>=0 and x< len(arr): listDel.append(arr[x])
  delete(listDel)

