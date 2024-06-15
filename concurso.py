N = input()
C = [input() for i in range(int(N[0]))]

K = int(N[2])
lista_ordenada = sorted(C)  
lista_decrescente = lista_ordenada[::-1]
nota_corte = lista_decrescente[K-1]
print(nota_corte)