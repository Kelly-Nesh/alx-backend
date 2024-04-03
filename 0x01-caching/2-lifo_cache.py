#!/usr/bin/python3
'''LIFO caching Module
'''
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    '''Represents an object which Inherited from
    BaseCaching and is a caching system
    '''

    def __init__(self):
        '''Initilize the object'''
        super().__init__()
        self.q = []

    def put(self, key, item):
        '''Insert cache data using the LIFO method
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            del_q = self.q.pop()
            print('DISCARD: {}'.format(del_q))
            del self.cache_data[del_q]

        self.q.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key."""
        return self.cache_data.get(key)
