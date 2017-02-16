class Human(object):
	def __init__(self, name):
		self.name = name
class Animal(object):
    def __init__(self, name, danger = False):
        self.name = name
        self.danger = danger
    def is_dangerous(animal):
        if animal.danger == True:
            print('{}, это животное ({}) опасно для человека.'.format(person.name, animal.name))
        else:
            print('{} - это неопасный для человека вид, {} '.format(animal.name, person.name))
person = Human('Mike')
animal1 = Animal('Anaconda', True)
animal2 = Animal('Khorek')
animal1.is_dangerous()            #Для себя вызвала метод двумя способами. Просто чтоб понять
Animal.is_dangerous(animal2)      #Собственно, вот и второй.