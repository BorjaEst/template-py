"""Pytest module to test sources as blackbox."""

import os
import pytest


def pytest_generate_tests(metafunc):
    metafunc.parametrize("tmpdir_name", ['backup_tests'], indirect=True)


class TestSave:
    """Functional tests for 'Save' database."""

    @pytest.mark.parametrize('items', [{'x': 1, 'y': 2}], indirect=True)
    def test_database_is_saved(self, database, temp_dir):
        path = temp_dir.join("db1.mydb")
        assert not os.path.isfile(path)
        assert database.save(path) is None  # No return value
        assert os.path.isfile(path)


@pytest.mark.parametrize('db_filename', ["db1.mydb"], indirect=True)
class TestLoad:
    """Functional tests for 'Load' database."""

    @pytest.mark.parametrize('items', [{'a': 1, 'b': 2}], indirect=True)
    def test_existing_returns_value(self, db_path, empty_database):
        database = empty_database
        assert database.keys == []
        assert database.load(db_path) is None  # No return value
        assert database.keys == ['a', 'b']
        assert database.get('a') == 1
        assert database.get('b') == 2
