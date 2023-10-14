#not
#el not antes de un False o True invierte el valor
resultado = not True #devuelve Falso
resultado = not False #devuelve True


#sistema que le de permiso a pablito para salir a la fiesta, tiene que barrer y trapear:

barrer = False
trapear = False

if barrer and trapear:
    print("¡Me impresionas, puedes ir a jugar!")
elif barrer or trapear:
    if barrer:
        print("Lo siento, te falta trapear, no puedes salir a jugar.")
    else:
        print("Lo siento, te falta barrer, no puedes salir a jugar.")
else:
    print("No te hagas el tonto, no hiciste nada, sal de aquí.")
