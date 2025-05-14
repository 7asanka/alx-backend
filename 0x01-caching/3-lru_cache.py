#!/usr/bin/env python3
"""LRU caching"""


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class that implements Least Recently Used cache replacement.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage = []

    def put(self, key, item):
        """
        Add item to cache. If cache is full, remove least recently used key.
        """
        if key is None or item is None:
            return

        if key in self.usage:
            self.usage.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.usage.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve item and update usage order.
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage.remove(key)
        self.usage.append(key)

        return self.cache_data[key]
