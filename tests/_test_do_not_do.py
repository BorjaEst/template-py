"""My bad testing example."""
import pizza_factory


def test_my_pizza_margarita():
    # I am going to do a setup here
    parameter1 = "Valencia"
    parameter2 = {"dough": {"...": {}}, "pizza": {}}
    factory = pizza_factory.factory(parameter1, parameter2)
    assert factory.location == "Valencia"
    Pizza = pizza_factory.pizza.Pizza
    pizza = factory.make(Pizza, "Margarita", "New York")
    pizza.toppings
    assert "dough" in pizza
    assert "tomato" in pizza.toppings
    assert "cheese" in pizza.toppings
