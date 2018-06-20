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


def calcula_troco(valor, recebido):
    disponiveis = [0.01, 0.05, 0.10, 0.50, 1, 5, 10, 50, 100]
    diferenca = round(recebido - valor, 2)
    troco = []
    while diferenca > 0:
        disponiveis = list(filter(lambda x: x <= diferenca, disponiveis))
        diferenca = round(diferenca - disponiveis[-1], 2)
        troco.append(disponiveis[-1])

    return troco


if __name__ == '__main__':
    unittest.main()
