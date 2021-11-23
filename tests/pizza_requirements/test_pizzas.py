"""Pytest module to test sources as blackbox."""
import yaml
from pizza_factory.factory import Factory
from pizza_factory.pizza import Dough, Pizza
from pytest import fixture


@fixture(scope="module")
def factory(recipes):
    return Factory(location="Valencia", recipes=recipes)


@fixture(scope="module")
def recipes():
    with open("tests/recipes.yaml", "r") as stream:
        return yaml.safe_load(stream)


@fixture(scope="class", params=["Neapolitan", "New York"])
def dough_style(request):
    return request.param if hasattr(request, "param") else None


class IsPizza:  # Common tests between all pizzas
    def test_has_dough(self, pizza):
        assert hasattr(pizza, "dough")
        assert type(pizza.dough) == Dough

    def test_has_tomato(self, pizza):
        assert "tomato" in pizza.toppings

    def test_has_cheese(self, pizza):
        assert "cheese" in pizza.toppings


class TestMargarita(IsPizza):
    @fixture(scope="class")
    def pizza(self, factory, dough_style):
        return factory.make(Pizza, name="Margarita", style=dough_style)

    def test_only_2_toppings(self, pizza):
        assert len(pizza.toppings) == 2


class TestVegetarian(IsPizza):
    @fixture(scope="class")
    def pizza(self, factory, dough_style):
        return factory.make(Pizza, name="Vegetarian", style=dough_style)

    def test_has_no_meet(self, pizza):
        assert "pepperoni" not in pizza.toppings


class TestPeperoni(IsPizza):
    @fixture(scope="class")
    def pizza(self, factory, dough_style):
        return factory.make(Pizza, name="Pepperoni", style=dough_style)

    def test_has_pepperoni(self, pizza):
        assert "pepperoni" in pizza.toppings
