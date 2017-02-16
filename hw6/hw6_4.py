import random, sys
def generator_function():
    element = 0
    while element < sys.maxsize:
        element = random.randint(element, sys.maxsize)
        yield element
for value in generator_function():
    print(value)
