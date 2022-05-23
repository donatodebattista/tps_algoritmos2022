from modulo_pila import Pila

pila_peliculas = Pila()
pila_peliculas_aux = Pila()
vec_peliculas_2014 = []
contador_peliculas_2018 = 0
vec_marvel_2016 = []

pelicula1 = {"titulo": "Avengers End Game", "estudio": "Marvel Studios", "anio": 2018}
pelicula2 = {"titulo": "Thor Ragnarok", "estudio": "Marvel Studios", "anio": 2018}
pelicula3 = {"titulo": "Spiderman homecomming", "estudio": "Marvel Studios", "anio": 2014}
pelicula4 = {"titulo": "Iron Man", "estudio": "Marvel Studios", "anio": 2016}
pelicula5 = {"titulo": "Black Widow", "estudio": "Marvel Studios", "anio": 2016}
pelicula6 = {"titulo": "Shrek", "estudio": "Dreamworks", "anio": 2018}
pelicula7 = {"titulo": "Avatar", "estudio": "Century Fox", "anio": 2014}
pelicula8 = {"titulo": "Doctor Strange", "estudio": "Marvel Studios", "anio": 2016}
pelicula9 = {"titulo": "Hulk", "estudio": "Marvel Studios", "anio": 2018}
pelicula10 = {"titulo": "Red", "estudio": "Disney", "anio": 2022}



pila_peliculas.apilar(pelicula1)
pila_peliculas.apilar(pelicula2)
pila_peliculas.apilar(pelicula3)
pila_peliculas.apilar(pelicula4)
pila_peliculas.apilar(pelicula5)
pila_peliculas.apilar(pelicula6)
pila_peliculas.apilar(pelicula7)
pila_peliculas.apilar(pelicula8)
pila_peliculas.apilar(pelicula9)
pila_peliculas.apilar(pelicula10)


def peliculas_estrenadas_en(pelicula, año): 
    if (pelicula["anio"] == año):
        return True
    else:
        return False

def menu():
    print("---------------------------------------------------------------------")
    print("1. mostrar los nombre películas estrenadas en el año 2014")
    print("2. indicar cuántas películas se estrenaron en el año 2018")
    print("3. mostrar las películas de Marvel Studios estrenadas en el año 2016")
    print("---------------------------------------------------------------------")
    return int(input("ELIJA UNA OPCION: "))
    
    
while True:
    vec_peliculas_2014 = []
    contador_peliculas_2018 = 0
    vec_marvel_2016 = []

    opcion = menu()

    if (opcion > 0) and (opcion < 4):

        if( opcion == 1):
            while(not pila_peliculas.pila_vacia()):
                dato = pila_peliculas.desapilar()

                if (peliculas_estrenadas_en(dato, 2014)):
                    vec_peliculas_2014.append(dato["titulo"])
                pila_peliculas_aux.apilar(dato)

            if(len(vec_peliculas_2014) == 0):
                print("No hay peliculas del año 2014")
            else:
                print("PELICULAS ESTRENADAS EN 2014: ")
                for i in range(len(vec_peliculas_2014)):
                    print("-", vec_peliculas_2014[i])

        elif(opcion == 2):
            while(not pila_peliculas.pila_vacia()):
                dato = pila_peliculas.desapilar()

                if (peliculas_estrenadas_en(dato, 2018)):
                    contador_peliculas_2018 += 1
                pila_peliculas_aux.apilar(dato)

            print("En 2018 se estrenaron", contador_peliculas_2018, "peliculas")

        elif(opcion == 3):
            while(not pila_peliculas.pila_vacia()):
                dato = pila_peliculas.desapilar()

                if (peliculas_estrenadas_en(dato, 2016) and (dato["estudio"] is "Marvel Studios")):
                    vec_marvel_2016.append(dato["titulo"])
                pila_peliculas_aux.apilar(dato)
            
            if(len(vec_marvel_2016) == 0):
                print("No hay peliculas de Marvel Studios estrenadas en 2016")
            else:
                print("PELICULAS DE MARVEL STUDIOS ESTRENADAS EN 2016: ")
                for i in range(len(vec_marvel_2016)):
                    print("-", vec_marvel_2016[i])


    while(not pila_peliculas_aux.pila_vacia()):
        dato2 = pila_peliculas_aux.desapilar()
        pila_peliculas.apilar(dato2)    

    print("--------------------------------------")
    continuar = input ("Desea ingresar otra opcion? s/n ")
    if (continuar is "n"): 
        break
    