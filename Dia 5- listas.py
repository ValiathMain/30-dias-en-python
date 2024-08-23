### listas ###

# las listas se definen como mi_lista = list() o  mi_lista = []
mi_lista = list()
mi_otra_lista = []

print(len(mi_lista))

mi_lista = [26, 24, 22, 25, 25, 5, 17]

print(mi_lista)
print(len(mi_lista))

mi_otra_lista= [26, 1.78, "Alejandro", "Valianth"]
print(mi_otra_lista)
print(type(mi_otra_lista))

print(mi_otra_lista[0])
print(mi_otra_lista[1])
print(mi_otra_lista[-1])
print(mi_otra_lista[-4]) # imprimir fuera del rango de la lista solo dara un indexerror

print(mi_otra_lista.count("Alejandro")) # cuenta el numero de datos que se repite
print(mi_lista.count(25))
print(f"la cantidad de veces que se repite 25 es: {mi_lista.count(25)}")

#////////////////////////////////////////////////////////////////////////////////////////////

age, height, name , surname = mi_otra_lista
print(name)

# se pueden sumar listas
print(mi_lista + mi_otra_lista)

# las listas solo se defienen con [] mientras esto solo sera una variable y un string
#mi_lista = "hola python" \\\\\ Si haces una variable con el mismo nombre de la lista, es posible que te de errores y quieres seguir usando la lista mas abajo en tu codigo
print(mi_lista)
print(type(mi_lista))

# esto agrega un nuevo dato a una lista, especificamente al ultimo lugar
mi_otra_lista.append("Brenda")
print(mi_otra_lista)

# esto inserta un dato en la posicion que tu decidas 
mi_otra_lista.insert(0, "Xalapa")
print(mi_otra_lista)

#esto borra el dato que tu indiques o escribas en el .remove (solo borra un dato, si es que se repiten)
mi_otra_lista.remove("Xalapa")
print(mi_otra_lista) 

# este .pop borra el ultimo dato pero lo retorna, pero tambien se puede sacar cualquiera .pop(2) usando esa modalidad, y te seguira retornando el dato borraro una linea abajo
elemento_pop = mi_otra_lista.pop() # forma de guardar el elemento que se saco
#print(mi_otra_lista.pop())
print(mi_otra_lista)
print(elemento_pop)

# eliminar un dato de la liste definitivamente
del mi_lista[2]
print(mi_lista)

# forma de copiar una lista a otra (tener cuidado si se hace despues de un clear)
mi_otra_lista = mi_lista.copy()

# como limpiar totalmente una lista
mi_lista.clear()
print(mi_lista)

# imprimir una lista que se copio arriba
print(mi_lista)
print(mi_otra_lista)

# como voltear el sentido de la lista generalmente
mi_otra_lista.reverse()
print(mi_otra_lista)

#ordenar una lista de un orden alfabetico u numerico
mi_otra_lista.sort()
print(mi_otra_lista)

# sublistas
print(mi_otra_lista)
print(mi_otra_lista[3:4]) # para sacar datos de una lista y su posicion