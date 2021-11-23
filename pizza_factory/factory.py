"""Pizza factory module"""
from pizza_factory.pizza import Dough, Pizza


class Factory:
    def __init__(self, location, recipes) -> None:
        self.location = location
        self.recipes = recipes
        self.machine = Machine()

    def make(self, order, **kwargs):
        match order:
            case order if order == Pizza:
                product = self.do_pizza(**kwargs)
            case order if order == Dough:
                product = self.do_dough(**kwargs)
            case _other:
                raise KeyError("Unknown recipe order")
        self.machine.cook(product)
        return product

    def do_pizza(self, name="Margarita", **dough_kwargs):
        toppings = self.recipes['pizza'][name]
        dough = self.do_dough(**dough_kwargs)
        return Pizza(toppings, dough)

    def do_dough(self, style="Neapolitan"):
        ingredients = self.recipes['dough'][style]
        return Dough(ingredients)

class Machine:
    def cook(self, product):
        product.bake()
        return True

