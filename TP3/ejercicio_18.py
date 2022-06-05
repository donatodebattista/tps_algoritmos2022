from modulo_cola import Cola

import random
from string import ascii_letters
from modulo_cola import Cola

cola_turnos = Cola()
cola1 = Cola()
cola2 = Cola()

class turno:
    def __init__(self, letra, numero):
        self.letra = letra
        self.numero = numero

    def __str__(self):
        return (f"{self.letra}, {self.numero}")

def renglon():
    print("--------------------------------")


#PUNTO A: Cargar la pila de forma random
for i in range (20):
    letras = ["A", "B", "C", "D", "E", "F"]
    numero = (str(random.randint(0, 999)).rjust(3, "0"))  #Funcion que completa los 0 a la izquierda
    letra = letras[random.randint(0, 5)]

    cola_turnos.arribo(turno(letra, numero))

print("COLA TURNOS")
cola_turnos.barrido_turnos()

#PUNTO B: separar cola
datos =[]
def separar_cola():
    letras_cola1 = ["A", "C", "F"]
    while(not cola_turnos.cola_vacia()):
        t = cola_turnos.atencion()
        if t.letra in letras_cola1:
            cola1.arribo(t)
        else:
            cola2.arribo(t) 
        datos.append(t)  #Guardo cada turno en un vector para no perder los datos 

separar_cola()

renglon()                   #Imprimo en pantalla cola 1 y cola 2
print("COLA 1")     
cola1.barrido_turnos()

renglon()
print("COLA 2")
cola2.barrido_turnos()


if(cola1.tamanio() > cola2.tamanio()):
    renglon()

    print("La cola 1 tiene mas turnos, con un total de ", cola1.tamanio(), "turnos")
    print("Letra/s con mas cantidad de turnos de la cola 1:", cola1.letra_con_mas_turnos(["A", "C", "F"]))

    renglon()
    print("Turnos con nro mayor a 506 de la cola 2 (cola menor):")
    cola2.barrido_turnos_nro_mayor_506()

elif(cola2.tamanio() > cola1.tamanio()):
    renglon()
    print("La cola 2 tiene mas turnos, con un total de ", cola2.tamanio(), "turnos")
    print("Letra/s con mas cantidad de turnos:", cola2.letra_con_mas_turnos(["B", "D", "E"]))

    renglon()
    print("Turnos con nro mayor a 506 de la cola 1 (cola menor):")
    cola1.barrido_turnos_nro_mayor_506()
else:
    print("Las colas tienen la misma cantidad de turnos")
