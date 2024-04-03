#!/usr/bin/env python3
""" Base Caching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BaseCache:
      - caching system without limit
    """

    def __init__(self):
        """init method. Calls superclass init"""
        super().__init__()

    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        the item value for the key key."""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        return self.cache_data.get(key, None)
