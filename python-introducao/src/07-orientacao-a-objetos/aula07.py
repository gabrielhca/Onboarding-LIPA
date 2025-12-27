""" Aula 07 - Relacionamento entre classes """


class Endereco:
    def __init__(self, cep, numero):
        self.cep = cep
        self.numero = numero

    def __str__(self):
        return f'Endereco(cep={self.cep}, numero={self.numero})'


class Telefone:
    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'Telefone(ddd={self.ddd}), numero={self.numero}'


class Pessoa:
    def __init__(self, nome, cpf, telefone, endereco):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.enderecos = [endereco]

    def add_endereco(self, endereco):
        self.enderecos.append(endereco)

    def print_enderecos(self):
        print(self.nome)
        for endereco in self.enderecos:
            print(endereco)

    def __str__(self):
        return f'Pessoa(nome={self.nome}, cpf={self.cpf}, telefone={self.telefone}, enderecos={self.enderecos})'


telefone = Telefone("11", "99999-9999")
pessoa1 = Pessoa("Joao", "100100100-10", telefone, Endereco("01001000", 101))
pessoa1.add_endereco(Endereco("01001000", 205))
pessoa1.add_endereco(Endereco("01001000", 107))


pessoa2 = Pessoa("Maria", "200200200-20", telefone, Endereco("01001000", 109))
pessoa2.add_endereco(Endereco("01001000", 120))

pessoa3 = Pessoa("Ana", "300300300-30", telefone, Endereco("01001000", 130))


print(pessoa1)
print(pessoa2)
print(pessoa1.nome, pessoa1.cpf, pessoa1.telefone)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)


pessoa1.print_enderecos()
pessoa2.print_enderecos()
pessoa3.print_enderecos()