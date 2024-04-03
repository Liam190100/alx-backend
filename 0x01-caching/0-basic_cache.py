#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Object that allows storing a dictionary.
    """
    def put(self, key, item):
        """item add at the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """item by key.
        """
        return self.cache_data.get(key, None)
