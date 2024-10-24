#!/usr/bin/env python3
from exercise import Cache
import unittest
from unittest.mock import patch

class TestCache(unittest.TestCase):
    """
    Unit tests for the Cache class methods.
    """

    @patch('redis.Redis')
    def setUp(self, MockRedis):
        """
        Set up a mocked Redis instance and initialize Cache.
        """
        self.mock_redis = MockRedis.return_value
        self.cache = Cache()

    def test_store(self):
        """
        Test that store method generates a unique key and stores the data.
        """
        key = self.cache.store("test_data")
        self.assertIsInstance(key, str)
        self.mock_redis.set.assert_called_once_with(key, "test_data")

    def test_get_with_conversion(self):
        """
        Test that get method retrieves and applies conversion function.
        """
        key = "test_key"
        self.mock_redis.get.return_value = b"123"
        result = self.cache.get(key, fn=int)
        self.assertEqual(result, 123)
        self.mock_redis.get.assert_called_once_with(key)

    def test_get_without_conversion(self):
        """
        Test that get method retrieves data without conversion.
        """
        key = "test_key"
        self.mock_redis.get.return_value = b"test_data"
        result = self.cache.get(key)
        self.assertEqual(result, b"test_data")
        self.mock_redis.get.assert_called_once_with(key)

    def test_get_str(self):
        """
        Test that get_str retrieves data and decodes it as a string.
        """
        key = "test_key"
        self.mock_redis.get.return_value = b"test_data"
        result = self.cache.get_str(key)
        self.assertEqual(result, "test_data")

    def test_get_int(self):
        """
        Test that get_int retrieves data and converts it to an integer.
        """
        key = "test_key"
        self.mock_redis.get.return_value = b"123"
        result = self.cache.get_int(key)
        self.assertEqual(result, 123)

    def test_get_non_existent_key(self):
        """
        Test that get returns None for non-existent keys.
        """
        key = "non_existent_key"
        self.mock_redis.get.return_value = None
        result = self.cache.get(key)
        self.assertIsNone(result)

    def test_redis_flush_on_init(self):
        """
        Test that Redis database is flushed upon Cache initialization.
        """
        self.mock_redis.flushdb.assert_called_once()

if __name__ == '__main__':
    unittest.main()
