"""Pytest module to test sources as blackbox."""
import uuid

from pizza_factory.factory import Factory, Machine
from pytest import fixture, mark


@fixture(scope="class")
def name(request):
    return request.param if hasattr(request, "param") else None


@fixture(scope="class")
def location(request):
    return request.param if hasattr(request, "param") else None


@mark.parametrize("name", ["Dominos", "Pizza Hut"], indirect=True)
@mark.parametrize("location", ["Valencia", "Karlsruhe"], indirect=True)
class TestFactory:
    @fixture(scope="class", autouse=True)
    def factory(self, name, location):
        return Factory(name=name, location=location)

    def test_name(self, factory, name):
        assert hasattr(factory, "name")
        assert type(factory.name) == str
        assert factory.name == name

    def test_location(self, factory, location):
        assert hasattr(factory, "location")
        assert type(factory.location) == str
        assert factory.location == location


@fixture(scope="class")
def id(request):
    return request.param if hasattr(request, "param") else None


@mark.parametrize("id", [uuid.uuid4() for _ in range(2)], indirect=True)
class TestMachine:
    @fixture(scope="class", autouse=True)
    def machine(self, id):
        return Machine(id)

    def test_has_id(self, machine, id):
        assert hasattr(machine, "id")
        assert type(machine.id) == uuid.UUID
        assert machine.id == id

    def test_has_make(self, machine):
        assert hasattr(machine, "make")

    def test_has_state(self, machine):
        assert hasattr(machine, "running")
        assert type(machine.running) == bool
