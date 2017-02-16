import time

def timer_of_func(function_to_decorate):
    def wrapper_of_func(*args):
        begint = time.time()
        function_to_decorate(*args)
        endt = time.time()
        print('The execution time of function - {} sec.'.format(endt - begint))
    return wrapper_of_func
@timer_of_func
def the_first_func():
    print('Hello, my dear')
    a = 876
    b = [i*2 for i in range(a)]
    print(b)
    
@timer_of_func
def the_second_func(*names):
    list_of_names = []
    for i in names:
        list_of_names.append(i)
    print(list_of_names)    

@timer_of_func
def the_third_function(*elements):
    summ = 0
    for i in elements:
        summ += i
    list_new = [i for i in range(0, summ)]
    print(list_new)


the_first_func()
the_second_func('dsjgbhdf', 'dsjgbhdf', 'dsjgbhdf', 'dsjgbhdf')
the_third_function(39, 86, 56, 2)