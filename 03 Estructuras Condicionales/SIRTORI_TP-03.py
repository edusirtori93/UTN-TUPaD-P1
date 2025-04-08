#1)Escribir un programa que solicite la edad del usuario. 
#Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Es mayor de edad.")
pass


#2)Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, 
# deberá mostrar por pantalla un mensaje que diga “Aprobado”;
# en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese una nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

 
#3)Escribir un programa que permita ingresar solo números pares. 
# Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par";
# en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". 
# Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese un número: "))

if num % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")
    

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla 
# a cuál de las siguientes categorías pertenece: 
# Niño/a: menor de 12 años. 
# Adolescente: mayor o igual que 12 años y menor que 18 años. 
# Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# Adulto/a: mayor o igual que 30 años. 

tuedad = int(input("Ingrese su edad: "))

if tuedad < 12:
    print("Usted es un niño.")
elif tuedad >= 12 and tuedad < 18:
    print("Usted es un adolescente.")
elif tuedad >= 18 and tuedad < 30:
    print("Usted es un adulto joven.")
else:
    print("Usted es un adulto.")
    

#5)Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). 
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta";
# en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

contrasena = input("Ingrese su contraseña: ")

if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 carácteres.")
    

#6)El paquete statistics de python contiene funciones que permiten tomar una lista de números 
# y calcular la moda, la mediana y la media de dichos números.
# escribir un programa que tome la lista numeros_aleatorios, 
# calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo.


import statistics
import random

numeros_aleatorios = [random.randint(1, 100) for i in range (50)]
#Nota: el bloque de código anterior crea una lista con 50 números 
# entre 1 y 100 elegidos de forma aleatoria.

moda = statistics.mode(numeros_aleatorios)
print(f"Moda: {moda}")

mediana = statistics.median(numeros_aleatorios)
print(f"Mediana: {mediana}")

media = statistics.mean(numeros_aleatorios)
print(f"Media: {media}")

if (media > mediana  > moda):
    print("Hay sesgo positivo")   
elif (media < mediana < moda):
    print("Hay sesgo negativo")
elif (media == mediana == moda):
    print("Sin sesgo")
pass

