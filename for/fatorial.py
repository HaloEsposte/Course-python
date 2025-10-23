numero = int(input("Digite um número inteiro não negativo: "))
fatorial = 1

if numero >= 0:
    for i in range(1, numero + 1):
        fatorial *= i

    print(f"O fatorial de {numero} é: {fatorial}")

else:
    print("Numero negativo!")
    
print()


if numero < 0:
    print("O numero precisa ser positivo")

else:
    fatorial = 1
    
    for multiplicador in range(1, numero + 1):
        fatorial *= multiplicador
        
        print(f"{multiplicador}! =", end= " ")
        
        for i in range(1, multiplicador + 1):
            print(i,  end= " ")
            
            if i != multiplicador:
                
                print(" * ", end="")
                
        print("=", fatorial)