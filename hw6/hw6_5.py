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
                yield d
            else:
                d = d.replace(month = d.month + 1, day = 1)
                yield d    

for i in generator_of_date():
    print(i)

# Для пошагового вызова необходимо присвоить функцию переменной и вызвать next(переменная_функции). Например:
# function = generator_of_date()
# next(function)    