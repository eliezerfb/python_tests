"""
rodar: python -m unittest
"""
import unittest
from jokenpo import jokenpo_juiz


class TestJuizJokenpo(unittest.TestCase):
    def test_jogada_invalida(self):
        self.assertEqual(jokenpo_juiz('xpto', 'optx'), 'jogada inválida')

    def test_empate_pedra(self):
        self.assertEqual(jokenpo_juiz('pedra', 'pedra'), 'empate')

    def test_empate_papel(self):
        self.assertEqual(jokenpo_juiz('papel', 'papel'), 'empate')

    def test_empate_tesoura(self):
        self.assertEqual(jokenpo_juiz('tesoura', 'tesoura'), 'empate')

    def test_jogador1_ganha_pedra(self):
        self.assertEqual(jokenpo_juiz('pedra', 'tesoura'), 'jogador1')

    def test_jogador1_ganha_papel(self):
        self.assertEqual(jokenpo_juiz('papel', 'pedra'), 'jogador1')

    def test_jogador1_ganha_tesoura(self):
        self.assertEqual(jokenpo_juiz('tesoura', 'papel'), 'jogador1')

    def test_jogador2_ganha_pedra(self):
        self.assertEqual(jokenpo_juiz('tesoura', 'pedra'), 'jogador2')

    def test_jogador2_ganha_papel(self):
        self.assertEqual(jokenpo_juiz('pedra', 'papel'), 'jogador2')

    def test_jogador2_ganha_tesoura(self):
        self.assertEqual(jokenpo_juiz('papel', 'tesoura'), 'jogador2')
