#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para 
#calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y 
# el número que indique el usuario



def factorial(x):
    return 1 if x == 0 else x * factorial(x - 1)
    
num = int(input('Dale: '))

for i in range(1, num + 1):
    print(f'El factorial de {i} es {factorial(i)}')
    

print()
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
        

#3) 