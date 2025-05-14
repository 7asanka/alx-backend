#!/usr/bin/env python3
"""MRU caching"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache implements Most Recently Used cache replacement.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Add item to cache. If full, discard the most recently used item.
        """
        if key is None or item is None:
            return

        if key in self.usage:
            self.usage.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru_key = self.usage.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve item and update it as most recently used.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage.remove(key)
        self.usage.append(key)

        return self.cache_data[key]
