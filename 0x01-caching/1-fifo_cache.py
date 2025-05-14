#!/usr/bin/env python3
"""FIFO caching"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class that implements a FIFO caching strategy.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add item to cache using FIFO replacement policy.
        Discard oldest item if over capacity.
        """
        if key is None or item is None:
            return

        if (key not in self.cache_data
                and len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        if key not in self.order:
            self.order.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve item from cache by key.
        Return None if not found.
        """
        return self.cache_data.get(key, None)
