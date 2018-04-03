Fonte: http://aprenda-python.blogspot.com.br/2016/10/por-que-properties-sao-melhores-que-getters-e-setters.html

# Por que properties são melhores que getters e setters

Quando vemos uma classe em Python escrita com métodos getters e setters, logo percebemos que o programador ainda não "pegou o jeito" de OOP em Python. Getters e setters são muito comuns em outras linguagens de programação porque os atributos normalmente são declarados com escopo privado. Ou seja, quem usa a classe não tem acesso aos atributos do objeto. Por isso criaram os métodos get_...() e set_...() para "violar" o encapsulamento dos membros privados.

Encapsulamento é uma coisa muito boa. Devemos usá-lo sempre que for útil. Aliás, talvez as classes sejam uma das melhores formas de colocarmos o encapsulamento em prática.

Python, claro, encoraja encapsulamento, mas de outra forma. Para começar, todos os membros de uma classe -- métodos e atributos -- têm visibilidade pública. Isso mesmo. Nada em um objeto fica escondido.

Definimos métodos e dados privados usando uma convenção: um underline no início do nome. Por exemplo, _codigo ao invés de codigo. Parece estranho a princípio, mas funciona muito bem. Afinal, se alguém quiser usar indevidamente um método ou um atributo da classe, estará sabotando o próprio programa. É o programa dele que vai dar errado!

Vou dar uma pausa aqui para justificar essa opção de projeto do Python. Não podemos esquecer o contexto de uso de uma classe. Uma classe nunca será usada por um usuário final diretamente. Ela sempre será usada por um programa, escrito por um programador. Quem usá-la, saberá o que está fazendo. Se não souber, vai ver os erros quando estiver testando o código e vai corrigir.

Quando vemos que tudo pode ser público em uma classe, passamos a gostar da simplicidade. De fato, quase sempre começamos a construir uma classe com todos os métodos e atributos sem o underline no início e só inserimos o underline ali quando fica claro o uso privado desse membro.

Isso pode nos levar a um problema: o cliente da classe pode ficar sabendo demais sobre a implementação e isso não é encapsulamento. Abordaremos a solução para esse problema nos exemplos abaixo.

Agora vamos começar a analisar um exemplo usando uma classe chamada Pessoa. Eu preciso de uma classe que guarde nome e sobrenome de uma pessoa. Mas também quero pegar o nome completo dela. Vamos aos códigos.

Na abordagem convencional, faríamos assim:

class Pessoa:
    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome
    def get_nome(self):
        return self._nome
    def set_nome(self, value):
        self._nome = value
    def get_sobrenome(self):
        return self._sobrenome
    def set_sobrenome(self, value):
        self._sobrenome = value
    def get_nome_completo(self):
        return "%s %s" % (self._nome, self._sobrenome)
Temos getters, setters e um método específico para pegar o nome completo: get_nome_completo().

Como em Python tudo é público, essa classe poderia ser simplificada assim:

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    def get_nome_completo(self):
        return "%s %s" % (self.nome, self.sobrenome)
Quando eu precisar pegar o nome da pessoa, simplesmente uso pessoa.nome. Quando eu quiser pegar o nome completo, uso pessoa.get_nome_completo().

Talvez não seja óbvio, mas um detalhe de implementação da classe Pessoa está exposto. E não é o atributo nome. É o método get_nome_completo(). Por que? Porque está claro que ele não é um atributo da classe. Ele começa com get_ e a chamada precisa ter os parênteses no final. Portanto, é um método getter.

Se eu quiser que esse detalhe fique realmente escondido, preciso usar uma property. Veja o exemplo abaixo:

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    @property
    def nome_completo(self):
        return "%s %s" % (self.nome, self.sobrenome)
Agora, para você pegar o nome completo, basta usar pessoa.nome_completo (sem o get_ inicial e sem os parênteses no final). Para quem usa a classe, usar pessoa.nome ou pessoa.nome_completo ficou igual. Sem olhar o código fonte da classe ninguém sabe como nome_completo foi implementado. Se é um atributo normal ou se é uma property. O decorator @property faz com que um método da classe possa ser acessado como se fosse um atributo. Isso é encapsulamento de verdade!

Mas eu posso querer mais detalhes na implementação da classe Pessoa. Por exemplo, o atributo nome precisa começar com uma letra maiúscula. Como fazer isso se estou acessando pessoa.nome diretamente? Simples. Basta criarmos outra property. Agora, para o nome:

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, value):
        self._nome = value.capitalize()
    @property
    def nome_completo(self):
        return "%s %s" % (self.nome, self._sobrenome)
