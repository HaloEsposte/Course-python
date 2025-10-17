#Exercicio imprimir lista de compras

itens_compra = ["maça", "banana", "cenoura", "leite"]

for iten in itens_compra:
    print(f"Eu preciso comprar {iten}")
print()    
    
#Exercicio: Estrela Descendente

for estrela in range(5, 0, -1):
    print("*" * estrela)
print()

#Exercicio: Palavra com mais de 4 letras

palavras = ["casa", "carro", "sol", "árvore"]

for palavra in palavras:
    if len(palavra) > 4:
        print(palavra)