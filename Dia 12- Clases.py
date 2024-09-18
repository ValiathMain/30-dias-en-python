# clases en python

class PersonaVacia: # las clases se hacen con CamelCase
    pass

print(PersonaVacia()) 
print(PersonaVacia)

class Persona:
    def __init__(self, name, surname, alias):
        self.name = name
        self.surname = surname
        self.alias = alias

    def camina(self): # se tiene que usar self para poder usarse con una def
        print(f"{self.name, self.alias} esta caminando")

mi_persona = Persona("Alejandro", "Valianth", "Glez")
print(mi_persona.name)
print(f"{mi_persona.name} {mi_persona.surname}")

mi_persona.camina() # se imprime dirtecto sin poner un print porque esta un ena def con el print



