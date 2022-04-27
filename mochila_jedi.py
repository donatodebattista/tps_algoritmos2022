vector_mochila = ["baston", "casco trooper", "sable de luz", "capa"]

print(" ")
print("MOCHILA:", vector_mochila)
print(" ")


cantidad_de_objetos = len(vector_mochila)


def usar_la_fuerza(mochila):
    if (len(mochila) == 0):
        return (False)

    elif(mochila[0] == "sable de luz"):
        return (True)
    
    else:
        del mochila[0] 
        return usar_la_fuerza(mochila)



if (usar_la_fuerza(vector_mochila)):
    print("Se ha encontrado un sable de luz")
    print("Fue necesario sacar", cantidad_de_objetos - len(vector_mochila), "objeto/s para encontrarlo")
    print(" ")
else:
    print("La mochila no contenia un sable de luz")
    print(" ")
