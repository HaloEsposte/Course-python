'''
posicaoLetra = "Python"
print(posicaoLetra[0])
print(posicaoLetra[1])
print(posicaoLetra[2])
print(posicaoLetra[3])
print(posicaoLetra[4])
'''
#########################################
'''
# Slice
frase = "Olá, mundo!"

# Obtendo uma parte da string usando slice
parte = frase[4:8]
print(parte) #Saída: Olá

# Obtendo os primeiros 5 caracteres da string
primeiros = frase[:5]
print(primeiros) # Saida: Olá,_

#Obtendo os últimos 6 caracteres da string
ultimos = frase [-6:]
print(ultimos) #Saida: mundo!

'''
#verificar se a palavra python está na frase
frase = "O módulo de python é muito legal"

#if - se
if "python" in frase:
    print("Sim, a palavra python está presente na frase.\n")
    
###############################################

#strip - Usamos para remover espaços em brsnco do inicio e do final da frase
frase = "          O módulo de python é muito legal        "
print(frase.strip())

#split, join e strip são metodos muito uteis da str

#split
frase = "Olá, como vai você?"
palavras = frase.split() # Dividindo a frase em palavras usando o espaço em branco como separador
print(palavras)

#método join() junta os elementos de uma lista em uma unica string, utilizando um separado esceficado entre cada elemento
palavras = ['Olá,', 'como', 'vai', 'você?']
frase = '_'.join(palavras) # Juntamos as palavras com um espaço em branco entre elas
print(frase)

#método strip
texto = "*********Olá!******"
texto_strip = texto.strip('*') #removendo um caractere especifico do inicio e do fim
print(texto_strip)

texto = "     Olá!     "
texto_strip = texto.strip() # removendo espaço em brando do inicio e do fim
print(texto_strip)