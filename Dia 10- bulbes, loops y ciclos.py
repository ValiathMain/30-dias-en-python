 ## bucles, loops y ciclos ###

mi_condicional = 0

while mi_condicional < 10: # un ciclo while siempre sera mas util para que un codigo se repita en funcion de una condicion 
    print(mi_condicional)
    mi_condicional += 1
else: # es opcional
    print("Mi condicion es mayor o igual que 10")

print("la ejecucion continua")

while mi_condicional < 20:
    mi_condicional += 1
    if mi_condicional == 15:
        print("Se detiene la ejecucion")
        break # esto hace que se detenga el bucle
    
    print(mi_condicional)
 
print("la ejecucion continua")

# for 

mi_lista = [26, 24, 22, 25, 25, 5, 17]

for dato in mi_lista:  # el FOR siempre sera mas util para iterar datos de un lista o terminos similadres
    print(dato)


mi_tupla = (26, 1.78, "Alejandro", "Valianth")

for dato in mi_tupla:
    print(dato)

mi_diccionario = {"Nombre":"Alejandro","Apodo": 'Valianth', "Edad": 26, 1:"Python"}

for dato in mi_diccionario: # solo imprime las keys mas no los value 
    print(dato)
    if dato == "Edad":
        break

else:
    print("El bucle a finalizado")

for dato in mi_diccionario: # solo imprime las keys mas no los value 
    print(dato)
    if dato == "Edad":
        continue 
    print("Se ejecuta")
else:
    print("El bucle a finalizado")
