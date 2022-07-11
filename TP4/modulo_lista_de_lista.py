def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoLista():
    info, sig, sublista = None, None, None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

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
    
    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            print("-------------------------------")
            # aux1 = aux.sublista.__inicio
            # while(aux1 is not None):
            #     print('  ', aux1.info)
            #     aux1 = aux1.sig

            aux = aux.sig


    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

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

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None

    
    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
            aux = aux.sig
        return mayor

    #Funciones ejercicio 15
    def barrido_mas_de_3_torneos_ganados(self):
        aux = self.__inicio
        while(aux is not None):
            if (aux.info.torneos_ganados > 3):
                print("-", aux.info.nombre)
            aux = aux.sig

    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
            aux = aux.sig
        return mayor
    

    def porcentaje_mayor_79(self):
        aux = self.__inicio
        while(aux is not None):
            porcentaje = 0
            total_batallas = aux.info.batallas_ganadas + aux.info.batallas_perdidas
            porcentaje = (aux.info.batallas_ganadas * 100) / total_batallas
            if(porcentaje > 79):
                print(aux.info)
            aux = aux.sig


    def barrido_tipo_agua_planta_fuego_volador(self):
        vec_tipo_subtipo = ["agua", "planta", "fuego", "volador"]
        aux = self.__inicio
        while(aux is not None):
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if ((aux2.info.tipo in vec_tipo_subtipo) or (aux2.info.subtipo in vec_tipo_subtipo)):
                    print(aux.info.nombre)
                    break
                aux2 = aux2.sig
            aux = aux.sig

    def promedio_nivel(self):
        total = 0
        aux = self.__inicio
        while(aux is not None):
            total = total + aux.info.nivel
            aux = aux.sig
        return total / self.tamanio()

    def barrido_entrenadores_por_pokemon(self, pok):
        aux = self.__inicio
        contador = 0
        while(aux is not None):
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if (aux2.info.nombre == pok):
                    contador += 1
                    break
                aux2 = aux2.sig
            aux = aux.sig
        return(contador)

    def busqueda_en_sublista(self, poke):
        aux = self.__inicio
        while(aux is not None):
            pos = None 
            pos = aux.sublista.busqueda(poke, "nombre")
            if(pos):
                print(aux.info.nombre)
            aux = aux.sig
    
    def cantidad_entrenadores_con_pokemon(self, poke):
        aux = self.__inicio
        contador = 0
        while(aux is not None):
            pos = None 
            pos = aux.sublista.busqueda(poke, "nombre")
            if(pos):
                contador += 1
            aux = aux.sig


    def barrido_Tyrantrum_Wingull_Terrakion(self):
        aux = self.__inicio
        while(aux is not None):
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if ((aux2.info.nombre == "tyrantrum") or (aux2.info.nombre == "wingull") or (aux2.info.nombre == "terrakion")):
                    print(aux.info.nombre)
                    break
                aux2 = aux2.sig
            aux = aux.sig

    def pokemones_repetidos(self):
        aux = self.__inicio
        while(aux is not None):
            vec_pokemons = []
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if (aux2.info.nombre in vec_pokemons):
                    print(aux.info.nombre)
                    break
                else:
                    vec_pokemons.append(aux2.info.nombre)
                aux2 = aux2.sig
            aux = aux.sig


#EJERCICIO 20
    def promedio_temperatura_mayo(self):
        acumulador = 0
        i = 0
        aux = self.__inicio
        while(aux is not None):
            i += 1
            if(aux.info.fecha[3] == "0" and aux.info.fecha[4] == "5"):
                acumulador = acumulador + aux.info.temperatura
            aux = aux.sig
        return acumulador / i

    def promedio_humedad_mayo(self):
        acumulador = 0
        i = 0
        aux = self.__inicio
        while(aux is not None):
            i += 1
            if(aux.info.fecha[3] == "0" and aux.info.fecha[4] == "5"):
                acumulador = acumulador + aux.info.humedad
            aux = aux.sig
        return acumulador / i

    def barrido_estacioes_nevando_lloviendo(self):
        aux = self.__inicio
        while(aux is not None):
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if (aux2.info.estado == "lloviendo" or aux2.info.estado == "nevando"):
                    print(aux.info.pais)
                    break
                aux2 = aux2.sig
            aux = aux.sig

    def barrido_estacioes_huracan_tormElectrica(self):
        aux = self.__inicio
        while(aux is not None):
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if (aux2.info.estado == "huracan" or aux2.info.estado == "tormenta electrica"):
                    print(aux.info.pais)
                    break
                aux2 = aux2.sig
            aux = aux.sig    


    def barrido_alumnos_aprobados(self):
        aux = self.__inicio
        while(aux is not None):
            aprobado = True
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if (aux2.info.nota < 6):
                    aprobado = False
                    break
                aux2 = aux2.sig
            if (aprobado):
                print(aux.info.nombre)
            else:
                print("el alumno", aux.info.nombre, "ha desaprobado al menos un parcial")
            aux = aux.sig    

    def promedio_mayor_8_89(self):
        aux = self.__inicio
        while(aux is not None):
            total_notas = 0
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                total_notas = total_notas + aux2.info.nota
                aux2 = aux2.sig
            if(total_notas / aux.sublista.tamanio() > 8.89):
                print(aux.info.nombre)
            aux = aux.sig    

    def alumnos_apellido_l(self):
        aux = self.__inicio
        while(aux is not None):
            if( aux.info.apellido[0] == "L"):
                print(aux.info)
            aux = aux.sig    


    def promedio_alumnos(self):
        aux = self.__inicio
        while(aux is not None):
            total_notas = 0
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                total_notas = total_notas + aux2.info.nota
                aux2 = aux2.sig
            print("promedio de ", aux.info.nombre, total_notas / aux.sublista.tamanio())
            aux = aux.sig    

    def alumnos_AyEDD(self):
        aux = self.__inicio
        while(aux is not None):
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if(aux2.info.materia == "algoritmos y estructuras de datos"):
                    print(aux.info.nombre)
                    break
                aux2 = aux2.sig
            aux = aux.sig    

    def porcentaje_aprobados(self):
        aux = self.__inicio
        contador_aprobados = 0
        while(aux is not None):
            if(aux.info.nota >= 6):
                contador_aprobados += 1
            aux = aux.sig
        porcentaje = (contador_aprobados * 100) / self.tamanio()
        return porcentaje

    def aprobados_desaprobados_bases_de_datos(self):
        aux = self.__inicio
        contador_aprobados = 0
        contador_desaprobados = 0
        while(aux is not None):
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if (aux2.info.materia == "base de datos"):
                    if(aux2.info.nota >= 6):
                        contador_aprobados += 1
                    else:
                        contador_desaprobados += 1
                    break
                aux2 = aux2.sig
            aux = aux.sig
        print("cantidad de alumnos que aprobaron base de datos", contador_aprobados)
        print("cantidad de alumnos que desaprobaron base de datos", contador_desaprobados)

    def alumnos_rindieron_2020(self):
        aux = self.__inicio
        while(aux is not None):
            aux2 = aux.sublista.__inicio
            while (aux2 is not None):
                if (aux2.info.fecha[6] == "2" and aux2.info.fecha[7] == "0" and aux2.info.fecha[8] == "2" and aux2.info.fecha[9] == "0"):
                    print(aux.info)
                    break
                aux2 = aux2.sig
            aux = aux.sig