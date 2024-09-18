# excepciones

numero_one, numero_two = 5, 1

numero_two = "1"
 
try:
    print(numero_one + numero_two)
    print("no se a produciod errores")
except:
    print("Se cometio un error")


# try exccept else
try:
    print(numero_one + numero_two)
    print("no se a produciod errores")
except:  # no se puede quitar porque si hay un try hay un e4scept
    print("Se cometio un error")   
else: # este es opcional
    print("La ejecucion continua correctamente ")
finally: # esta igual es opcional
    print("La ejecucion continua")


try:
    print(numero_one + numero_two)
    print("no se a produciod errores")
except TypeError: 
    print("Se cometio un error")  