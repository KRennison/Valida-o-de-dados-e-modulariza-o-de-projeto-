import random
import utilidades

numeros = []

for i in range(10):
    numeros.append(random.randint(1, 100))

print("Numeros:", numeros)
print("Maior numero:", utilidades.maior_iterativo(numeros))
print("Maior recursivo:", utilidades.maior_recursivo(numeros))￼Enter
