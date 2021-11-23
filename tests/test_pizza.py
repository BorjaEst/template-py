"""Pytest module to test sources as blackbox."""
from pizza_factory.pizza import Dough
from pytest import fixture, mark, fail


@fixture(scope="class")
def dough_style(request):
    return request.param if hasattr(request, "param") else None


@mark.parametrize("dough_style", ["Neapolitan", "New York"], indirect=True)
class TestDough:
    @fixture(scope="class", autouse=True)
    def dough(self, factory, dough_style):
        return factory.make(Dough, dough_style)

    def test_is_white(self, dough):
        assert dough.color == "white"

    # TODO: Except one which is square
    def test_is_round(self, dough):
        assert dough.shape == "round"

    def test_tastes_good(self, dough):
        try: dough.taste()
        except Exception as reason: fail(reason)


class TestGarnish:
    pass


class TestCheese:
    pass


class TestToppings:
    pass
