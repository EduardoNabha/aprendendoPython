from turtle import st


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    #Getter
    @property
    def preco(self):
        return self._preco

    #Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        
        self._preco = valor


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()







p1 = Produto('CAMISETA', 50)
p1.desconto(10)
print(p1.preco)
print(p1.nome)
p2 = Produto('Caneca', 15)
p2.desconto(10)
print(p2.preco)

