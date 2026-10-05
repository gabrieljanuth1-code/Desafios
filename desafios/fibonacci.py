n = int (input("Quantos termos:"))

fibonacci = [0, 1]
for i in range(2, n):
    seq = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(seq)
print("Sequencia fibonacci:", fibonacci[:n])    