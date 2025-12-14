# SEGUNDO BLOCO DO CURSO-UDEMY
#       Armazenamentos

# Comparação de valores é dado por == 

# Dando valores as variaveis 
D = 0
print("valor de D:", D)
A = 2 
print("Valor de A:", A)
B = 3
print("Valor de B:", B)
C = 5
print("Valor de C:", C)

# alterando o valor de C
C = C + 1 
print("Valor de C:", C)

# Alterando o valor de D com as variaveis 
D = A + C
print("Valor de D:", D)

# Tipos de dados 
#Texto : str
#Numericos : int, float, complex
#Sequencia: list, tuple, range
#Mapeamento: dict
#Conjuntos: set, frozenset
#Booleano: bool
#Binários : bytes, bytearray, memoryview

# definir os tipos de dados 

x = "hello world" #str
x = 20 #int
x = 20.5 #float
x = 1j #complex
x = ["apple","banana","cherry"] # list
x = ("apple", "banana","cherry") # tuple
x = range(6) #range
x = {"name" : "jhon","age" : 36} #dict
x = {"apple","banana","cherry"} #set
x = frozenset ({"apple","banana","cherry"}) # frozenset
x = True #bool
x = b"Hello" #bytes
x = bytearray(5) # bytearray
x = memoryview(bytes(5)) #memoryview

# criando um dado de 6 lados
import random

dado = random.randrange ( 1, 7)
print(dado)
print("\n") # funciona como uma quebra de linha
dado2 = random.randrange (1,21)
print(dado2)
print("\n")

for x in "Elivan":
    print(x + "->")

h = "Homenzinho torto com casa torta"

a = len(h)
print(a)

b = "torto" in h
print (b)
print("ereto" in h)

if "torta" in h:
    print("Verdadeira afirmação")
if "fogo" not in h:
    print("Afirmação falsa")

if b:
    print("Verdadeira afirmação")





