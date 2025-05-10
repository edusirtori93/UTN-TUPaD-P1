#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

lista1 = list(range(4,101,4,))
print(lista1)

print()
#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos!

lista2 = ["Argentina", "Chile", "Canadá", "Brasil"]
print(lista2[-2])

print()
#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.

lista_vacia = []
lista_vacia.append(1)
lista_vacia.append(11)
lista_vacia.append(14)
print(lista_vacia)

print()
#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla.

animales = ["perro", "gato", "carpincho", "serpiente"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

print()
#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#Lo que acaba de realizar el programa es remover uno de los elementos de la lista "números",
# a través de la función "remove" 
# más específicamente se trata del número de mayor valor(22), ubicado o especificado por 
# la función "max".

print()
#6) Crear una lista con números del 10 al 30 (incluído), 
# haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista3 = list(range(10,31,5))
print(lista3[0:2])

print()
#7) Reemplazar los dos valores centrales (índices 1 y 2) 
# de la lista “autos” por dos nuevos valores cualesquiera.

autos = ["sedan", "polo", "sudan","gol"]
autos[1:3] = "siena", "clio"
print(autos)

print()
#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)

print()
#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla.

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

print()
#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:

lista_anidada = [[15],[True], [25.5, 57.9, 30.6], [False]]
print(lista_anidada)