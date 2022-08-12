

def get_format():
    listSplit = [',',';', ':']# список разделителей
    spr = input("Введите формат вывода (разделитель): ")
    if not spr in listSplit: spr = None
    return spr



def input_data(): # ввод новых данных
    data = []
    data.append (input("Введите фамилию: "))
    data.append(input ("Введите имя: "))
    data.append(input("Введите телефон: "))
    data.append(input("Добавьте описание: "))
    return data

def write_data(data, spr): # запись новых данных в файл
    with open('phone.csv', 'a+') as file:
        if spr == None:
            for el in data:
                file.write(f"{el}\n") # если разделитель не выбран то 
            file.write(f"\n")         
        else:
            file.write(spr.join(data)) # записываем данные через разделитель spr
            file.write(f"\n")