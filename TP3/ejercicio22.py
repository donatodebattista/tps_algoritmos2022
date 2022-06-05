from modulo_cola import Cola

cola_personajes = Cola()
cola_personajes_aux = Cola()

class personaje:
    def __init__(self, nombre_personaje, nombre_superheroe, genero):
        self.nombre_personaje = nombre_personaje
        self.nombre_superheroe = nombre_superheroe
        self.genero = genero 

    def __str__(self):
        return (f"{self.nombre_personaje}, {self.nombre_superheroe}, {self.genero}")



personajes = [
    {"nombre_personaje": "Tony Stark", "nombre_superheroe": "ron Man", "genero": "M"},
    {"nombre_personaje": "Steve Rogers", "nombre_superheroe": "Capitan America", "genero": "M"},
    {"nombre_personaje": "Carol Danvers", "nombre_superheroe": "Capitana Marvel", "genero": "F"},
    {"nombre_personaje": "Natasha Romanoff", "nombre_superheroe": "Black Widow", "genero": "F"},
    {"nombre_personaje": "Scott Lang", "nombre_superheroe": "Ant-Man", "genero": "M"},
]


for pers in personajes:
    cola_personajes.arribo(personaje(pers["nombre_personaje"], 
                                     pers["nombre_superheroe"], 
                                     pers["genero"]))

#Punto A
print("Nombre del personaje de Capitana Marvel:", cola_personajes.personaje_de("Capitana Marvel"))

#Punto B
print("----------------------")
print("Personajes Femeninos:")
cola_personajes.barrido_personajes_femeninos()

#Punto C
print("----------------------")
print("Personajes masculinos:")
cola_personajes.barrido_personajes_masculinos()

#Punto D
print("----------------------")
print("Superheroe de Scott Lang:", cola_personajes.superheroe_de("Scott Lang"))

#Punto E
print("----------------------")
print("Superheroes o personajes que empiezan con la letra S:")
cola_personajes.barrido_letra_s()

#Punto F
print("----------------------")
if (cola_personajes.superheroe_de("Carol Danvers") is None):
    print("El personaje Carol Danvers, no se encuentra en la cola")
else:
    print("Superheroe de Carol Danvers:", cola_personajes.superheroe_de("Carol Danvers"))