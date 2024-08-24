#  Dia de Diccionarios 

mi_diccionario = dict()
print(type(mi_diccionario))

mi_otro_diccionario = {}
print(type(mi_otro_diccionario))

mi_otro_diccionario = {"Nombre":"Alejandro","Apodo": 'Valianth', "Edad": 26, 1:"Python"}

# en un diccionario esta es una forma bastante comoda para no revolerse con los datos puestos sobre el mismo
mi_diccionario = {
     "Nombre":"Alejandro",
     "Apodo": 'Valianth', 
     "Edad": 26, 
     "Lenguajes": {"Python", "C++", "Machine learning"}, # forma de meter varias variables en una sola parte del diccionario
     "Colores": {"Azul", "Gris", "Verde"},
     1: 1.78
}

print(mi_otro_diccionario)
print(mi_diccionario)

print(len(mi_otro_diccionario))
print(len(mi_diccionario))

print(mi_diccionario["Nombre"])

mi_diccionario["Nombre"] = "Brenda" # forma de reemplazar un dato

print(mi_diccionario["Nombre"])

print(mi_diccionario[1])

mi_diccionario["Ciudad"] = "Xalapa" # Forma de agregar un dato nuevo es igual a reemplazar

print(mi_diccionario)

del mi_diccionario["Ciudad"] # aqui con del podemos borrar un elemento y solo ese
print(mi_diccionario)

print("Valianth" in mi_diccionario) # no encuentra por valor
print("Apodo" in mi_diccionario)    # encuentra por llave ambos retornando en dato bool

print(mi_diccionario["Apodo"])

print(mi_diccionario.items())    # muestra todo los datos, las llaves nunca cambian pero los valores si pueden cambiar en orden
print(mi_diccionario.keys())     # muestras solo las llaves/keys
print(mi_diccionario.values())   # muestra solo los valores/values sin las llaves
#print(mi_diccionario.fromkeys)

new_dic = dict.fromkeys(("Alias","color",1))

print(new_dic)

new_dic["Alias"] = "Brenditan"

print(new_dic)

#------------------------------------------

lista = ["nombre",1,"colores"] 

the_dict = dict.fromkeys((lista)) # una lista se puede convertir ne un diccionario y viseversa
print(the_dict)

#--------------------------------------

dicci = dict.fromkeys(mi_diccionario) # esta es una forma de borrar los values de un dict y solo quedarte con las keys en otro nuevo diccionario
print(dicci)

#------------------------------------

dicci = dict.fromkeys(mi_diccionario,("Ale","sis")) # una forma de metes esos valores en todas las keys
print(dicci)