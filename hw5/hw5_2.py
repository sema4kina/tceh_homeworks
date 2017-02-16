class IntToStr(object):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return '{}'.format(self.value)
    def __add__(self, object_to_add):
        return str(self.value) + str(object_to_add)
    def __radd__(self, object_to_add):
        return str(object_to_add) + str(self.value)
 
obj = IntToStr(10.5)
print(obj + 'ads')    
print(obj)
print('adf' + obj)