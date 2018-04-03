class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.__sobrenome = sobrenome

    @property
    def nome(self):
        return self.__nome

    # @property
    # def sobrenome(self):
    #    return self.__sobrenome

    @nome.setter
    def nome(self, value):
        self.__nome = value.capitalize()

    # @sobrenome.setter
    # def sobrenome(self, value):
    #    self.__sobrenome = value.capitalize()

    @property
    def nome_completo(self):
        return "%s %s" % (self.nome, self.__sobrenome)


if __name__ == "__main__":
    pessoa = Pessoa(nome="eliezer", sobrenome='bourchardt')

    print(pessoa.nome)
    #print(pessoa.sobrenome)
    print(pessoa.nome_completo)
