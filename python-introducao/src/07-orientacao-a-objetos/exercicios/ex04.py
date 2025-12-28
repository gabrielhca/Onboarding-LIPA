""" Ex04 - Lista de participações no Projeto """

from ex01 import Aluno
from ex03 import Participacao


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel
        self.participacoes = []

    def add_participacao(self, participacao):
        """Adiciona uma participação ao projeto."""
        self.participacoes.append(participacao)

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._titulo = value

    @property
    def responsavel(self):
        return self._responsavel

    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._responsavel = value

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, value):
        if not value or (isinstance(value, str) and not value.isdigit()):
            raise ValueError("Parametro numerico obrigatorio")
        self._codigo = int(value)

    @classmethod
    def contruir_com_string(cls, linha):
        partes = linha.split(",")
        return cls(codigo=partes[0].strip(), titulo=partes[1].strip(), responsavel=partes[2].strip())

    def __eq__(self, value):
        if isinstance(value, Projeto):
            return self.codigo == value.codigo
        return False

    def __hash__(self):
        return hash(self.codigo)

    def __repr__(self):
        return f"Projeto({self.codigo}, {self.titulo}, {self.responsavel})"


# Exemplo de uso

projeto = Projeto(10, "Desenvolvimento de Software", "Gabriel Amorim")

aluno1 = Aluno(1, "Ana Silva", "ana.silva@example.com")
aluno2 = Aluno(2, "Pedro Gomes", "pedro.gomes@example.com")

participacao1 = Participacao(100, "2024-01-15", "2024-06-15", aluno1, projeto)
participacao2 = Participacao(101, "2024-02-01", "2024-07-01", aluno2, projeto)

projeto.add_participacao(participacao1)
projeto.add_participacao(participacao2)

print(projeto)
for participacao in projeto.participacoes:
    print(participacao)
print(f"Total de participações no projeto: {len(projeto.participacoes)}")
