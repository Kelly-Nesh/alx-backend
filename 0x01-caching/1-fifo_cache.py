#!/usr/bin/env python3
""" FIFO module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ fifo cache:
      - fifo caching system without limit
    """

    def __init__(self):
        """init method. Calls superclass init"""
        super().__init__()
        self.q = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data
        the item value for the key key."""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            del_q = self.q.pop(0)
            print('DISCARD: {}'.format(del_q))
            del self.cache_data[del_q]

        self.q.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        return self.cache_data.get(key)
