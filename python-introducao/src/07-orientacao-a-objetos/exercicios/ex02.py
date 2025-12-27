""" Ex 02 - Classe Projeto """


class Projeto:
    def __init__(self, codigo, titulo, responsavel):
        self.codigo = codigo
        self.titulo = titulo
        self.responsavel = responsavel

    # getter
    @property
    def titulo(self):
        return self._titulo

    @property
    def responsavel(self):
        return self._responsavel

    @property
    def codigo(self):
        return self._codigo

    # setter
    @titulo.setter
    def titulo(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._titulo = value

    @responsavel.setter
    def responsavel(self, value):
        if not value:
            raise ValueError("Parametro obrigatorio")
        self._responsavel = value

    @codigo.setter
    def codigo(self, value):
        if not value or isinstance(value, str) and not value.isdigit():
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


entrada = "1, Laboratório de Desenvolvimento de Software, Pedro Gomes"
projeto_teste = Projeto.contruir_com_string(entrada)
print(projeto_teste)
print(type(projeto_teste.codigo))

projeto1 = Projeto("5", "Gabriel Henrique", "g@h.com")
projeto2 = Projeto(5, "Gabriel Amorim", "g@a.com")

conjunto_de_projetos = {projeto1, projeto2}
print(f"Projeto1 == Projeto2? {projeto1 == projeto2}")
print(f"Tamanho do conjunto: {len(conjunto_de_projetos)}")

print(type(projeto1.codigo))
print(type(projeto2.codigo))
