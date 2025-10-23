'''
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)
'''



#Exercicio: FUnção para calcular Estatísticas de Números

def estatistica(*args):
    
    return sum(args) / len(args), max(args), min(args)


numero = list(map(float, input("digite uma sequência de npumeros separdos por espaços: ").split()))

media, maior, menor = estatistica(*numero)

print(f"Média: {media}")
print(f"O maior Número: {maior}")
print(f"O menor Número: {menor}")