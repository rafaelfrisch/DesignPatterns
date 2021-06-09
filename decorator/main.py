class Pizza:
    def getTotalCost(self):
        return self.__class__.cost

class Base(Pizza):
    cost = 0

class Decorator(Pizza):
    def __init__(self, pizza):
        self.pizza = pizza

    def getTotalCost(self):
        return self.pizza.getTotalCost() + Pizza.getTotalCost(self)

class Bacon(Decorator):
    cost = 2
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Cheese(Decorator):
    cost = 3
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

class Tomato(Decorator):
    cost = 4
    def __init__(self, pizza):
        Decorator.__init__(self, pizza)

pizza_1 = Cheese(Bacon(Base()))
print("The price for the pizza is: R$" + str(pizza_1.getTotalCost()))
