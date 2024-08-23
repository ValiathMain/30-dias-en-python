# Dia de sets

mi_set = set()
print(type(mi_set))   

mi_otro_set = {}
print(type(mi_otro_set)) # esto dice que inicialmente es un diccionario

mi_otro_set = {"Alejandro","Valianth",26}
print(type(mi_otro_set))

print(len(mi_otro_set))

mi_otro_set.add("Brenda")

print(mi_otro_set) # un set no es una estrutura ordenada

mi_otro_set.add("Brenda") # En los sets los datos no se pueden repetir

print(mi_otro_set)

print("Valianth" in mi_otro_set) # en lugar de imprimir el dato con el print lo retorna como un dato boolean true o false

mi_otro_set.remove("Valianth")
print(mi_otro_set)

mi_otro_set.clear()
print(len(mi_otro_set))

del mi_otro_set
# print(mi_otro_set)

mi_set = {"Alejandro","Valianth",26}
mi_lista = list(mi_set)

print(mi_lista)
print(mi_lista[1]) # hacer este tipo de transformaciones no es lo mas recomendado ya que de todos modos no llega a tener un orden

mi_otro_set = {"Python","C++","Java"}

nuevo_set = mi_set.union(mi_otro_set)
print(nuevo_set.union(nuevo_set).union(mi_set).union({"Go"})) # no acepta repetidos ||||| si no se pone asi .union({"Go"}) agrega las letras por separado

print(nuevo_set.difference(mi_set))
