import collections


class LRUCache:

    def __init__(self, capacity=None):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def __call__(self, func):

        def wrapper(*args):
            if not self.capacity:
                return func(*args)
            value = self.get(args)
            if not value:
                value = func(*args)
                self.set(args, value)
            return value
        return wrapper

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return False

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
