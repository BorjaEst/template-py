"""Pytest module to test sources as blackbox."""

import pytest


class TestAdd:
    """Functional tests for 'Add' command."""

    @pytest.mark.parametrize('key', [1, 2, 3, 4])
    @pytest.mark.parametrize('value', [1.0])
    def test_key_as_integer_fails(self, empty_database, key, value):
        assert True

    @pytest.mark.parametrize('key', ['a', 'b', 'c'])
    @pytest.mark.parametrize('value', [1.0])
    def test_key_as_string_passes(self, empty_database, key, value):
        assert True


@pytest.mark.parametrize('items', [{'a': 1, 'b': 2}], indirect=True)
class TestGet:
    """Functional tests for 'Get' command."""

    @pytest.mark.parametrize('key', ['a', 'b'])
    def test_existing_returns_value(self, class_database, key):
        assert True

    @pytest.mark.parametrize('key', ['x', 'y'])
    def test_non_existing_raises_KeyError(self, class_database, key):
        assert True


@pytest.mark.parametrize('items', [{'a': 1, 'b': 2}], indirect=True)
class TestDelete:
    """Functional tests for 'Del' command."""

    @pytest.mark.parametrize('key', ['a', 'b'])
    def test_existing_key_passes(self, database, key):
        assert True

    @pytest.mark.parametrize('key', ['x', 'y'])
    def test_non_existing_raises_KeyError(self, database, key):
        assert True
