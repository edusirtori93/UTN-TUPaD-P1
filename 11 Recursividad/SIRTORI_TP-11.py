#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para 
#calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y 
# el número que indique el usuario


print('1')
def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)
    
num = int(input('Ingrese un numero entero mayor que 1: '))

for i in range(1, num + 1):
    print(f'El factorial de {i} es {factorial(i)}')
    

print('\n2')
# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)
    
pos = int(input('Ingrese una posición: '))

for a in range(0, pos):
    if a <= pos:
        print(f'El valor de la posición {a} es {fibonacci(a)}')
        



print('\n3')
#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(n, p):
    if p == 0:
        return 1
    else:
        return n * potencia(n, p - 1)


base = int(input("Ingrese el número base: "))
exponente = int(input("Ingrese el número del exponente: "))

resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es igual a {resultado}")



print('\n4')
#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal 
# y devuelva su representación en binario como una cadena de texto.

def pasar_binario(nro):
    if nro == 0:
        return ""
    else:
        return pasar_binario(nro // 2) + str(nro % 2)


nro = int(input("Ingrese un número entero positivo: "))
if nro == 0:
    print("0")
else:
    binario = pasar_binario(nro)
    print(f"El número {nro} en binario es: {binario}")
    
print('\n5')
#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False
    
palabra = input("Ingrese un espacio sin cadenas ni tildes: ")
print(es_palindromo(palabra))


print('\n6')
#6) Escribí una función recursiva en Python llamada suma_digitos(n) 
# que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingrese un número: "))
print(f'La suma de los dígitos del número ingresado es de {suma_digitos(numero)}')



print('\n7')
#7) Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo 
# y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
bloques = int(input('Ingrese el nro de la base de la piramide: '))
print(f'El numero de bloques necesario para construir una piramide es de {contar_bloques(bloques)}')


print('\n8')
#8)
