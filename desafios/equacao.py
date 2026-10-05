pt = int(input("Digite o primeiro termo:"))

r = int(input("Digite a razão: "))

lista =[pt]

for i in range(1,10): # começa a contagem com i partindo de 1
    x = lista[i - 1] + r  # pega o indice de i e subtrai por 1 pra obter o numero na lista e adiciona r
    lista.append(x)# atualiza na lista

print(lista)    