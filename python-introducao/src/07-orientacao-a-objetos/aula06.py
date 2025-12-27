""" Aula 06 - __eq__ e __hash__"""

nome1 = "Joao"
nome2 = "Joao"
print(nome1 == nome2)


class Pessoa:
    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def __eq__(self, value):
        if isinstance(value, Pessoa):
            return self.cpf == value.cpf
        return False

    # numero usado em coleções para identificar o objeto
    def __hash__(self):
        return hash(self.cpf)

    def __repr__(self):
        return f"Pessoa({self.cpf},{self.nome})"


pessoa1 = Pessoa("100100100-10", "Joao")
pessoa2 = Pessoa("100100100-10", "Joao")
pessoa3 = Pessoa("100100100-11", "Maria")
print(pessoa1 == pessoa2)

pessoas = {pessoa1, pessoa2, pessoa3}
print(pessoas)

pessoas_lista = [pessoa1, pessoa2, pessoa3]
print(pessoas_lista)
print(pessoas_lista.count(pessoa1))
