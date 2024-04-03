#!/usr/bin/python3
'''LRU Caching
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''Represents least recently used caching object
    inherited from BaseCaching class
    '''

    def __init__(self):
        '''Intilizes the oject
        '''
        super().__init__()
        self.q = []

    def put(self, key, item):
        '''Inserts an item in to the cach_date usding
        the LRU technique
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            del_q = self.q.pop(0)
            print('DISCARD: {}'.format(del_q))
            del self.cache_data[del_q]

        self.q.append(key)
        self.cache_data[key] = item

    def get(self, key):
        '''Returns the cache data which are linked to the key
        '''

        if key is None or key not in self.cache_data:
            return None

        self.q.remove(key)
        self.q.append(key)

        return self.cache_data[key]
