"""Pytest configuration file."""

import pytest
from template import module

# configurations ----------------------------------------------------


# module fixtures ---------------------------------------------------
@pytest.fixture(scope='module')
def tmpdir_name(request):
    print("\t MODULE_FIXTURE: tmpdir_name ", request.param)
    return request.param


@pytest.fixture(scope='module')
def temp_dir(tmpdir_factory, tmpdir_name):
    temp_dir = tmpdir_factory.mktemp(tmpdir_name)
    print("\t MODULE_FIXTURE: temp_dir ", temp_dir)
    return temp_dir


@pytest.fixture(scope='module')
def db_filename(request):
    print("\t MODULE_FIXTURE: db_filename ", request.param)
    return request.param


@pytest.fixture(scope='module')
def items(request):
    """Returns a dictionary of key-value items"""
    print("\t CLASS_FIXTURE: items ", request.param)
    return request.param


@pytest.fixture(scope='module')
def db_path(temp_dir, db_filename, items):
    database = module.Database()
    [database.add(k, v) for k, v in items.items()]
    db_path = temp_dir.join(db_filename)
    database.save(db_path)
    print("\t MODULE_FIXTURE: db_path ", db_path)
    return db_path


# class fixtures --------------------------------------------------
@pytest.fixture(scope='class')
def class_database(items):
    """Returns a class shared database with some items already"""
    print("\t CLASS_FIXTURE: class_database")
    database = module.Database()
    [database.add(k, v) for k, v in items.items()]
    return database


# function fixtures -------------------------------------------------
@pytest.fixture(scope='function')
def empty_database():
    """Returns a completely new and empty database"""
    print("\t FUNCTION_FIXTURE: new_database")
    return module.Database()


@pytest.fixture(scope='function')
def database(empty_database, items):
    """Returns a new database but with some items already"""
    print("\t FUNCTION_FIXTURE: database")
    database = empty_database
    [database.add(k, v) for k, v in items.items()]
    return database
