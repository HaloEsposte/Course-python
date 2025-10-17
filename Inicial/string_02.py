#Utilizando Formated String

#Utilizando Formated Strings
nome = "Alice"
idade = 25
altura = 1.65

#Criando uma mesnagem formatada usando f-string
mensagem = f"Olá, meu nome é {nome}. Tenho {idade} anos e minha altura é {altura:.2f} metros\n"
print(mensagem)


# Métodos para istrings
texto = "Olá, mundo!"

# Método upper() - Converte a string para maiúsculas
texto_upper = texto.upper()
print(texto_upper)

# Método lower() - Converte a string para minúscula
texto_lower = texto.lower()
print(texto_lower)

# Método capitalize() - Capitaliza a primeira letra da string
# A primeira letra "o" é convertida em maiuscula
texto_capitalize = texto.capitalize()
print(texto_capitalize) 

# Método count() - Conta o número de ocorrências de um determinado caractere ou substring na str
ocorrencias = texto.count("o")
print(ocorrencias) # Output: 1

# Método replace() - Substitui todas as ocorrências de uma substring por outra substring
texto_substituido = texto.replace("mundo", "amigo")
print(texto_substituido)