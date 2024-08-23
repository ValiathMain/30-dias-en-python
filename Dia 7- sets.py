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
