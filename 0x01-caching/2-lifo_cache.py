#!/usr/bin/env python3
"""FIFO cache"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class that implements a LIFO caching strategy.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.stack = []  # used to track insertion order

    def put(self, key, item):
        """
        Add item to cache using LIFO replacement policy.
        Discard most recent item if over capacity.
        """
        if key is None or item is None:
            return

        if (key not in self.cache_data
                and len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            last_key = self.stack.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

        # Remove the key if it's already in stack to prevent duplicates
        if key in self.stack:
            self.stack.remove(key)

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve item from cache by key.
        Return None if not found.
        """
        return self.cache_data.get(key, None)