Para usar essa classe, vamos trabalhar com um exemplo no REPL do Python:

>>> a = Pessoa(nome="felipe", sobrenome="da silva")
>>> a.nome
Felipe
>>> a.nome_completo
Felipe da silva
>>>
>>> a.nome = "roberto"
>>> a.nome
Roberto
>>> a.nome_completo
Roberto da silva
>>>
>>> a.nome_completo = "qualquer coisa"
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
can't set attribute
Note os detalhes dessa implementação:

O nome da pessoa está guardado no atributo _nome. E isso fica completamente encapsulado dentro da property nome.
Podemos usar nome como se fosse um atributo simples, tanto para pegar o valor, quanto para atribuir um valor.
O atributo sobrenome está sendo acessado diretamente, pois não temos nenhuma regra especial para ele.
O nome completo é uma property "read only".
Se não usássemos uma property, precisaríamos criar um método set_nome(), com o mesmo resultado. Mas havemos de concordar que a sintaxe da property é muito mais intuitiva para quem usa a classe, não é?

No futuro, se tivermos alguma particularidade para o atributo sobrenome, podemos mudar a implementação da classe sem afetar nenhum código externo, simplesmente usando outra property; dessa vez para o sobrenome.

As properties são muitos úteis quando utilizadas em lugar de métodos que retornam algum estado da classe. Por exemplo:

property is_active ao invés de um método is_active()
is_valid ao invés de is_valid()
nome_completo ao invés de get_nome_completo()
contatos ao invés de get_contatos()
Vejamos agora um caso real e bem simples onde eu uso properties para retornar estados da minha própria classe de exception.

>>> class MinhaException(Exception):
...     @property
...     def code(self):
...         return self.args[0]
...     @property
...     def message(self):
...         return self.args[1]
... 
>>> try:
...     raise MinhaException("003", "Campo obrigatório")
... except MinhaException as e:
...     print ("Erro %s (%s)" % (e.code, e.message))
... 
>>>
O exemplo acima cria duas properties, code e message, para abstrair a forma como esse atributos são guardados pela classe Exception. MinhaException simplifica o acesso a esses atributos ao mesmo tempo que aproveita a infraestrutura do Python, sem criar nada desnecessário.

Properties podem fazer mais do que isso. No exemplo abaixo temos dois usos poderosos de properties sem perder a simplicidade: a) "apagar" um atributo; b) uma property que é write only:

>>> class Campo:
...     def __init__(self, valor):
...         self.valor = valor
...         self._erros = []
... 
...     @property
...     def erros(self):
...         return self._erros
... 
...     @erros.deleter
...     def erros(self):
...         self._erros = []
... 
...     def _set_erro(self, valor):
...         self._erros.append(valor)
... 
...     erro = property(fset=_set_erro)
... 
>>> 
>>> c = Campo("nome")
>>> c.erro = "required"
>>> c.erro = "too short"
>>> c.erros
['required', 'too short']
>>> del c.erros
>>> c.erros
[]
>>> 
Percebemos que o comando del c.erros chama a property @erros.deleter para "apagar" o conteúdo de _erros. Na verdade, _erros é inicializado novamente e o objeto continua com o atributo funcionando. Muito melhor do que se usásssemos clean_erros(), não é?

Note que se tentarmos fazer c.erros = ["a", "b"], vamos ver uma mensagem dizendo que ele não pode ser ajustado. Esse comportamento é proposital. Novamente, não vamos expor os detalhes de implementação da classe. Então, usamos uma property que pode apenas receber valor, o atributo erro. Usamos c.erro para adicionar um erro à lista. Bem mais intuitivo do que algo como add_erro(). Nesse caso precisamos usar a função builtin property() porque esse atributo não pode ser lido.

Concluindo, as properties são melhores do que métodos getters e setters porque:

Podemos iniciar uma classe de uma forma bem direta, sem complexidade desnecessária, usando atributos simples;
Podemos acrescentar regras de armazenamento e/ou fornecimento de informações à medida do necessário, sem mexer na interface da classe;
A sintaxe de uso das properties é igual ao uso de atributos, sendo mais intuitiva para os clientes da classe.
Não escreva mais suas classes com sotaque de outras linguagens. Use properties ao invés de getters e setters.