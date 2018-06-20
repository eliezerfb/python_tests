"""http://dojopuzzles.com/problemas/exibe/troco/
Funcionários de empresas comerciais que trabalham como caixa tem uma grande
responsabilidade em suas mãos. A maior parte do tempo de seu expediente de
trabalho é gasto recebendo valores de clientes e, em alguns casos, fornecendo
troco.

Seu desafio é fazer um programa que leia o valor total a ser pago e o valor
efetivamente pago, informando o menor número de cédulas e moedas que devem
ser fornecidas como troco.

Deve-se considerar que há:

cédulas de R$100,00, R$50,00, R$10,00, R$5,00 e R$1,00;
moedas de R$0,50, R$0,10, R$0,05 e R$0,01.
"""

from decimal import *
import unittest



def calcula_troco(valor, recebido):
    getcontext().prec = 3
    disponiveis = [0.01, 0.05, 0.10, 0.50, 1, 5, 10, 50, 100]
    diferenca = float(Decimal(recebido) - Decimal(valor))
    troco = []
    while diferenca > 0:
        disponiveis = list(filter(lambda x: x <= diferenca, disponiveis))
        diferenca = diferenca - disponiveis[-1]
        troco.append(disponiveis[-1])

    return troco


class TestaTroco(unittest.TestCase):

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

#    def test_troco(self):
#        self.assertEqual(calcula_troco(33.34, 200), [0.01, 0.05, 0.10, 0.50, 1, 5, 10, 50, 100])


if __name__ == '__main__':
    unittest.main()
