list = [] #criar lista vazia pra receber valores

for i in range(5):#repetição para coletar os dados
    x = float(input("Digite a temperatura:"))
    list.append(x)#adiciona a lista cada input digitado

print("Temperaturas:", list) #mostra a lista

print("Primeiro dia:", list[0]) #mostra o primeiro valor da lista

print("Ultimo dia:", list[-1]) #mostra o ultimo valor da lista
