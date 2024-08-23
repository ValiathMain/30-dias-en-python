# dia de tuplas
# la tupla se puede definir de estas 2 maneras, pero las mas correcta es la segunda 
mi_tupla = tuple()
mi_otra_tupla = (10,20,30,40,50,60)

mi_tupla = (26, 1.78, "Alejandro", "Valianth")
print(mi_tupla)
print(type(mi_tupla))

print(mi_tupla[0])
print(mi_tupla[-1])
# llamar a datos fuera de rango dara error asi como en las listas
#print(mi_tupla[4])
#print(mi_tupla[-6])

print(mi_tupla.count("Alejandro")) # retorna la cantidad de veces que existe en la tupla
print(mi_tupla.index("Valianth"))  # retorna en que posicion esta el dato en la misma tupla

# mi_tupla[1] = 1.80 # a las tuplas no se les puede agregar datos
# print(mi_tupla)    se dice que una tupla es inmutable

mi_nueva_tupla = mi_tupla + mi_otra_tupla # las tuplas tambien se pueden sumar/concatenar
print(mi_nueva_tupla)

print(mi_nueva_tupla[0:4]) # sacar datos de una tupla de un rango a otro

mi_tupla = list(mi_tupla)
print(type(mi_tupla))

mi_tupla[3] = "Brenda"
mi_tupla.insert(1, "Valianth")
print(mi_tupla)

mi_tupla = tuple(mi_tupla) # las tuplas se peuden convertir a listas y viceversa
print(type(mi_tupla))      # recordemos que si vamos a usar una tupla es porque realmente no se va cambiar nada

#del mi_tupla se puede borrar una tupla 
print(mi_tupla)