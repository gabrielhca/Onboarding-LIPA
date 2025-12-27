""" Aula 03 - Metodos de classe """


class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @classmethod  # metodo de classe e não de instância
    def from_list(cls, lista):
        return cls(lista[0], lista[1])

    @classmethod
    def from_string(cls, rep_retangulo):
        base, altura = rep_retangulo.split(sep=",")
        return cls(float(base), float(altura))

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# intanciando um objeto do tipo Retangulo
retangulo1 = Retangulo(10.0, 5.0)
retangulo2 = Retangulo(6.0, 3.0)
retangulo3 = Retangulo.from_list([20.0, 3.5])
retangulo3 = Retangulo.from_string("55.4, 13.5")

print(retangulo3.base, retangulo3.altura,
      retangulo3.calcular_area(), retangulo3.calcular_perimetro())
