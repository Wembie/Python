#Punto 1
numero = 0
while numero != -1:
    numero = int( input( "Digite un numero: " ) )
    if numero >= 0 and numero <= 10:  
        print( numero, end = " " )
        for i in range( numero ):
            print( "*", end = "" )
        print( "\n" )    

#Punto 3
sumaNotasTotal = 0
n = int( input( "Digite la cantidad de cursos: " ) )
for curso in range( n ):
    sumaNotasCurso = 0
    m = int( input( f"Digite la cantidad de estudiantes del curso { curso + 1 }: " ) )
    for estudiante in range( m ):
        nombreEstudiante = input( f"Digite el nombre del estudiante { estudiante + 1 } del curso { curso + 1 }: " )
        nota = float( input( f"Digite la nota de { nombreEstudiante }: ") )
        sumaNotasCurso += nota
    sumaNotasTotal += sumaNotasCurso
    print( f"Sumas de las notas del curso { curso + 1 } es de: { sumaNotasCurso }" )
print( f"Suma total de las notas de todos los cursos es de: { sumaNotasTotal }" )