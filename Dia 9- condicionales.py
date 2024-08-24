### Condicionales ###

mi_condicional = False

if mi_condicional:
    print("se ejecuta la condicion del if")

mi_condicional = 5*5
if  mi_condicional == 10:
    print("se ejecuta la condicion del segundo if")

if mi_condicional > 10 and mi_condicional < 20:
    print("Es mayor que 10 y menor que 20")
elif mi_condicional == 25: # los elif paran la toma de decision y ahi mismo se quedaria y ya no pasaria por el ultimo else
    print("Es igual a 1")
else:
    print("es menor o igual que 10 o mayor o igual que 20")

print("la ejecucion continua")


mi_str = "h"

if not mi_str:
    print("esta cadena de texto es vacia")

if mi_str == "cadenas de texto":
    print("estas cadenas de texto coinciden")