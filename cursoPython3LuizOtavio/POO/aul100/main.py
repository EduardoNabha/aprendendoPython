from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

'''
print(p1.nome)
p1.comer('Maça')
p1.falar('POO')
p1.pararDeComer()
p1.falar('POO')
p1.comer('alimento')
p1.pararDeFalar()
p1.falar('assunto')
'''
#p1.falar('POO')
#p2.falar('Filmes')
#p1.comer('Churrasco')
print(p1.anoAtual, p2.anoAtual)
print(Pessoa.anoAtual)

print(p1.getAnoNascimento())

