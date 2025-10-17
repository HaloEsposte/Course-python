import random

print(random.randrange(1, 100))

#Gera numeros de pont flutuante aleatórios entre 0 e 1
print(random.random())

#Gera um numero inteiro aleátorio entre dois valores (inclusive)
print(random.randrange(10, 20)) # Gera um numero entre 10 e 20, inclusive

# Escolher aleatóriamente elementos de uma lista
frutas = ["maça", "banana", "abacaxi"]
print(random.choice(frutas)) # Escolher uma fruta na lista aleatóriamente

# Embaralhar aleatóriamente uma lista:
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros) # A lista 'numeros' agora está embaralhada

# Gera um numero de ponto flutuante aleatório em um intervalo especifico
print(random.uniform(5.5, 9.5)) # Gera um número de ponto flutuante entre 5.5 e 9.5
