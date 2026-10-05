#lista vazia
list = []
#receber 10 preços
for i in range(10):
     x =  float(input("digite o preço dos produtos:"))
    #adicionar a lista vazia 
     list.append(x)
# x percorre a lista e filtra
caros = [x for x in list if x > 100]
print(caros)   
