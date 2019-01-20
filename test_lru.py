import unittest
from random import choice
import lru


class TestLRU(unittest.TestCase):

    def test_capacity_variable(self):
        lru_class = lru.LRUCache(10)
        self.assertEqual(10, lru_class.capacity)

    def test_caching(self):

        def some_func(x, y):
            return x + y

        lru_func = lru.LRUCache(20)(some_func)

        # Test whether caching working
        avaiable_variables = range(3)

        for i in range(1000):
            x, y = choice(avaiable_variables), choice(avaiable_variables)
            actual = lru_func(x, y)
            expected = some_func(x, y)
            self.assertEqual(actual, expected)

    def test_one_capacity(self):

        @lru.LRUCache(1)
        def some_func():
            nonlocal counter
            counter += 1
            return 15
        counter = 0

        for i in range(3):
            self.assertEqual(some_func(), 15)
        self.assertEqual(counter, 1)

    def test_zero_capacity(self):

        @lru.LRUCache(0)
        def some_func():
            nonlocal counter
            counter += 1
            return 15
        counter = 0

        for i in range(3):
            self.assertEqual(some_func(), 15)
        self.assertEqual(counter, 3)

    def test_miss_capacity(self):

        @lru.LRUCache()
        def some_func():
            nonlocal counter
            counter += 1
            return 15
        counter = 0

        for i in range(3):
            self.assertEqual(some_func(), 15)
        self.assertEqual(counter, 3)


if __name__ == '__main__':
    unittest.main()
