import datetime
def generator_of_date():
    d = datetime.date.today()
    while True:
        try:
            d = d.replace(day = d.day + 1)
            yield d
        except ValueError:
            if d.month == 12:
                d = d.replace(year = d.year + 1, month = 1, day = 1)
<<<<<<< HEAD
                yield d
            else:
                d = d.replace(month = d.month + 1, day = 1)
                yield d    
=======
                yield d   # Без этой строчки у меня пропускались все 1 января
            else:
                d = d.replace(month = d.month + 1, day = 1)
                yield d   # А без этой строчки все первые числа месяца
>>>>>>> 5c25dc15c7d2526c350c053cce8d411976c60ec3

for i in generator_of_date():
    print(i)

# Для пошагового вызова необходимо присвоить функцию переменной и вызвать next(переменная_функции). Например:
# function = generator_of_date()
# next(function)    
