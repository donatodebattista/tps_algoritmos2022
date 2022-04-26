''' Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
y que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo. '''
#Primero filas (y) despues columnas(x)

from pickle import TRUE


matriz_laberinto = [
    [' ', '#', '#', '#', '#', '#', '#', "#"],       # ' ' Espacios libres
    [' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],       # '#' Paredes 
    ['#', ' ', '#', ' ', '#', '#', ' ', '#'],       # 'l' llegada
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#'],       # 'c' camino
    ['#', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', '#', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', "l"],
]

matriz_laberinto2 = [
    [' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],       
    [' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#'],        
    ['#', ' ', '#', ' ', '#', '#', ' ', '#', '#', ' ', '#'],       
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#'],      
    ['#', '#', '#', ' ', ' ', ' ', '#', '#', ' ', '#', '#'],    
    [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', '#', ' ', '#', '#', '#', '#', "#", '#', '#', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' '],
    ['#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' '],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', "l"],
]

def salida_del_laberinto (x, y, laberinto):
    if (laberinto[x][y] == 'l'):
        return True

    elif (laberinto[x][y] != "#" and laberinto[x][y] != "c"):
        laberinto[x][y] = "c"

        if (x != len(laberinto)-1):
            if (salida_del_laberinto(x + 1, y, laberinto)):
                return True

        if (y != len(laberinto)-1):
            if salida_del_laberinto(x, y + 1, laberinto):
                return True

        if (x != 0):
            if salida_del_laberinto(x - 1, y, laberinto):
                return True 

        if (y != 0):
            if salida_del_laberinto(x, y - 1, laberinto): 
                return True
            else:
                laberinto[x][y] = " "
    
        else:
            laberinto[x][y] = " "
    else:
        return False
    
salida_del_laberinto (0, 0, matriz_laberinto2)



for i in range (0, len(matriz_laberinto2)):
    print(matriz_laberinto2[i])

