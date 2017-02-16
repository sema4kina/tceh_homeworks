#1 Возведение числа в степень
digit = int(input('Введите число - '))
degree = int(input('В какую степень возвести? '))

def operation(x, y):
    print('Спасибо, ваш ответ -', pow(x,y))
    return pow(x, y)

operation(digit, degree)    

#2 Нахождение НОК
x = int(input('Введите первое число  '))
y = int(input('Введите второе число  '))

def nok(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b 
        else: b = b % a
    return a + b

nod = nok(x, y)
print ('НОК = ', (x * y) / nod) 

#3 Подсчёт количества элементов с одинаковым типом данных в списке

list1 = [1, 'abc', '123', 4.5, None]
listtypes = {}

def count_types(thelist):
    global listtypes
        for element in thelist:
            if type(element) not in listtypes:
            listtypes.update({type(element): 1})
        else:
            listtypes[type(element)] += 1
    return listtypes

count_types(list1)  
print(listtypes)

#4 Сравнение словарей и вывод общих ключей

list1 = {1: 45, 'a': 28, 'sdf': 'abv'}
list2 = {1: 'sdf', 'ed': 817, 'sdf': 'abv'}

def compare_lists(a, b):
    ij_count = 0
    for i in a.keys():
        for j in b.keys():
            if i == j:
                ij_count += 1
    print(ij_count)
compare_lists(list1, list2)             

#5 Список аргументов  --> список типов аргументов

new_list = []
def find_types(*l):
    global new_list
    for i in l:
        new_list.append(type(i))
    return new_list
find_types(1, 34, 'df', 3.4, None)   
print(new_list) 

#6 Список списков --> Матрица

list1 = [[1, 2, 3], [2, 4, 6], [7, 3, 6]]

def matrix_print(l):
    for raw in l:
        x = ''
        for element in raw:
            x = x + ' '+ str(element)  # Думаю, так будет симпатичнее
        print(x)
            
matrix_print(list1)

#7 Список из списков --> список из уникальных аргументов

list1 = [['s', 34, 'b'], [34, 'c', 'dc'], ['b', 2, 2]]
def join_list(l):
    result = []
    for list2 in l:
        for element in list2:
            if element not in result:
                result.append(element)
    return result   

print(join_list(list1)) 