"""Pytest module to test sources as blackbox."""
from pizza_factory.factory import Machine
from pytest import fixture


class TestMachine:
    @fixture(scope="function")
    def machine(self):
        return Machine()

    def test_has_make(self, machine):
        assert hasattr(machine, "cook")
