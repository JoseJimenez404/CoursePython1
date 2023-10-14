otros_cursos_min = 2.5
otros_cursos_max = 7

otros_cursos_promedio = 4
micurso = 1.5

#diferencias de duracion

#aca vamos a obtener cuanto equivale mi curso a el total del otro curso
# diferencia_con_min = micurso/otros_cursos_min * 100
#ahora, cuando le ponemos el 100 antes, obtenemos la diferencia entre ellos.
diferencia_con_min = 100 - micurso/otros_cursos_min * 100

diferencia_con_max = 100 - micurso *1000 // otros_cursos_max/10

diferencia_con_promedio = 100 - micurso / otros_cursos_promedio * 100

print(diferencia_con_min)
print(diferencia_con_max)
print(diferencia_con_promedio)

print(f'mi curso dura un {diferencia_con_min}% menos que el mas rapido')