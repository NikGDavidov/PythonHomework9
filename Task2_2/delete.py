from export_output import read_data
from import_input import write_data
def delete (listDel):
    data = read_data()
    newData =[]
    for el in data:
        if not el in listDel:
            newData.append(el)
 # print(newData)
    f = open('phone.csv', 'w')
    f.close()
    for line in newData:
        write_data(line,',')




   

