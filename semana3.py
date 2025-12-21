#num = input("Digite um numero: ")

#triplo = int(num) * 3 

print()
#print("O triplo de", num, "é",triplo)

import os

os.system("cls") or None

#num1 = input("Digite o primeiro numero: ")
#num1 = int(num1) 

#num2 = input("Digite o segundo numero: ")
#num2 = int(num2)

#mult1 = num1 * num2 
print()
#print("A multiplicação de ", num1,"por",num2, "é", mult1)

x = 5 
print(x > 3 and x < 10)

print(x > 3 or x < 4)

print(not(x > 3 or x < 4))

print()

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x 

print(x is z)
print(x is y)
print(x == y)
print(x is not z)
print(x is not y)
print(x != y)


lista = ["maça","banana","cereja","maça", "cereja"]

print(lista)
print(len(lista))

# tuplas são parecidas as listas, porém são imutáveis e ficam entre ( )

tupla = ("Gabriel","Danny","Arthur", "Danny")
print(tupla)
print(len(tupla))

tupla2 = ("carro",)
print(type(tupla2))

tupla3 = ("carro")
print(type(tupla3))

#se nao por a , nao será considerada tupla, mas sim uma str

# set nao é ordenadas e são entre {} nao permite valor duplicado

# uso do if else elif
# atividade 
print()

print("Neste primeiro calculo iremos observar a disponibilidade de água para os seus hectares")
hect = float(input("Quantos hectares? "))
agua = float(input("Quantos litros de água? "))

agua_utili =(agua / hect)

print(f"A cobertura de água por hectares será de", agua_utili,"hec/litros")

if agua_utili < 15:
    print("Quantidade de água é insuficiente para", (int(hect)),"hectares, recomenda-se quantidade maior")
elif agua_utili > 16:
    print("Quantidade de água minima atentida.")
    print("valores podem sofrer alteração com base nas diferentes cultura")
