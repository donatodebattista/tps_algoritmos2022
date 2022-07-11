from modulo_listas import Lista

class Jedi:
    def __init__(self, nombre, maestro, sable_luz, especie):
        self.nombre = nombre
        self.maestro = maestro
        self.sable_luz = sable_luz
        self.especie = especie

    def __str__(self):
        return f"{self.nombre} | {self.maestro} | {self.sable_luz} | {self.especie}"


lista_jedis_nombre = Lista()
lista_jedis_especie = Lista()

file = open('archivo_jedi.txt')
lineas = file.readlines()

lineas.pop(0) 
for linea in lineas:
    datos = linea.split(';')
    # datos.pop(-1)
    lista_jedis_nombre.insertar(Jedi(datos[0],
                             datos[3].split('/'),
                             datos[4].split('/'),
                             datos[2]),
                        campo='nombre')

    lista_jedis_especie.insertar(Jedi(datos[0],
                              datos[3].split('/'),
                              datos[4].split('/'),
                              datos[2]),
                         campo='especie')

#Punto A
lista_jedis_nombre.barrido()
print("-------------------------------------------------------")
lista_jedis_especie.barrido()

print("-------------------------------------------------------")
#Punto B
pos_ahsokaTano = lista_jedis_nombre.busqueda("ahsoka tano", "nombre")
print("Informacion de ahsoka tano:")
print("- Nombre:", pos_ahsokaTano.info.nombre)
print("- Maestros:", pos_ahsokaTano.info.maestro)
print("- Colores de sable de luz:", pos_ahsokaTano.info.sable_luz)
print("- especie:", pos_ahsokaTano.info.especie)
print("-------------------------------------------------------")
pos_kitFisto = lista_jedis_nombre.busqueda("kit fisto", "nombre")
print("Informacion de Kit Fisto:")
print("- Nombre:", pos_kitFisto.info.nombre)
print("- Maestros:", pos_kitFisto.info.maestro)
print("- Colores de sable de luz:", pos_kitFisto.info.sable_luz)
print("- especie:", pos_kitFisto.info.especie) 

#Punto C
print("-------------------------------------------------------")
print("APRENDICES DE YODA:")
lista_jedis_nombre.barrido_aprendices("yoda")
print("-------------------------------------------------------")
print("APRENDICES DE Luke Skywalker:")
lista_jedis_nombre.barrido_aprendices("luke skywalker")

print("-------------------------------------------------------")

#Punto D
print("Jedis de especie humana:")
lista_jedis_nombre.barrido_especie("human")
print("-------------------------------------------------------")
print("Jedis de especie twi'lek:")
lista_jedis_nombre.barrido_especie("twi'lek")

print("-------------------------------------------------------")
#Punto E
print("Jedis que empiezan con A")
lista_jedis_nombre.barrido_nombre_empieza_con("a")

print("-------------------------------------------------------")
#Punto F
print("Jedis que utilizaron mas de un sable de luz")
lista_jedis_nombre.barrido_jedis_mas_de_un_sable_de_luz()

print("-------------------------------------------------------")
#Punto G
print("Jedis que utilizaron sables de luz amarillos o violetas")
lista_jedis_nombre.barrido_sable_de_luz_violeta_amarillo()

print("-------------------------------------------------------")
#Punto H
print("Padawans de qui-gon jin")
lista_jedis_nombre.barrido_aprendices("qui-gon jin")
print("---------------")
print("Padawans de mace windu")
lista_jedis_nombre.barrido_aprendices("mace windu")