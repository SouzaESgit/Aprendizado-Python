# PRIMEIRO BLOCO DO CURSO-UDEMY

print(2+2)
print ("Hello, World!")

if 5> 2: 
    print ("Cinco é maior que dois")
    print("Fim do bloco do if")
# os print superiores fazem parte do bloco porque estão no mesmo afastamento
print("Fora do bloco if")

if 5 > 20:
    print("Cinco é maior que vinte")
#não é executado porque a afirmação é falsa
print ("não faz parte do bloco if")

"""Isto é uma string, usada como bloco de comentário"""

x = 5
y = "Elian"
z = 4 

print (x)
print (y)

print(f"Seu valor é: {x+z}")

#tipo de representações 
# 3   "3"    3.0

a = str(3) # a será 3
b = int(3)# b sera 3
c = float(3)# c será 3.0

print(type(a))

# a = Laranja
# b = Banana
# c = Cereja 

a, b, c, = "laranja", "banana", "cereja"

print (a)
print (b)
print (c)

def func():
    print("python é trabalhoso também")
func()
func()
func()

raio = 15

import math

def circulo():
    ferencia = (raio**2)*math.pi
    return ferencia
print (circulo())

#exercicio para compreender variaveis locais e globais dentro do python 

x = "incrível"

def myfunc():
    x = "Surreal"
    y = "Fantastico"
    global z 
    z = "Bem vindo ao curso"
    print ("Python é " + x + " e " + y)
    print (z)

myfunc()

print ("=================")
print ("Você é " + x)
print (z)

# Ao analisar a função (def) o objetivo é entender que: A variável (X = surreal)
# não vai ser lida como "surreal", mas sim como "incrivel", porque o x = surreal está 
# em uma definição local de uma def (função).
# diferente da z = "bem vindo ao curso", pois ela está configurada como global
# para ele ler o X local basta por anteriormente 
# -<global x>-

