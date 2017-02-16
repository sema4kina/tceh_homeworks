def my_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper():
        print("We\'re going to call the function")
        print("But the function {} won\'t be called".format(function_to_decorate.__name__))
    # Возвращаем функцию
    return the_wrapper

# Та функция, которую необходимо положить в обёртку "декоратора"
@my_new_decorator
def function_to_call():
    print("I can be called.")

function_to_call()