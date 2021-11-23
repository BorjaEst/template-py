"""Pytest module to test sources as blackbox."""
import types

import yaml
from pizza_factory.factory import Factory
from pizza_factory.pizza import Dough
from pytest import fail, fixture, raises


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


class TestDoughFromMachine:
    @fixture(scope="class", autouse=True)
    def dough(self, factory, dough_style):
        return factory.make(Dough, style=dough_style)

    def test_is_white(self, dough):
        assert dough.color == "white"

    # TODO: Except those which are squared
    def test_is_round(self, dough):
        assert dough.shape == "round"

    def test_tastes_good(self, dough):
        assert hasattr(dough, "taste")
        assert type(dough.taste) == types.MethodType
        try:
            dough.taste()
        except Exception as reason:
            fail(reason)


class TestWithoutMachine:
    @fixture(scope="class", autouse=True)
    def dough(self, recipes, dough_style):
        ingredients = recipes["dough"][dough_style]
        return Dough(ingredients)

    def test_tastes_bad(self, dough):
        with raises(Exception):
            dough.taste()
