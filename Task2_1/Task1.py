# 1) 1. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:*

# 2+2 => 4;

# 1+2*3 => 7;

# 1-2*3 => -5;

# - Добавьте возможность использования скобок, меняющих приоритет операций.

# *Пример:*

# 1+2*3 => 7;

# (1+2)*3 => 9;
# Доделать реализацию функции eval со скобками

# избавляемся от скобок
def noBrackets(stroka):
     while"(" in stroka:
        index_of_braket1 = stroka.find('(')

        index_of_braket2 = stroka.find(')')
        
        substroka = stroka[index_of_braket1:index_of_braket2+1] 
        # index_of_braket3 = stroka[index_of_braket1:].find('(')
        # if index_of_braket3 >0 and index_of_braket3<index_of_braket2: 
        # noBrackets(substroka) #на случай двойных/тройных скобок  не доделал// цейтнот
        temp = plusMinus(dm(substroka[1:-1]))
        stroka = stroka.replace(substroka,temp)
     return stroka

# умножаем и делим
def dm(stroka):
   
        stroka_after_dm = stroka
    
        for i in range (len(stroka)-1):
            index_del_from = 0
            index_del_to = 0 
        
            if stroka[i]=="*" or stroka [i] =='/':
                multyplier1 =''
                multyplier2 =''
                j=0
                for j in range (i):
                    if stroka[i-1-j].isdigit():
                        multyplier1 += stroka[i-1-j]
                        if i-1-j ==0:multyplier1 = multyplier1[::-1]
             
                    else: 
                        multyplier1 = multyplier1[::-1]
                        index_del_from =i-j
                        break
                for j in range (len(stroka)-i-1):
                    if stroka[i+1+j].isdigit():
                        multyplier2 += stroka[i+1+j]
                        if i+1+j==len(stroka)-1:
                            index_del_to = i+1+j
                            break
                    else: 
                        index_del_to = i+1+j
                        break
                if stroka[i] =='*': res = int(multyplier1) * int (multyplier2)
                else: res = int( int(multyplier1) / int (multyplier2) )
             
                if index_del_to == len(stroka)-1:stroka_after_dm = stroka_after_dm.replace(stroka[index_del_from:], str(res))
                else: stroka_after_dm = stroka_after_dm.replace(stroka[index_del_from:index_del_to], str(res))
                # print (stroka_after_dm)
        if "*" in stroka_after_dm or '/' in stroka_after_dm : return dm (stroka_after_dm) #  * и / могут идти подряд, пришлось добавить рекурсию
        else: return(stroka_after_dm)
       
 # а теперь складываем и вычитаем (умножение и деление было бы проще сделать тут же через список, но уже сделано)
def plusMinus(stroka_dm):
    sum = 0
    listSplit = ['+','-']
    listNum =[]
    listSigns=[]
    temp =''
    elements = stroka_dm
    if stroka_dm[0] =='-': elements = stroka_dm[1:]
    for el in elements:
        if el not in listSplit:
            temp +=el
        else:
            listNum.append(temp)
            listSigns.append(el)
            temp =''
    listNum.append(temp)
    # print(listNum)
    # print(listSigns)
    sum = int (listNum[0])
    if stroka_dm[0]=="-" : sum = - sum
    for i in range (1,len(listNum)):
        if listSigns[i-1] == '+': sum += int(listNum[i])
        else: sum -= int(listNum[i])
    return str(sum)
    

#начало кода
def calc(stroka):
# stroka = '-2*2*4/(1+1)-(5+1)*2+2*6*2'
# st = noBrackets(stroka)
# # print(st)
# st1 = dm(st)
# # print(st1)
# # st2 = plusMinus(st1) 
    st2 = plusMinus(dm(noBrackets(stroka)))
    return(f'{stroka} -> {st2}')


