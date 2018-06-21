"""http://dojopuzzles.com/problemas/exibe/jokenpo/
Jokenpo é uma brincadeira japonesa, onde dois jogadores escolhem um dentre
três possíveis itens: Pedra, Papel ou Tesoura.

O objetivo é fazer um juiz de Jokenpo que dada a jogada dos dois jogadores
informa o resultado da partida.

As regras são as seguintes:

* Pedra empata com Pedra e ganha de Tesoura
* Tesoura empata com Tesoura e ganha de Papel
* Papel empata com Papel e ganha de Pedra

         pedra   papel   tesoura
pedra      0       2       1
papel      1       0       2
tesoura    2       1       0

"""


def jokenpo_juiz(jogador1, jogador2):
    opcao = ('pedra', 'papel', 'tesoura')
    if (jogador1 not in opcao) or (jogador2 not in opcao):
        return 'jogada inválida'

    regra = ((0, 2, 1),
             (1, 0, 2),
             (2, 1, 0))

    final = regra[opcao.index(jogador1)][opcao.index(jogador2)]
    return ('empate', 'jogador1', 'jogador2')[final]
