from csv import list_dialects
from random import Random, random
from modulo_listas import Lista

class pelicula:
    def __init__(self, nombre, valoracion_publico, anio_estreno, recaudacion ):
        self.nombre = nombre
        self.valoracion_publico = valoracion_publico
        self.anio_estreno = anio_estreno
        self.recaudacion = recaudacion 

    def __str__(self):
        return (f"{self.nombre}, {self.valoracion_publico}, {self.anio_estreno}, {self.recaudacion}")

peliculas = [
    {"nombre": "Avatar", "valoracion": 8, "año_estreno": 2010, "recaudacion": 10},
    {"nombre": "Avengers: End Game", "valoracion": 10, "año_estreno": 2019, "recaudacion": 3},
    {"nombre": "Luca", "valoracion": 10, "año_estreno": 2010, "recaudacion": 4},
    {"nombre": "Harry Potter", "valoracion": 9, "año_estreno": 2006, "recaudacion": 1},
]

lista_peliculas = Lista()
lista_aux = Lista()

for p in peliculas:
    lista_peliculas.insertar(pelicula(p["nombre"], p["valoracion"], p["año_estreno"], p["recaudacion"]), campo="nombre")

lista_peliculas.barrido()

# Punto a
print("------------------------")
anio = int(input("Ingrese el año: "))
print("Peliculas del año", anio)
lista_peliculas.barrido_peliculas_anio(anio)

#Punto B
print("------------------------")
pelicula_mayor_recaudacion = lista_peliculas.pelicula_que_mas_recaudo()
print("La pelicula que mas dinero recaudo es", pelicula_mayor_recaudacion.info.nombre, "con un total de $", pelicula_mayor_recaudacion.info.recaudacion)
print("Informacion de", pelicula_mayor_recaudacion.info.nombre)
print("Nombre:", pelicula_mayor_recaudacion.info.nombre)
print("Valoracion:", pelicula_mayor_recaudacion.info.valoracion_publico)
print("Año de estreno:", pelicula_mayor_recaudacion.info.anio_estreno)
print("Recaudacion:", pelicula_mayor_recaudacion.info.recaudacion)

#Punto C
print("------------------------")
print("Pelicula/s mejor valoradas por el publico:")
lista_peliculas.peliculas_mayor_valoracion()

#Punto D
def clonar_lista(lista1, lista2, campo):
    while (not lista1.lista_vacia()):
        dato = lista1.atencion()
        lista2.insertar(dato, campo= campo)

print("------------------------")
print("Peliculas ordenadas por nombre:")
lista_peliculas.barrido()

print("------------------------")
print("Peliculas ordenadas por recaudacion (menor a mayor):")
clonar_lista(lista_peliculas, lista_aux, "recaudacion")
lista_aux.barrido()

print("------------------------")
print("Peliculas ordenadas por año de estreno:")
clonar_lista(lista_aux, lista_peliculas, "anio_estreno")
lista_peliculas.barrido()

print("------------------------")
print("Peliculas ordenadas por valoracion del publico (menor a mayor):")
clonar_lista(lista_peliculas, lista_aux, "valoracion_publico")
lista_aux.barrido()
