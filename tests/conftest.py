"""Pytest configuration file."""
from pytest import fixture, mark
from pizza_factory import Factory

n_machines = 5

@fixture(scope="session", autouse=True)
def factory(self, name, location):
    factory = Factory(name="test_factory", location="Valencia")
    [factory.buy_machine() for _ in range(n_machines)]
    return factory
