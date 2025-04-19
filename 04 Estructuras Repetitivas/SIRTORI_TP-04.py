#1)Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for n in range (101):
    print(n)
    

print()
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene. 

entrada = (input("Ingrese un número entero: "))

while not (entrada.isdigit()):
    entrada = input("ERROR. Ingrese un número entero:")
print(f"El número ingresado contiene {len(entrada)} dígito/s.")



print()
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos 
# valores dados por el usuario, excluyendo esos dos valores.

valor1 = int(input("Ingrese un número:"))
valor2 = int(input("Ingrese otro número, mayor que el primero:"))
sumatoria = 0

for i in range(valor1+1, valor2):
    sumatoria += i
print(f"La suma de los numeros comprendidos entre esos dos valores es {sumatoria}")



print()
#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

NUMERO_INVALIDO = 0
num = int(input("Ingrese un número entero (0 para cortar):"))
suma = 0

while not (num == NUMERO_INVALIDO):
    suma += num 
    num = int(input("Ingrese otro número entero (0 para cortar):"))
print(f"La suma de los números ingresados es {suma}")




print()
#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
numero_aleatorio = random.randint(0, 10)
print(numero_aleatorio)

entrada3 = int(input("Adivina un número entre 1 y 9: "))

while entrada3 != numero_aleatorio:
    if entrada3 > 0 and entrada3 <= 9:
        entrada3 = int(input("¡Incorrecto! Inténtalo de nuevo: "))
    else:
        entrada3 = int(input("ERROR. Ingresa un número entre 1 y 9: "))   
print(f"¡Muy bien! El número secreto era {entrada3}")




print()
#6)Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for a in range(100, 0, -2):
    print(a)
    

print()
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 
# y un número entero positivo indicado por el usuario

entrada = int(input("Ingrese un número entero positivo: "))
suma = 0

while entrada < 0:
    entrada = int(input("ERROR. Ingrese un número entero positivo: "))
    
for h in range(0, entrada+1):
    suma += h
print(f"El resultado de la suma es {suma}")



print()
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos.

pares = 0
impares = 0
positivos = 0
negativos =0 


for n in range (0, 100):
    entero = int(input("Ingrese un número entero: "))
    
    if entero % 2 == 0:
        pares += 1
    else:
        impares += 1
        
    if entero >= 0:
        positivos += 1
    else:
        negativos += 1
print()
print(f"La cantidad de numeros pares ingresados fue de {pares}")
print(f"La cantidad de numeros impares ingresados fue de {impares}")  
print(f"La cantidad de numeros positivos ingresados fue de {positivos}")  
print(f"La cantidad de numeros negativos ingresados fue de {negativos}")



print()
#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores.

for m in range (0, 100):
    entero1 = int(input("Ingrese un número entero: "))
    sumatoria += entero1
    

media = sumatoria / 100
print(f"La media de los numeros ingresados es de {media}")




print()
#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

digitos = (input("ingrese un número: "))

while not (digitos.isdigit()):
    digitos = input("ERROR. Ingrese un número entero:")
invertido = int(digitos[::-1])
print(invertido)