print("suma: ",  2 + 3)
print("resta", 3 - 4)
print("multiplicacion", 3 * 5 )
print("Division: ", 4 / 2)                       
print("Division: ", 7 / 2)
print("residio de la divicion: ", 7 // 6)
print("divicion: ", 2 / 6)
#cantidad que sobra despues te poner el segundo digito en el primero
print("cuanto sobra al menos un numero en otro:", 10 % 2)
print("exponente: ", 2**3)

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('numeros compeljos: ', 1 + 1j)
print('multiplicacion de numeros complejos: ',(1 + 1j) * (1-1j))

#tambien se pueden juntar con cadenas de texto
texto1 = "hola "
texto2 = "python"

print(texto1 + texto2)

# convertir un dato int en un dato str
print("hola " + str(5) + " python")
print("hola" + str(5) + "python")
print("hola" * 5)

#print con str y valor 
print("Total:", 26)
print("Producto:", "computadora")   

# calcular la arena de una circulo

pi = 3.1416
rad = 6
area_circulo = pi * rad ** 2

print(f"el area del circulo es: {area_circulo} metros cuadrados")

# calcular el area de un rectangulo

alto = 5
largo = 5
area_cuadrado = alto * largo

print(f"El area del rectangulo es: {area_cuadrado} metros cuadrados")

# calcular la masa de un objeto

masa = 75
gravedad = 9.81
formula_peso = masa * gravedad

print(f"El peso es: {formula_peso} N")

# datos booleanos con mayor y menor

print(3 > 2)   # el resultado es True porque 3 si es mayor que 2
print(3 >= 2)  # el resultado es True porque 3 mayor o igual que 2
print(3 < 2)   # el resultado es False porque 3 no es mayor que 2
print(2 < 3)   # el resultado es True porque 2 si es menor que 3
print(2 <= 3)  # el resultado es True porque 2 si es menor o igual que 3
print(3 == 2)  # el resultado es False porque 2 no es igual a 3
print(3 != 2)  # El resultado es True porque 3 si es diferente a 2

# comparando la cantidad de letras en palabras, True y False como el caso de arriba

print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

#comparacion booleana

print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# mas modos de comparacion

print('1 is 1', 1 is 1)                   # 1 esta en 1 asi que es True
print('1 is not 2', 1 is not 2)           # 1 no esta en 2 asi que es True
print('A in Asabeneh', 'A' in 'Asabeneh') # A esta en Asabeneh asi que es True
print('B in Asabeneh', 'B' in 'Asabeneh') # B no esta asabeneh asi que es False
print('coding' in 'coding for all')       # Coding esta en coding for all asi que es True
print('a in an:', 'a' in 'an')            # a esta en an asi que es True
print('4 is 2 ** 2:', 4 is 2 ** 2)        # 4 esta en 2**2 asi que es True

