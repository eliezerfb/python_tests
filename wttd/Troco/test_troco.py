"""
rodar: python -m unittest
"""
import unittest
from troco import calcula_troco


class Calcula_TrocoTest(unittest.TestCase):
    def test_valor_igual(self):
        self.assertEqual(calcula_troco(100, 100), [])

    def test_valor_menor(self):
        self.assertEqual(calcula_troco(100, 99), [])

    def test_troco_1_centavo(self):
        self.assertEqual(calcula_troco(0.1, 0.2), [0.1])

    def test_troco_10_centavos(self):
        self.assertEqual(calcula_troco(0.9, 1), [0.1])

    def test_troco_2_centavos(self):
        self.assertEqual(calcula_troco(0.03, 0.05), [0.01, 0.01])

    def test_troco(self):
        # 200 - 33.34 = 166,66 passa por todos valores para fechar o troco.
        self.assertEqual(calcula_troco(33.34, 200), [100, 50, 10, 5, 1, 0.5,
                                                     0.1, 0.05, 0.01])
