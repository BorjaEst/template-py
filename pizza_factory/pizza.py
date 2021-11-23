class Pizza:
    def __init__(self, toppings, dough) -> None:
        self.toppings = toppings
        self.dough = dough

    @property
    def baked(self):
        return self.dough.baked

    def bake(self):
        self.dough.bake()

    def taste(self):
        if self.baked:
            return "Good!"
        else:
            raise Exception("Not baked!")


class Dough:
    def __init__(self, ingredients) -> None:
        self.flour = ingredients.pop("flour", "0 g")
        self.water = ingredients.pop("water", "0 ml")
        self.salt = ingredients.pop("salt", "0 g")
        self.yeast = ingredients.pop("yeast", "0 g")
        self.olive_oil = ingredients.pop("olive_oil", "0 g")
        self.color = "white" if self.flour != "0 g" else "green"
        self.shape = "round" if self.water != "0 g" else "None"
        self.__baked = False

    @property
    def baked(self):
        return self.__baked

    def bake(self):
        self.__baked = True

    def taste(self):
        if self.baked:
            return "Good!"
        else:
            raise Exception("Not baked!")
