"""
Module description. This is a module example for a dummy database.
The Database main class uses a internal _dict variable to store the
key-values.
"""

import logging
import pickle


# Module configuration
logger = logging.getLogger('module')
badformat_msg = "Error: bad database file format {path}"


class Database:
    """Simple class database with interface example"""

    def __init__(self):
        logger.debug("New database instance")
        self._dict = {}

    def __str__(self):
        lines = ["{}:{}".format(k, v) for k, v in self._dict.items()]
        return '\n'.join(lines)

    @property
    def size(self):
        """Returns the number of keys stored in the database."""
        logger.debug("Accessing size property")
        return len(self._dict)

    @property
    def keys(self):
        """Returns the stored keys in the database."""
        logger.debug("Accessing keys property")
        return list(self._dict.keys())

    def add(self, key, value):
        """Adds a key-value to the database."""
        logger.debug("Adding key: %s, value: %s", key, value)
        self._dict[key] = value

    def get(self, key):
        """Gets the value from a specific key in the database."""
        logger.debug("Getting key: %s value", key)
        return self._dict[key]

    def delete(self, key):
        """Deletes a specific key-value from the database."""
        logger.debug("Deleting key: %s and value", key)
        self._dict.pop(key)

    def save(self, path):
        """Saves the database in a specific file."""
        logger.debug("Saving database in: %s", path)
        with open(path, 'wb') as file:
            pickle.dump(self._dict, file, pickle.HIGHEST_PROTOCOL)

    def load(self, path):
        """Loads the database from a specific file."""
        with open(path, 'rb') as file:
            self._dict = pickle.load(file)
