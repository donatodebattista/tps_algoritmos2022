from modulo_lista_de_lista import Lista
from random import randint, choice

class entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas

    def __str__(self):
        return (f"{self.nombre}, {self.torneos_ganados}, {self.batallas_perdidas}, {self.batallas_ganadas}")

class pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return (f"{self.nombre}, {self.nivel}, {self.tipo}, {self.subtipo}")

lista_entrenadores = Lista()
lista_pokemons = Lista()

entrenadores = [
    {"nombre": "Entrenador1", "torneos_ganados": 3, "batallas_perdidas": 50, "batallas_ganadas": 50},
    {"nombre": "Entrenador2", "torneos_ganados": 20, "batallas_perdidas": 4, "batallas_ganadas": 2},
    {"nombre": "Entrenador3", "torneos_ganados": 16,  "batallas_perdidas": 12, "batallas_ganadas": 24},
    {"nombre": "Entrenador4", "torneos_ganados": 2,  "batallas_perdidas": 13, "batallas_ganadas": 90},
    {"nombre": "Entrenador5", "torneos_ganados": 45,  "batallas_perdidas": 10, "batallas_ganadas": 42},
    {"nombre": "Entrenador6", "torneos_ganados": 4,  "batallas_perdidas": 6, "batallas_ganadas": 24},
]

pokemons = [
    {"nombre": "pikachu", "nivel": 40, "tipo": "electrico", "subtipo": "raton"},
    {"nombre": "charizard", "nivel": 180, "tipo": "fuego", "subtipo": "volador"},
    {"nombre": "charmander", "nivel": 20, "tipo": "fuego", "subtipo": "lagartija"},
    {"nombre": "rattata", "nivel": 9, "tipo": "tierra", "subtipo": "raton"},
    {"nombre": "pidgeot", "nivel": 35, "tipo": "fuego", "subtipo": "volador"},
    {"nombre": "squirtle", "nivel": 80, "tipo": "agua", "subtipo": "tortuga"},
    {"nombre": "magicarp", "nivel": 100, "tipo": "agua", "subtipo": "pez"},
    {"nombre": "terrakion", "nivel": 12, "tipo": "tierra", "subtipo": "roca"},
    {"nombre": "tyrantrum", "nivel": 45, "tipo": "planta", "subtipo": "dinosaurio"},
    {"nombre": "wingull", "nivel": 22, "tipo": "aire", "subtipo": "volador"}, 
]

for e in entrenadores:
    lista_entrenadores.insertar(entrenador(e["nombre"],
                                            e["torneos_ganados"],
                                            e["batallas_perdidas"],
                                            e["batallas_ganadas"]),
                                            campo = "nombre")

for p in pokemons:
    lista_pokemons.insertar(pokemon(p["nombre"],
                                    p["nivel"],
                                    p["tipo"],
                                    p["subtipo"]),
                                    campo="nombre")


for e in entrenadores:
    for i in range(randint(1, 5)):
        pok = choice(pokemons)
        pos = lista_entrenadores.busqueda(e["nombre"], "nombre")
        pos.sublista.insertar(pokemon(pok['nombre'],
                                      pok['nivel'],
                                      pok['tipo'],
                                      pok['subtipo']), 'nombre')


lista_entrenadores.barrido_lista_lista()


#Punto A: 
print("---------------A---------------")
e = input("Ingrese el nombre del entrenador: ")
posicion_entrenador = lista_entrenadores.busqueda(e, "nombre")
cantidad_pokemones = posicion_entrenador.sublista.tamanio()
print(f"El entrenador {e} tiene un total de {cantidad_pokemones} pokemones") 


#Punto B:
print("---------------B---------------")
print("Entrenadores con mas de 3 torneos ganados:")
lista_entrenadores.barrido_mas_de_3_torneos_ganados()


#Punto C:
print("---------------C---------------")
entrenador_con_mas_torneos_ganados = lista_entrenadores.mayor_de_lista("torneos_ganados")
pokemon_mas_nivel = entrenador_con_mas_torneos_ganados.sublista.mayor_de_lista("nivel")
print(f"{entrenador_con_mas_torneos_ganados.info.nombre} es el entrenador con mas torneos ganados y su pokemon de mayor nivel es {pokemon_mas_nivel.info}")


#Punto D
print("---------------D---------------")
e2 = input("Ingrese el nombre del entrenador para mostrar toda su info: ")
posicion_e2 = lista_entrenadores.busqueda(e2, "nombre")
if(posicion_e2):
    print(posicion_e2.info)
    print("Pokemones de", e2)
    print(posicion_e2.sublista.barrido())
else:
    print("El entrenador ingresado no se encuentra en la lista")


#Punto E    
print("---------------E---------------")
lista_entrenadores.porcentaje_mayor_79()


#Punto F
print("---------------F---------------")
lista_entrenadores.barrido_tipo_agua_planta_fuego_volador()


#Punto G
print("---------------G---------------")
dato = input("Ingrese el entrenador:")
posicion = lista_entrenadores.busqueda(dato, "nombre")
sublista_dato = posicion.sublista
print(sublista_dato.promedio_nivel())


#Punto H
print("---------------H---------------")
pok = input("Ingrese el pokemon:")
print("Cantidad de entrenadores que tienen el pokemon", pok)
print(lista_entrenadores.barrido_entrenadores_por_pokemon(pok))

#Punto I
print("---------------I---------------")
lista_entrenadores.pokemones_repetidos()

#Punto j
print("---------------J---------------")
print("Entrenadores que tienen a Tyrantrum, Wingull o Terrakion:")
lista_entrenadores.barrido_Tyrantrum_Wingull_Terrakion()


#Punto k
print("---------------K---------------")
entr = input("Ingrese el nombre del entrenador ")
pos_entrenador = lista_entrenadores.busqueda(entr, "nombre")

if (pos_entrenador):
    poke = input("Ingrese el nombre del pokemon ")
    pos_pokemon = pos_entrenador.sublista.busqueda(poke, "nombre")
    if(pos_pokemon):
        print(f"El pokemon {poke} se encuentra en la lista de pokemones de {entr}")
        print("Informacion de", entr)
        print(pos_entrenador.info)
        print("Info de", poke)
        print(pos_pokemon.info)

    else:
        print(f"El pokemon ingresado no se encuentra en la lista de pokemones de {entr}")
else:
    print("El entrenador ingresado no se encuentra en la lista")
