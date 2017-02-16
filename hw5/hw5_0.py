class Products(object):
    def __init__(
        self, name, price, count,
        kilo = False, quantity = False,
        litres = False, is_edible = True
        ):
        self.name = name
        self.price = price
        self.count = count
        self.kilo = kilo
        self.quantity = quantity
        self.litres = litres
        self.is_edible = is_edible
    def summ(self):
        return (self.price * self.count) * 0.95 if self.quantity == True and self.count >= 2 else self.price * self.count
class Basket(object):
    def __init__(self, free_space):
        self.free_space = free_space
    def add_to_basket(self, product):
        if product.is_edible == True:
            self.free_space -= 1
        else:    
            print('{} is bad. Don\'t take it please'.format(product.name))
        return self.free_space    


my_bag = Basket(15)
lemon = Products('Lemon', 50, 3, 1, False, True, False)
milk = Products('Milk', 50, 1, False, False, True, True)
print(lemon.summ())
print(milk.summ())
my_bag.add_to_basket(lemon)
my_bag.add_to_basket(milk)
print(my_bag.free_space)