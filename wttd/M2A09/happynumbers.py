"""Os números felizes são definidos pelo seguinte procedimento. Começando com
qualquer número inteiro positivo, o número é substituído pela soma dos
quadrados dos seus dígitos, e repetir o processo até que o número seja igual
a 1 ou até que ele entre num ciclo infinito que não inclui um ou seja a soma
dos quadrados dos algarismos do quadrado de um número positivo inicial.
Os números no fim do processo de extremidade com 1, são conhecidos como
números feliz, mas aqueles que não terminam com um 1 são números
chamados infelizes.
"""


def happy(number):
    next_ = sum(int(char) ** 2 for char in str(number))
    return number in (1, 7) if number < 10 else happy(next_)


assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 8, 9))
