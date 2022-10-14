from random import randint
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAnoNascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod    #método de classe, n é referente a estancia mas sim a classe

    def por_ano_de_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento

        return cls(nome, idade)   

    @staticmethod #método estático n recebe a classe nem a instancia
    
    def gerar_id():
        rand = randint(10000,19999)
        return rand

p1 = Pessoa('Luiz', 35)
print(p1.idade)
p1.getAnoNascimento()

p2 = Pessoa.por_ano_de_nascimento('Pedro', 1987)
print(p2.idade)
#p1.getAnoNascimento()

print(Pessoa.gerar_id())
print(p1.gerar_id())