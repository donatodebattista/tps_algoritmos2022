from modulo_cola import Cola
from modulo_lista import Lista
from modulo_jurasick_park import dinosaurs

class dinosaurio:
    def __init__(self, nombre, tipo, numero, periodo, descubrimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.numero = numero
        self.periodo = periodo
        self.descubrimiento = descubrimiento

    def __str__(self):
        return (f"{self.nombre}, {self.tipo}, {self.numero}, {self.periodo}, {self.periodo}, {self.descubrimiento}")

class alerta:
    def __init__(self, tiempo, codigo_zona, numero_dinosaurio, nombre_dinosaurio, alimentacion_dinosaurio, nivel_alerta):
        self.tiempo = tiempo
        self.codigo_zona = codigo_zona
        self.numero_dinosaurio = numero_dinosaurio
        self.nombre_dinosaurio = nombre_dinosaurio
        self.alimentacion_dinosaurio =alimentacion_dinosaurio
        self.nivel_alerta = nivel_alerta

    def __str__(self):
        return (f"{self.tiempo}, {self.codigo_zona}, {self.numero_dinosaurio}, {self.nombre_dinosaurio}, {self.alimentacion_dinosaurio}, {self.nivel_alerta}")

lista_dinosaurios = Lista()
lista_alertas_tiempo = Lista()
lista_alertas_dinosaurios = Lista()
lista_alertas_dinosaurios_aux = Lista()

cola_hervivoros = Cola()
cola_carnivoros = Cola()

for d in dinosaurs:
    lista_dinosaurios.insertar(dinosaurio(d["name"], d["type"], d["number"], d["period"], d["named_by"]), "nombre")

file = open("alerts.txt")

lineas = file.readlines()


lineas.pop(0)
for linea in lineas:
    datos = linea.split(';')

    nro = datos[2]
    d = lista_dinosaurios.busqueda(int(nro), "numero")
    lista_alertas_tiempo.insertar(alerta(datos[0],
                             datos[1],
                             datos[2],
                             d.info.nombre,
                             d.info.tipo, 
                             datos[3].rstrip('\n')),
                            campo='tiempo')

    nro = datos[2]
    d = lista_dinosaurios.busqueda(int(nro), "numero")

    lista_alertas_dinosaurios.insertar(alerta(datos[0],
                                              datos[1],
                                              datos[2],
                                              d.info.nombre,
                                              d.info.tipo,
                                              datos[3].rstrip('\n')),
                                              campo='nombre_dinosaurio')


#Ultimo descubrimiento
pos = lista_dinosaurios.busqueda(lista_dinosaurios.ultimo_dinosaurio_descubierto(), "nombre")
dato = pos.info.descubrimiento
dato2 = dato.split(", ")
print("El ultimo dinosaurio en ser descubierto es: ")
print(lista_dinosaurios.ultimo_dinosaurio_descubierto(), "y fue descubierto por", dato2[0])

#lista_dinosaurios.barrido()
print("Listado de alertas ordenado por tiempo")
lista_alertas_tiempo.barrido()
print("----------------------------")
print("Listado de alertas ordenado por nombre de dinosaurio")
lista_alertas_dinosaurios.barrido()

#ELIMINAR ZONAS
lista_alertas_tiempo.eliminar("WYG075", "codigo_zona")
lista_alertas_tiempo.eliminar("SXH966", "codigo_zona")
lista_alertas_tiempo.eliminar("LYF010", "codigo_zona")

#MODIFICAR ZONA HYD195
pos = lista_alertas_dinosaurios.busqueda("HYD195", "codigo_zona")
pos.info.nombre_dinosaurio = "Mosasaurus"    
print("--------------------------")
print("Alerta con nombre de dinosaurio modificado:")
print(pos.info)
 


#LISTADO DE LA INFORMACION DE LOS DINOSAURIOS Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel  ́critical’ o ‘high’.
print("--------------------------")
print("#LISTADO DE LA INFORMACION DE LOS DINOSAURIOS Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel  ́critical’ o ‘high’")
lista_alertas_dinosaurios.barrido_dinosaurios("Tyrannosaurus Rex")
lista_alertas_dinosaurios.barrido_dinosaurios("Spinosaurus")
lista_alertas_dinosaurios.barrido_dinosaurios("Giganotosaurus")

#CARGAR COLAS
while(not lista_alertas_dinosaurios.lista_vacia()):
    lvl_alert = ["medium", "low"]
    dato = lista_alertas_dinosaurios.atencion()
    if((dato.alimentacion_dinosaurio == "carnívoro ") and (not dato.nivel_alerta in lvl_alert)):
        cola_carnivoros.arribo(dato)
    elif((dato.alimentacion_dinosaurio == "herbívoro ") and (not dato.nivel_alerta in lvl_alert)):
        cola_hervivoros.arribo(dato)
    lista_alertas_dinosaurios_aux.insertar(dato, "nombre_dinosaurio")

#ATENDER COLAS DE ALERTAS Y MOSTRAR LA INFO EN PANTALLA A EXCEPCION DE EPC944
print("--------------------")
while(not cola_carnivoros.cola_vacia()):
    dato = cola_carnivoros.atencion()
    if(dato.codigo_zona != "EPC944"):
        print(dato)

#LISTAR DINOSAURIOS Raptors Y Carnotaurus Y EL CODIGO DE ZONA DE Compsognathus
print("---------------------------")
for i in range (lista_alertas_dinosaurios_aux.tamanio()):
    dato = lista_alertas_dinosaurios_aux.atencion()
    if(dato.nombre_dinosaurio == "Raptors (Dromaeosauridae)" or dato.nombre_dinosaurio == "Carnotaurus"):
        print(dato)
    if(dato.nombre_dinosaurio == "Compsognathus"):
        print("Podemos encontrar un Compsognathus en las zonas", dato.codigo_zona)
