"""Em alguns lugares é comum lembrar um número do telefone associando seus
dígitos a letras. Dessa maneira a expressão MY LOVE significa 69 5683.
Claro que existem alguns problemas, uma vez que alguns números de telefone
não formam uma palavra ou uma frase e os dígitos 1 e 0 não estão associados
a nenhuma letra.

Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente
baseado na tabela abaixo. Uma expressão é composta por letras maiúsculas
(A-Z), hifens (-) e os números 1 e 0.

Letras  ->  Número
ABC, 2
DEF, 3
GHI, 4
JKL, 5
MNO, 6
PQRS   ->  7
TUV, 8
WXYZ   ->  9
Entrada

A entrada consiste de um conjunto de expressões.
Cada expressão está sozinha em uma linha e possui C caracteres,
onde 1 ≤ C ≤ 30. A entrada é terminada por fim de arquivo (EOF).

Saída

Para cada expressão você deve imprimir o número de telefone correspondente.

Exemplo de entrada,

1-HOME-SWEET-HOME
MY-MISERABLE-JOB

Saída correspondente,

1-4663-79338-4663
69-647372253-562

Curiosidades

A frase "The quick brown fox jumps over the lazy dog" é um pangrama
(frase com sentido em que são usadas todas as letras do alfabeto de
determinada língua) da língua inglesa.

Já em português,

"Um pequeno jabuti xereta viu dez cegonhas felizes"

"""

def get_number_from_word(word):
    conversion = (('ABC', '2'), ('DEF', '3'), ('GHI', '4'), ('JKL', '5'),
                  ('MNO', '6'), ('PQRS', '7'), ('TUV', '8'), ('WXYZ', '9'))
    number = [c[1] for c in conversion if word in c[0]]
    return number[0] if len(number) == 1 else word


def find_phone(words):
    words = words.upper().replace(' ', '-')
    return ''.join([get_number_from_word(w) for w in words])


assert get_number_from_word('-') == '-'
assert get_number_from_word('x') == 'x'
assert get_number_from_word('E') == '3'
assert find_phone('1-HOME-SWEET-HOME') == '1-4663-79338-4663'
assert find_phone('MY-MISERABLE-JOB') == '69-647372253-562'
assert find_phone('1-800-COMPUTE') == '1-800-2667883'

frase = 'The quick brown fox jumps over the lazy dog'
print(find_phone(frase))

frase = 'Um pequeno jabuti xereta viu dez cegonhas felizes'
print(find_phone(frase))
