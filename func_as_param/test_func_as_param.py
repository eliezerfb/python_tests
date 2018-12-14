"""
How run: python -m unittest
"""
import unittest


def converter(value, cast):
    return cast(value)


class TestCast(unittest.TestCase):
    def test_int(self):
        conv = converter('1', lambda x: int(x))
        self.assertEqual(conv, 1)

    def test_float(self):
        conv = converter('1', lambda x: float(x))
        self.assertEqual(conv, 1.0)

    def test_str(self):
        conv = converter(1, lambda x: str(x))
        self.assertEqual(conv, '1')
