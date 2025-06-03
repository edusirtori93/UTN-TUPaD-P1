#1) Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

#módulos
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa principal

imprimir_hola_mundo()


#2)Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre 
# y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

#módulo
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

#programa principal
nombre = input("¿Cómo te llamás?: ")
saludar_usuario(nombre)



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
    print(f"El area del circulo es {area}.")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    print(f"El perímetro del círculo es de {perimetro}.")

#programa principal
radio = positivo_validado("Ingrese el radio del círculo: ")

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio) #Fijarse después cómo reducir dígitos


#5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad 
# de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.

#modulo
def segundos_a_horas(segundos):
    horas = segundos / 3600
    print(f"{segundos} segundos corresponden a {horas} horas.")

#programa principal
segundos = float(input("Ingrese la cantidad de segundos: "))
segundos_a_horas(segundos)