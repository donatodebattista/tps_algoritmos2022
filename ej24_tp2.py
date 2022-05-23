# Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
# necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
# ción uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
# car la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.

from modulo_pila import Pila

personaje1 = {"nombre": "Groot", "cantidad_peliculas": 7}        
personaje2 = {"nombre": "Thor", "cantidad_peliculas": 5}
personaje3 = {"nombre": "Rocket Raccoon", "cantidad_peliculas": 8}
personaje4 = {"nombre": "Iron Man", "cantidad_peliculas": 3}
personaje5 = {"nombre": "Black Widow", "cantidad_peliculas": 2}
personaje6 = {"nombre": "Capitan America", "cantidad_peliculas": 9}
personaje7 = {"nombre": "Daredevill", "cantidad_peliculas": 2}

pila_personajes = Pila()
pila_personajes_aux = Pila()
vec_personajes_mas_5_peliculas = []
letras_iniciales = ["C", "D", "G"]
vec_personajes_empieza_C_D_G = []

pila_personajes.apilar(personaje1)
pila_personajes.apilar(personaje2)
pila_personajes.apilar(personaje3)
pila_personajes.apilar(personaje4)
pila_personajes.apilar(personaje5)
pila_personajes.apilar(personaje6)
pila_personajes.apilar(personaje7)

def cargar_pila_auxiliar():
    while(not pila_personajes.pila_vacia()):
        pila_personajes_aux.apilar(pila_personajes.desapilar())

def posicion_personaje(personaje):
    cargar_pila_auxiliar()
    pos_actual = 0
    pos_pers = 0

    while(not pila_personajes_aux.pila_vacia()):
        dato = pila_personajes_aux.desapilar()
        pos_actual += 1
        
        if (dato["nombre"] is personaje):
            pos_pers = pos_actual

        pila_personajes.apilar(dato)

    return pos_pers

def personajes_mas_5_peliculas():
    cargar_pila_auxiliar()
    while(not pila_personajes_aux.pila_vacia()):
        dato = pila_personajes_aux.desapilar()
        
        if(dato["cantidad_peliculas"] > 5):
            vec_personajes_mas_5_peliculas.append(dato)

        pila_personajes.apilar(dato)

    return(vec_personajes_mas_5_peliculas)

def cantidad_de_peliculas_personaje(personaje):
    cant_peliculas = 0
    cargar_pila_auxiliar()
    while(not pila_personajes_aux.pila_vacia()):
        dato = pila_personajes_aux.desapilar()

        if (dato["nombre"] is personaje):
            cant_peliculas = dato["cantidad_peliculas"]
        pila_personajes.apilar(dato)
    return cant_peliculas
        

def nombres_C_D_G():
    cargar_pila_auxiliar()

    while(not pila_personajes_aux.pila_vacia()):
        dato = pila_personajes_aux.desapilar()

        if (dato["nombre"][0] in letras_iniciales):
            vec_personajes_empieza_C_D_G.append(dato["nombre"])
        
        pila_personajes.apilar(dato)

    return vec_personajes_empieza_C_D_G



print("Posicion de Groot: ", posicion_personaje("Groot"))
print("Posicion de Rocket Raccoon: ", posicion_personaje("Rocket Raccoon"))
print("--------------------------------------")

personajes_mas_5_peliculas()
print("Personajes con mas de 5 peliculas:")
for i in range(len(vec_personajes_mas_5_peliculas)):
    print("-","personaje:", vec_personajes_mas_5_peliculas[i]["nombre"], "- cantidad de peliculas:", vec_personajes_mas_5_peliculas[i]["cantidad_peliculas"])
print("--------------------------------------")
print("Cantidad de peliculas de Black Widow:", cantidad_de_peliculas_personaje("Black Widow"))

print("--------------------------------------")
print("Personajes que empiezan con C, G, o D")
nombres_C_D_G()
for i in range(len(vec_personajes_empieza_C_D_G)):
    print("-", vec_personajes_empieza_C_D_G[i])
