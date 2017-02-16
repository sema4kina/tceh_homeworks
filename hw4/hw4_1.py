class Person(object):
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.friends_list = []
    def know(self, Person):
        self.friends_list.append(Person)
    
    def is_known(self, person):
        if person in self.friends_list:
            print('{}, мы знакомы. '.format(person))
        else:
            print('{}, мы ещё не знакомы. '.format(person))
me = Person(25, 'Mary')
me.know('Viktor')
me.know('Alex')
me.is_known('Viktor')                
me.is_known('Adrej')   