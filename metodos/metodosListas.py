#list, (funcion) crea una lista con list
lista = list(["jose","mike"])
messi = [2,6,8,9,1,5]

#len, cuanta los elementos
cadena = "hola"
resultado = len(lista) # devuelve la cantidad de elementos de la lista

#agregar un elemento a una lista con append
numeros = [1,2,3,4,5]
numeros.append(10)

#agregando un elemento a la lista en un indice en especifico
lista.insert(2,"Jose")

#agregando varias elementos a una lista, una lista
lista.extend([5,8])

#eliminando un elemento de la lista, por su indice
#si pones -1, elimina el ultimo elemento, -2 el anteultimo y asi  sucecivamente
lista.pop(0)

#removiendo un elemento de la lista por su valor, si lo encuentra lo elimina, sino, devuelve una excepcion
lista.remove("Jose")

#eliminando todos los elementos de una lista
numeros.clear()

#sort, ordena los elementos de manera ascendente, solo con NUMEROS
messi.sort()

#reverse, cambia el orden , lo ordena de reversa
messi.reverse()

print(lista)
print(numeros)
print(messi)
