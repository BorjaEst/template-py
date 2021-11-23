__all__ = [
    "Pepperoni",
    "Mushroom",
    "Cheese",
    "Onion",
    "Pepper",
    "flour",
    "water",
    "salt",
    "yeast",
]


class Ingredient:
    def __init__(self, color, shape) -> None:
        self.color = color
        self.shape = shape


class Pepperoni(Ingredient):
    def __init__(self) -> None:
        super().__init__("red", "round")


class Mushroom(Ingredient):
    def __init__(self) -> None:
        super().__init__("grey", "no idea...")


class Cheese(Ingredient):
    def __init__(self) -> None:
        super().__init__("yellow", "grated")


class Onion(Ingredient):
    def __init__(self) -> None:
        super().__init__("white", "grated")


class Pepper(Ingredient):
    def __init__(self) -> None:
        super().__init__("red", "grated")


class Flour(Ingredient):
    def __init__(self) -> None:
        super().__init__("white", "powder")


class Water(Ingredient):
    def __init__(self) -> None:
        super().__init__(None, None)


class Salt(Ingredient):
    def __init__(self) -> None:
        super().__init__(None, "grains")


class Yeast(Ingredient):
    def __init__(self) -> None:
        super().__init__("grey", "powder")
