### tema de funciones ###

def mi_funcion ():
    print("Esto es mi funcion") 

mi_funcion()
mi_funcion()
mi_funcion() 


def suma_dos_valores (primer_numero, segundo_numero):
    print(primer_numero + segundo_numero)

suma_dos_valores(5,6)
suma_dos_valores(2,6)
suma_dos_valores(5,7)

#///////////////////////////////

#def multi_dos_numeros (num1, num2):
#    resultado = num1 * num2
#    print(f"El resultado de {num1} y {num2} es: {resultado}")

#num1 = int(input("Inserta el primer numero: "))  # es necesario poner int ya que solo estamos usando un input
#num2 = int(input("inserta el segundo numero: "))

#multi_dos_numeros(num1, num2)

#///////////// dato importante return de datos, cosa que aun no me cuadra bien

def suma_dos_valores_return (primer_numero, segundo_numero):
    return primer_numero + segundo_numero

suma_dos_valores_return(10,5)

mi_resultado = suma_dos_valores_return(5,9)
print(mi_resultado)\


def sumas(num1, num2):
    mi_suma = num1 + num2
    return mi_suma

def print_name(name, surname):
    print(f"{name} {surname}")

print_name("Valianth","Alejandro") # asi no lleva un orden, si no tal cual entran los datos
print_name(surname = "Valianth",name = "Alejandro") # asi estaria ordenado ya que se dicta donde va el valor 

#/////////////////////////

def print_name_default(name, surname, alias = "Sin alias"): # alias seria un valor por defecto o default
    print(f"{name} {surname} {alias}")

print_name_default("Alejandro", "Valianth")

#/////////////////////////////////////

def print_textos(*textos): # esto es para agregar varios textos en el mismo print
    for text in textos:
        print(text)

print_textos("Hola","Adios","brenda","alejandro")