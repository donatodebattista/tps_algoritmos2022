def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]

class nodoLista():
    info, sig = None, None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1


    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig

    def atencion(self):         #Devuelve el dato (frente) y lo elimina de la lista
        dato = self.__inicio.info
        self.__inicio = self.__inicio.sig
        self.__tamanio -= 1
        return dato


    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux            
        else:
            return None

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
        if dato:
            self.__tamanio -= 1
        return dato


    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos


    def ultimo_dinosaurio_descubierto(self):
        año_mayor = -1
        año_de_descubrimiento_ultimo = None
        aux = self.__inicio
        while(aux is not None):
            dato = aux.info.descubrimiento
            dato2 = dato.split(", ")
            numero = int(dato2[1])
            if (numero > año_mayor):
                año_mayor = numero
                año_de_descubrimiento_ultimo = aux.info.nombre
            aux = aux.sig
        return(año_de_descubrimiento_ultimo)


    def barrido_dinosaurios(self, dino):
        lvl_alerta = ["high", "critical"]
        aux = self.__inicio
        while(aux is not None):
            if((aux.info.nombre_dinosaurio == dino) and (aux.info.nivel_alerta.strip() in lvl_alerta)):
                print(aux.info)
            aux = aux.sig

