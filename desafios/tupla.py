
#cria duas listas vazias
muda = []
nomes = []

#define a quantidade de alunos que sera usado como range
quantidade = int(input("digite a quantidade de alunos: "))

for i in range(quantidade):
    #pega nome dos alunos
    nome = input("Digite o nome do aluno:")
    nomes.append(nomes)

#pega as notas dos alunos
    notas = float(input("Qual a nota do aluno:"))
    muda.append(notas)
   
#transforma a lista em uma tupla    
tuple(muda)

print(muda)
print(max(muda)) # da o maior numero da tupla
print(min(muda))  # da o menor numero da tupla  
print(sum(muda)/quantidade) # calcula a media 