def read_data():
    listSplit = [',',';', ':']# список разделителей
    with open('phone.csv', 'r') as file:
        data = []
        temp = []
        for line in file:
            flag=0
            for el in listSplit: 
               if el in line:#если в строке есть разделитель
                flag = 1
                data.append(line.strip().split(el)) #получаем список списков

           
            if line != '' and flag == 0: 
                if line != '\n':        
                    temp.append(line.strip()) 
                else:
                    data.append(temp) #при пустой строке с \n записываем список в список списков
                    temp= []
    return data

def output_data(dt):
    if len(dt) > 0:
        print("_"*88)
        print("Фамилия".center(15), "Имя".center(15), "Телефон".center(15), "Описание".center(40))
        print("_"*88)
        for el in dt:
            print(el[0].center(15), el[1].center(15), el[2].center(15),el[3].center(40,'.'))
    else:
        print("Справочник пока не содержит данных")
    print('_'*88)
    print()