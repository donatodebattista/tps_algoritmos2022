
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

    def insertar_sin_criterio(self, dato):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sig = self.__inicio
        self.__inicio = nodo
        self.__tamanio += 1


    
    def barrido_armadura_traje(self):
        aux = self.__inicio
        while(aux is not None):
            if('traje' in aux.info.bio or 'armadura' in aux.info.bio):
                print(aux.info)
            aux = aux.sig
        

    def barrido_genero_femenino(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.genero == "femenino"):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_anterior_1963(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.aparicion < 1963):
                print(aux.info)
            aux = aux.sig
    
    def barrido_jedi_master(self):
        aux = self.__inicio
        while(aux is not None):
            if('yoda' in aux.info.maestro or 'luke skywalker' in aux.info.maestro):
                print(aux.info)
            aux = aux.sig

    def barrido_droide(self):
        episodios = [1, 2, 3, 4, 5, 6]
        aux = self.__inicio
        while(aux is not None):
            x = 0
            if(aux.info.especie == "droide"):
                if(len(aux.info.episodios) == 6):
                    for i in range (0, 6):
                        if(not aux.info.episodios[i] in episodios):
                            break
                        else:
                            x = x+1
                    if (x == 6):
                        print(aux.info.nombre)
            aux = aux.sig

    def barrido_comienza_con(self, iniciales=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] in iniciales):
                print(aux.info)
            aux = aux.sig


    def contar_por_casa(self):
        marvel, dc = 0, 0

        aux = self.__inicio
        while(aux is not None):
            if(aux.info.casa.capitalize() == 'Marvel'):
                marvel += 1
            if(aux.info.casa.capitalize() == 'Dc'):
                dc += 1
            aux = aux.sig

        return marvel, 

    def barrido_episodios_4_5_6_7(self):
        aux = self.__inicio
        while(aux is not None):
            if (4 in aux.info.episodios and 5 in aux.info.episodios and 6 in aux.info.episodios and 7 in aux.info.episodios):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_personajes_mas_850_anios(self):
        aux = self.__inicio
        mayor = aux
        while(aux is not None):
            if(aux.info.edad > 850):
                print(aux.info.nombre)

                if(aux.info.edad > mayor.info.edad):
                    mayor = aux
            aux = aux.sig
        print(mayor.info.nombre, "es el personaje mayor y tiene", mayor.info.edad, "años.")

    def barrido_humanos_Alderaan(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.especie == "humano" and aux.info.planeta_natal == "Alderaan"):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_altura_menor_70cm(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.altura < 0.70):
                print(aux.info)
            aux = aux.sig

    def barrido_empresa(self, destino):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.destino == destino):
                print("-", aux.info)
            aux = aux.sig


    def barrido_peliculas_anio(self, anio):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.anio_estreno == anio):
                print("-", aux.info)
            aux = aux.sig

    def pelicula_que_mas_recaudo(self):
        aux = self.__inicio
        mayor = aux.info.recaudacion
        pelicula_mayor_recaudacion = aux
        while(aux is not None):
            if(aux.info.recaudacion > mayor):
                mayor = aux.info.recaudacion
                pelicula_mayor_recaudacion = aux
            aux = aux.sig
        return pelicula_mayor_recaudacion

    def peliculas_mayor_valoracion(self):
        aux = self.__inicio
        mayor_valoracion = aux.info.valoracion_publico
        while(aux is not None):
            if(aux.info.valoracion_publico > mayor_valoracion):
                mayor_valoracion = aux.info.valoracion_publico
            aux = aux.sig
        
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.valoracion_publico == mayor_valoracion):
                print("-", aux.info.nombre)
            aux = aux.sig
    

    def barrido_personaje(self, personaje):
        aux = self.__inicio
        while(aux is not None):
            if (aux.info.nombre == personaje):
                print(aux.info)
            aux = aux.sig


    #FUNCIONES EJERCICIO 22
    def barrido_aprendices(self, maestro):
        aux = self.__inicio
        while(aux is not None):
            for i in range (len(aux.info.maestro)):
                if (aux.info.maestro[i] == maestro):
                    print(aux.info.nombre)
            aux = aux.sig


    def barrido_nombre_empieza_con(self, letra):
        aux = self.__inicio
        while(aux is not None):
            if (aux.info.nombre[0] == letra):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_especie(self, especie):
        aux = self.__inicio
        while(aux is not None):
            if (aux.info.especie == especie):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_jedis_mas_de_un_sable_de_luz(self):
        aux = self.__inicio
        while(aux is not None):
            if (len(aux.info.sable_luz) > 1):
                print(aux.info.nombre, "utilizo sables de luz color", aux.info.sable_luz)
            aux = aux.sig

    def barrido_sable_de_luz_violeta_amarillo(self):
        aux = self.__inicio
        while(aux is not None):
            for i in range (0, (len(aux.info.sable_luz))): 
                if ((aux.info.sable_luz[i]) == "yellow") or ((aux.info.sable_luz[i]) == "purple"):
                    print(aux.info)
                    break
            aux = aux.sig