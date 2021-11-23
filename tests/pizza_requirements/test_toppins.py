"""Pytest module to test sources as blackbox."""
from pizza_factory import ingredients
from pytest import fixture


class TestPepperoni:
    @fixture(scope="class")
    def pepperoni(self):
        return ingredients.Pepperoni()

    def test_is_red(self, pepperoni):
        assert pepperoni.color == "red"

    def test_is_round(self, pepperoni):
        assert pepperoni.shape == "round"


class TestMushroom:
    @fixture(scope="class")
    def mushroom(self):
        return ingredients.Mushroom()

    def test_is_grey(self, mushroom):
        assert mushroom.color == "grey"

    def test_is_not_round(self, mushroom):
        assert mushroom.shape != "round"

    def test_is_not_square(self, mushroom):
        assert mushroom.shape != "square"


class TestCheese:
    @fixture(scope="class")
    def cheese(self):
        return ingredients.Cheese()

    def test_is_yellow(self, cheese):
        assert cheese.color == "yellow"

    def test_is_grated(self, cheese):
        assert cheese.shape == "grated"


class TestOnion:
    @fixture(scope="class")
    def onion(self):
        return ingredients.Onion()

    def test_is_white(self, onion):
        assert onion.color == "white"

    def test_is_grated(self, onion):
        assert onion.shape == "grated"


class TestPepper:
    @fixture(scope="class")
    def pepper(self):
        return ingredients.Pepper()

    def test_is_white(self, pepper):
        assert pepper.color in ["red", "green"]

    def test_is_grated(self, pepper):
        assert pepper.shape == "grated"
