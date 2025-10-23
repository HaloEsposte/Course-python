altura = 3
largura = 5

for i in range(altura):
    for j in range(largura):
         print("*", end=" ")
    
    print()
    
    
altura2 = 5

for i in range(altura2):
    espacos = altura2 - i -1
    estrela = 2 * i + 1
    print(" " * espacos + "*" * estrela) 
