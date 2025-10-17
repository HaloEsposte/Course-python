n = int(input("Digite um úmero inteiro positivo: "))
soma = 0

for i in range(1,n+1):
    quadrado = pow(i, 2)
    soma += quadrado
    print(f"Quadrado de {i}: {quadrado}")
    
print(f"A soma dos quadrados dos numeros de 1 até {n} é: {soma}")
