#Definiendo una variable 
#usar Snike, es decir usando guiones bajos
name = "mike"

#concatenar con +
bienvenida = "hola" + name

#concatenar con f-strings
bienvenida = f" hola {name} ¿como estas ?"

#del es un operador para borrar datos
del bienvenida
print(bienvenida)


#operadores de pertenencia (in - not in)
print("hola" in bienvenida) #aqui pregutamos si la palabra hola existe
print("hola" not in bienvenida) #aqui pregutamos si la palabra hola no existe