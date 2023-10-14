cadena1 = "hola, Mike"
cadena2 = "JOSE"

#dir - (funcions ) devuelve la lista de atributos validos del objeto que se le pasa
resultado = dir(cadena1)

#upper (metodo) es un metodo que convierte a mayuscula
resultado = cadena1.upper()

#lower , es un metodo para convertir a minusculas
resultado2 = cadena2.lower()

#Capitalize, metodo que solo deja la primera letra en mayuscula
resultado3 = cadena2.capitalize()

#find, buscamos una cadena dentro de otra, nos devuelve la posicion en la que esta posicionada. 

#----- si no encuentra nada, coincidencias, devuelve -1
busqueda_find = cadena1.find("a")

#----- en caso de no encontrar una coincidencia devuelve una excepcion.
busqueda_index = cadena1.index("a")

#isNumeric, si es numerico devuelve True,sino, false
es_numerico = cadena1.isnumeric()

# isalpha, si es alfanumerico devolvemos true, sino, false
#verifica que solo haya valores de la A hasta la Z, sin espacios etc.
es_alfanumerico = cadena1.isalpha()

#count, devuelve la cantidad de veces que coinciden en la variable.
contar_coincidencias = cadena1.count("a")

#len,(funcion) cuenta la cantidad de caracteres de una cadena 
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena, con una letra en especifico
empieza_con = cadena1.startswith("H")

#verifica con que letra o letras termina la cadena de texto
termina_con = cadena1.endswith("ke")

#reemplaza un pedaso de cadena , por otra, si se encuentra
cadena_nueva = cadena1.replace("hola","hola wu")

#metodo especial,separar cadenas con la cadena que le pasemos, ejemplo:
#por cada coma que encuentre es un valor, y devuelve un arreglo con todos los valores que encuentre .
separar_cadena = cadena1.split(",")
print(separar_cadena)

