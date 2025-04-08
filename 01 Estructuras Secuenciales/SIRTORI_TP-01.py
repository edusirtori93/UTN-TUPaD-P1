# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!")


# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Por favor, ingrese su nombre:")
print(f"Hola {nombre}!")


#3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre1 = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
nacionalidad = input("Lugar de residencia: ")

print(f"Soy {nombre1} {apellido}, tengo {edad} años y vivo en {nacionalidad}.")


#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Ingrese el radio del círculo: "))
pi = 3.1416

area = pi*radio**2
perimetro = 2*pi*radio

print(f"El área del círculo es {area}, mientras que su perímetro es {perimetro}")


#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = float(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"Equivale a {horas} horas")


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

num_mul = int(input("Ingrese un número para multiplicar: "))

print(f"{num_mul} x 1 = {num_mul*1}")
print(f"{num_mul} x 2 = {num_mul*2}")
print(f"{num_mul} x 3 = {num_mul*3}")
print(f"{num_mul} x 4 = {num_mul*4}")
print(f"{num_mul} x 5 = {num_mul*5}")
print(f"{num_mul} x 6 = {num_mul*6}")
print(f"{num_mul} x 7 = {num_mul*7}")
print(f"{num_mul} x 8 = {num_mul*8}")
print(f"{num_mul} x 9 = {num_mul*9}")
print(f"{num_mul} x 10 = {num_mul*10}")


#7) Crear un programa que pida al usuario dos números enteros distintos del 0 
# y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

num1 = int(input("Ingrese un número distinto de 0: "))
num2 = int(input("Ingrese otro número distinto de 0: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 // num2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))

imc = peso / altura**2

print(f"Su IMC es de {imc}")


#9) Crear un programa que pida al usuario una temperatura en grados Celsius 
# e imprima por pantalla su equivalente en grados Fahrenheit.

temp_cel = float(input("Ingrese la temperatura en grados Celcius: "))
temp_fahr = (temp_cel * 9/5 + 32)

print(f"Su equivalente en Fahrenheit es: {temp_fahr}")


#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

num_1 = int(input("Ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Ingrese el tercer número: "))

promedio = (num_1 + num_2 + num_3) / 3

print(f"El promedio es de {promedio}")

