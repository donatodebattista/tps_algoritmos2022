class nodoCola():
    info, sig = None, None


class Cola():

    def __init__(self):
        self.__frente = None
        self.__final = None
        self.__tamnio = 0

    def arribo(self, dato):
        nodo = nodoCola()
        nodo.info = dato

        if self.__final is None:
            self.__frente = nodo
        else:
            self.__final.sig = nodo
        self.__final = nodo

        self.__tamnio += 1

    def atencion(self):
        dato = self.__frente.info

        self.__frente = self.__frente.sig
        if self.__frente is None:
            self.__final = None

        self.__tamnio -= 1
        return dato

    def tamanio(self):
        return self.__tamnio

    def cola_vacia(self):
        return self.__frente is None

    def en_frente(self):
        return self.__frente.info

    def mover_al_final(self):
        dato = self.atencion()
        self.arribo(dato)
        return dato

    def barrido(self):
        aux = self.__frente
        while(aux is not None):
            print(aux.info)
            aux = aux.sig

    #Funciones ejercicio 18
    def barrido_turnos(self):
        aux = self.__frente
        while(aux is not None):
            print(aux.info.letra, aux.info.numero)
            aux = aux.sig
    
    def barrido_turnos_nro_mayor_506(self):
        aux = self.__frente
        while(aux is not None):
            if(int(aux.info.numero) > 506):
                print(aux.info.letra, aux.info.numero)
            aux = aux.sig
    

    def turnos_nro_mayor_506(self):
        while(not self.cola_vacia()):
            dato = self.atencion()
            numero = int(dato.numero)
            if(numero > 506):
                print(dato.letra, dato.numero)

    def letra_con_mas_turnos(self, letras): #letras es un vector que va a contener las letras de cada cola
        cont_0 = 0
        cont_1 =0
        cont_2 = 0
        while(not self.cola_vacia()):
            dato = self.atencion()
            if (dato.letra == letras[0]):   #Calcular cantidad de turnos por letra
                cont_0 += 1
            elif(dato.letra == letras[1]):
                cont_1 += 1
            else:
                cont_2 += 1
        print("Cantidad de turnos de la letra", letras[0],":" ,cont_0)
        print("Cantidad de turnos de la letra", letras[1],":" ,cont_1)
        print("Cantidad de turnos de la letra", letras[2],":" ,cont_2)

        
        contadores = [cont_0, cont_1, cont_2]

        if(cont_0 != cont_1 and cont_1 != cont_2 and cont_2 != cont_0):  #Evaluar cual letra tiene mas turnos
            if(cont_0 == max(contadores)):
                return letras[0]
            elif(cont_1 == max(contadores)):
                return letras[1]
            else:
                return letras[2]
        elif(cont_0 == cont_1 and cont_1 == cont_2 and cont_2 == cont_0):
            return(letras[0], letras[1], letras[2])
        else:
            if(cont_0 == cont_1):
                if cont_0 == max(contadores):
                    return (letras[0], letras[1])
                else:
                    return letras[2]
            elif(cont_0 == cont_2):
                if cont_0 == max(contadores):
                    return (letras[0], letras[2])
                else:
                    return(letras[1])
            else:
                if(cont_1 == max(contadores)):
                    return(letras[1], letras[2])
                else:
                    return(letras[0])

    #Funciones ejercicio22
    def personaje_de(self, superheroe):
        aux = self.__frente
        while(aux is not None):
            if (aux.info.nombre_superheroe == superheroe):
                return(aux.info.nombre_personaje)
            aux = aux.sig

    def barrido_personajes_femeninos(self):
        aux = self.__frente
        while(aux is not None):
            if (aux.info.genero == "F"):
                print("-", aux.info.nombre_superheroe)
            aux = aux.sig

    def barrido_personajes_masculinos(self):
        aux = self.__frente
        while(aux is not None):
            if (aux.info.genero == "M"):
                print("-", aux.info.nombre_personaje)
            aux = aux.sig

    def superheroe_de(self, personaje):
        aux = self.__frente
        while(aux is not None):
            if (aux.info.nombre_personaje == personaje):
                return(aux.info.nombre_superheroe)
            aux = aux.sig
    
    def barrido_letra_s(self):
        aux = self.__frente
        while(aux is not None):
            if (aux.info.nombre_personaje[0] == "S" or aux.info.nombre_superheroe[0] == "S"):
                print("-", aux.info)
            aux = aux.sig
    
            
                


