"""Pytest module to test sources as blackbox."""
import yaml
from pizza_factory.factory import Factory, Machine
from pytest import fixture, mark, raises


@fixture(scope="module")
def recipes():
    with open("tests/recipes.yaml", "r") as stream:
        return yaml.safe_load(stream)


@fixture(scope="class", params=["Valencia", "Karlsruhe"])
def location(request):
    return request.param


class TestFactory:
    @fixture(scope="class")
    def factory(self, location, recipes):
        return Factory(location, recipes)

    def test_location(self, factory, location):
        assert hasattr(factory, "location")
        assert type(factory.location) == str
        assert factory.location == location

    def test_recipes(self, factory, recipes):
        assert hasattr(factory, "recipes")
        assert type(factory.recipes) == dict
        assert factory.recipes == recipes
        assert "dough" in factory.recipes
        assert "pizza" in factory.recipes

    def test_machine(self, factory):
        assert hasattr(factory, "machine")
        assert type(factory.machine) == Machine


class TestMissingLocation:
    def test_type_error(self, recipes):
        with raises(TypeError):
            Factory(recipes=recipes)


class TestMissingRecipes:
    def test_type_error(self, location):
        with raises(TypeError):
            Factory(location=location)
