from datetime import datetime

class Pessoa:

    anoAtual = int(datetime.strftime(datetime.now(), '%Y'))
    #^ variável da classe
    
    
    #método = é  a função de uma classe
    #__init__ = método construtor
    def __init__(self, nome, idade, comendo = False, falando = False):
        self.nome = nome #o self disponibiliza a variavel pra trodos os outros métodos dentro da classe
        self.idade = idade
        self.comendo = comendo
        self.falando = falando 

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo!')
            return

        if self.falando:
            print(f'{self.nome} já está falando!')
            return
        
        print(f'{self.nome} está falando sobre {assunto}!')
        self.falando = True

    def pararDeFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return
        print(f'{self.nome} parou de falar!')
        self.falando = False

    def comer(self, alimento):
        if self.comendo == True:
            print(f'{self.nome} já está comendo!')
            return

        if self.falando:
            print(f'{self.nome} não pode comer falando!')
            return

        print(f'{self.nome} está comendo {alimento}!')
        self.comendo = True

     


    def pararDeComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return

        print(f'{self.nome} parou de comer!')
        self.comendo = False




    def getAnoNascimento(self):
        return self.anoAtual - self.idade
