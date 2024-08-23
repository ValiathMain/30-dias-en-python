# strings

# las comillas dobles y las comidllas simples funcionan totalmente igual
my_string = "Hola python"
my_string2 = 'Hola python2'

print(len(my_string))
print(len(my_string2))

# como agregar un espacio con comillas en un string
print(my_string + " " + my_string2)

# como hacer un string con salto de linea 
my_new_string = "este es un salto de linea\naqui esta el otro salto de linea"

print(my_new_string)

# este es un string con tabulacion
my_tab_string = "\teste es un string con tabulacion"

print(my_tab_string)

# este es un string con escape
my_scape_string = "\\este es un string \\n con escapado"

print(my_scape_string)

# formateo, para un string es %s y para un int es %d en caso de usar %s o %d
# para el formateo con .format es con llaves {}
# concatenar y con mas es una mala practica
# esta es una inferencia de datos y es la mejor forma de meter datos dentro de un string
name, surname, age = "Alejandro", "Valianth", 26

print("Mi nombres es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombres es %s %s y mi edad es %d" %(name, surname, age))
print
print(f"Mi nombres es {name} {surname} y mi edad es {age}")

# desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language

print(a)
print(b)

# division de caracteres

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#saltar caracteres 
language_slice = language[0:6:2]
print(language_slice)

# volterar una variable
voltear_lenguage = language[::-1]
print(voltear_lenguage)

# funciones --------
print(language.capitalize()) # poner la primera mayuscula
print(language.upper())      # poner todo en mayuscula
print(language.count("t"))   # buscar un dato u caracter en una variable
print(language.isnumeric())  # nos dice si es numerico en boolean
print(language.lower())      # pone todo en minisculas
print(language.lower().isupper()) # forma de comprobar si es mayusculas y da el resultado en boolean
print(language.startswith("py"))
