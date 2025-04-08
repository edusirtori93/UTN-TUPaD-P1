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


#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla; 
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Ingrese una palabra: ")

if frase.endswith("a") or frase.endswith("A"):
    print(f"{frase}!")  
elif frase.endswith("e") or frase.endswith("E"):
    print(f"{frase}!")
elif frase.endswith("i") or frase.endswith("I"):
    print(f"{frase}!") 
elif frase.endswith("o") or frase.endswith("O"):
    print(f"{frase}!")
elif frase.endswith("u") or frase.endswith("U"):
    print(f"{frase}!")   
else:
    print(frase)
    

#8)Escribir un programa que solicite al usuario que ingrese su nombre 
# y el número 1, 2 o 3 dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario 
# e imprimir el resultado por pantalla.

nombre = input("Nombre: ")
print("Ingrese: ")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúsculas.")
print("3. Si quiere su nombre con la primera letra mayúscula.")

num = int(input("Opción: "))

if num == 1:
    print(nombre.upper())
elif num == 2:
    print(nombre.lower())
elif num == 3:
    print(nombre.title())
else:
    print ("La opción ingresada es incorrecta.")


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = float(input("Magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
pass


#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

print("¿En qué emisferio se encuentra?")
print('"N": si se encuentra en el emisferio norte.')
print('"S": si se encuentra en el emisferio sur.')
emisferio = input("Ingrese el caracter que corresponda: ")
print()

print("¿Qué mes del año es?")
print("1 - Enero")
print("2 - Febrero")
print("3 - Marzo")
print("4 - Abril")
print("5 - Mayo")
print("6 - Junio")
print("7 - Julio")
print("8 - Agosto")
print("9 - Septiembre")
print("10 - Octubre")
print("11 - Noviembre")
print("12 - Diciembre")

mes = int(input("Ingrese el número que corresponda: "))
print()

dia = int(input("¿Qué día del mes es?: "))

if emisferio == "N":
    if mes == 12:
        if dia >= 21 and dia <= 31:
            print("Usted está en invierno.")
        else:
             print("La fecha es incorrecta.")          
    elif mes == 1:
        if dia >= 1 and dia <= 31:
            print("Usted está en invierno.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 2:
        if dia >= 1 and dia <= 29:
            print("Usted está en invierno.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 3:
        if dia >= 1 and dia <= 20:
            print("Usted está en invierno.")
        else:
            print("Usted está en primavera.")
    elif mes == 4:
        if dia >= 1 and dia <= 30:
            print("Usted está en primavera.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 5:
        if dia >= 1 and dia <= 31:
            print("Usted está en primavera.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 6:
        if dia >= 1 and dia <= 20:
            print("Usted está en invierno.")
        else:
            print("Usted está en verano.")
    elif mes == 7:
        if dia >= 1 and dia <= 31:
            print("Usted está en verano.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 8:
        if dia >= 1 and dia <= 31:
            print("Usted está en verano.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 9:
        if dia >= 1 and dia <= 20:
            print("Usted está en verano.")
        else:
            print("Usted está en otoño.")
    elif mes == 10:
        if dia >= 1 and dia <= 31:
            print("Usted está en otoño.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 11:
        if dia >= 1 and dia <= 30:
            print("Usted está en otoño.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 12:
        if dia >= 1 and dia <= 20:
            print("Usted está en otoño.")
        pass
    else:
        print("El mes es incorrecto.")

elif emisferio == "S":
    if mes == 12:
        if dia >= 21 and dia <= 31:
            print("Usted está en verano.")
        else:
            print("Usted está en primavera.")
    elif mes == 1:
        if dia >= 1 and dia <= 31:
            print("Usted está en verano.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 2:
        if dia >= 1 and dia <= 29:
            print("Usted está en verano.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 3:
        if dia >= 1 and dia <= 20:
            print("Usted está en verano.")
        else:
            print("Usted está en otoño.")
    elif mes == 4:
        if dia >= 1 and dia <= 30:
            print("Usted está en otoño.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 5:
        if dia >= 1 and dia <= 31:
            print("Usted está en otoño.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 6:
        if dia >= 1 and dia <= 20:
            print("Usted está en otoño.")
        else:
            print("Usted está en invierno.")
    elif mes == 7:
        if dia >= 1 and dia <= 31:
            print("Usted está en invierno.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 8:
        if dia >= 1 and dia <= 31:
            print("Usted está en invierno.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 9:
        if dia >= 1 and dia <= 20:
            print("Usted está en invierno.")
        else:
            print("Usted está en primavera.")
    elif mes == 10:
        if dia >= 1 and dia <= 31:
            print("Usted está en primavera.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 11:
        if dia >= 1 and dia <= 30:
            print("Usted está en primavera.")
        else:
            print("La fecha es incorrecta.")
    elif mes == 12:
        if dia >= 1 and dia <= 20:
            print("Usted está en primavera.")
        pass
    else:
         print("El mes es incorrecto.")
else:
    print("El caracter es incorrecto. Intente nuevamente.")

