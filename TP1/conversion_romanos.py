valores = {"I" : 1, "V": 5, "X": 10, "L" : 50, "C": 100, "D": 500, "M": 1000}

numero = "XXI"


def convertir_numero_romano(cadena, indice):
    if indice == len(cadena)-1:
        return valores[cadena[indice]]
    elif (valores[cadena[indice]] >= valores[cadena[indice +1]]):
        return valores[cadena[indice]] + convertir_numero_romano(cadena, indice+1)
    else:
        return - valores[cadena[indice]] + convertir_numero_romano(cadena, indice+1)


print (convertir_numero_romano(numero, 0))