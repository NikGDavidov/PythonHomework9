from import_input import get_format
from import_input import input_data
from import_input import write_data

from export_output import read_data
from export_output import output_data

from find_name import find_name

from delete import delete


def start():
  flag = 1
  while flag ==1:
    print( "Выберите действие: \n\
           1 - вывод всех контактов;\n\
           2 - поиск контакта по имени;\n\
           3 - добавление контакта;\n\
           4 - удаление контакта;\n\
           5 - выход из программы")

    mode = input("             : ")
    if mode == '5':
        print ("Всего доброго!") 
        flag = 0
        break
    
    if mode == '1':
       data = read_data()
       if len(data)>0 : output_data(read_data())
       else :
            print("Данные пока не заведены. Можете добавить данные выбрав опцию 3.")
    if mode== '3':
        fr = get_format()
        write_data(input_data(), fr)
   
    if mode == '2':
        info = input("Введите имя для поиска: ")
        data = read_data()
        el = find_name(info, data)
        if len(el)>0:
            print ("Нашлись следующие данные:")
            output_data(el)
            
        else:
            print("Данные не обнаружены")

    if mode =="4":
        info = input("Введите имя для удаления: ")
        data = read_data()
        el = find_name(info, data)
        if len(el)>0:
            print ("Нашлись следующие данные для удаления:")
            output_data(el)
            st = input("Введите через пробел индексы строк, которые вы хотите удалить (индекс верхней строчки = 0). ")
            indexDel =st.split()
            listDel =[]
            for i in indexDel:
                x = int(i)
                if x>=0 and x< len(el): listDel.append(el[x])
            delete(listDel)
        else:
            print("Данные не обнаружены.")
    input("Нажмите enter для продолжения.")

        