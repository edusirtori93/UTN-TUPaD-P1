print("1")
#1) Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

#módulos
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa principal

imprimir_hola_mundo()

print("\n2")
#2)Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre 
# y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

#módulo
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#programa principal
nombre = input("¿Cómo te llamás?: ")
saludar_usuario(nombre)


print("\n3")
#3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: 
# “Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados.

#modulo
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

#programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("¿Cuántos años tenés?: ")
residencia = input("¿Dónde vivís?: ")

informacion_personal(nombre, apellido, edad, residencia)

print("\n4")
#4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

#modulos
import math

def positivo_validado(mensaje, min = 0, max = float("inf")):
    n = float(input(f"{mensaje}"))
    while n < min or n > max:
        n = float(input(f"ERROR. {mensaje}"))
    return n

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    print(f"El area del circulo es {area:.2f}.")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perímetro del círculo es de {perimetro:.2f}.")

#programa principal
radio = positivo_validado("Ingrese el radio del círculo: ")

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio) #Fijarse después cómo reducir dígitos

print("\n5")
#5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad 
# de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#modulo
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos corresponden a {horas:.2f} horas.")

#programa principal
segundos = float(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)

print("\n6")
#6) Crear una función llamada tabla_multiplicar(numero) que reciba un número 
# como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la función.

#modulo
def entero_validado(mensaje, min = float("-inf"), max = float("inf")):
    n = int(input(f"{mensaje}"))
    while n < min or n > max:
        n = int(input(f"ERROR. {mensaje}"))
    return n

def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i} = {numero*i}")
        i += 1

#programa principal
numero = int(input("Ingrese un número entero: "))
tabla_multiplicar(numero)


print("\n7")
#7) Crear una función llamada operaciones_basicas(a, b) que reciba 
# dos números como parámetros y devuelva una tupla con el resultado 
# de sumarlos, restarlos, multiplicarlos y dividirlos. 
# Mostrar los resultados de forma clara.

#módulos
def operaciones_basicas(a, b):
    suma = a+b
    resta = a-b
    multiplicacion = a * b
    if b!= 0:
        division = a//b
    else:
        division = "ERROR. Division por cero!"
    return (suma, resta, multiplicacion, division)

def mostrar_resultados(resultados):
    print("Resultados de las operaciones básicas son:")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")


#programa principal
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultados = operaciones_basicas(a, b)

operaciones_basicas(a, b)
mostrar_resultados(resultados)


print("\n8")
#8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
# y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

#módulos
def calcular_imc(peso, altura):
    imc = peso / altura**2
    print(f"Su indice de masa corporal es de {imc:.2f}")

#programa principal
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

calcular_imc(peso, altura)


print("\n9")
#9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y 
# devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

#modulo
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5 + 32)
    print(f"Su equivalente en Fahrenheit es: {fahrenheit}")
    
#programa principal
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
celsius_a_fahrenheit(celsius)


print("\n10")
#10) Crear una función llamada calcular_promedio(a, b, c) que reciba 
# tres números como parámetros y devuelva el promedio de ellos. 
# Solicitar los números al usuario y mostrar el resultado usando esta función.

#módulo
def calcular_promedio(a, b, c):
    promedio = (a+b+c) / 3
    print(f"\nEl promedio de los tres números ingresados es de {promedio:.2f}")


#programa principal:
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

calcular_promedio(a, b, c)