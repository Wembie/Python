sueldo_enero = 500
sueldo_febrero = 480
sueldo_marzo = 525
sueldo_trimestre = sueldo_enero+sueldo_febrero+sueldo_marzo
print ("El sueldo del trimestre es", sueldo_trimestre)

a = 83
b = 11
suma = a + b
resta = a - b
multiplicacion = a * b
division_entera = a // b
division_flotante = a / b
potencia = a ** b
modulo = a % b
print ("Suma:", suma, "Resta:", resta, "Multiplicacion:", multiplicacion, "Division Entera:", division_entera, "Division Flotante:", division_flotante, "Potencia:", potencia, "Modulo:", modulo)

nombre = input ("Write your name: ")
edad = int (input("Write your age: ")) #Se vuelve un numero entero es decir para hacer operaciones
estatura = float (input("Write your height: ")) #Se vuelve numero con decimales
print ("Su nombre es", nombre,".", "Su edad es", edad,".", "Su estatura es", estatura,".")

if 5 > 3 :              #Condicional de si, entonces
    print ("Es mayor")
else :
    print ("Es menor")

Puntaje = float (input("Cuanto saco en la materia?: "))   #Preguntando con variables
print ("Usted saco", Puntaje)
if Puntaje >= 3 :
    print ("Es decir, que Gano la materia")
else :
    print ("Es decir, que Perdio la materia")

#Ejercicio 1.1

Nombre = input ("Digite su nombre: ")
print ("Su nombre es", Nombre)
Nombrecito = ("Juan")
if Nombre == Nombrecito :
    print ("Usted es el ganador!!!")
else :
    print ("Tu nombre podría ser mejor")

#Ejercicio 1.2

Numero_1 = float (input ("Digite el primer numero: "))
Numero_2 = float (input ("Digite el segundo numero: "))
print ("Los numero digitados son el", Numero_1, "y el", Numero_2)
if Numero_1 == Numero_2 :
    print ("Los Numeros elegidos son Iguales")
else :
    print ("Los Numero elegidos no son iguales")
if Numero_1 > Numero_2 :
    print ("El Numero 1 es mayor que el Numero 2")
else :
    print ("El Numero 1 es menor que el Numero 2")
if Numero_1 < Numero_2 :
    print ("El Numero 2 es mayor que el Numero 1")
else :
    print ("El Numero 2 es menor que el Numero 1")

#Ejercicio 1.3

Numero = int (input ("Dijite un numero entero del 1 al 7: "))
if Numero == 1 :
    print ("El dia de la semana que concuerda con el numero que elejiste fue Lunes")
if Numero == 2 :
    print ("El dia de la semana que concuerda con el numero que elejiste fue Martes")
if Numero == 3 :
    print ("El dia de la semana que concuerda con el numero que elejiste fue Miercoles")
if Numero == 4 :
    print ("El dia de la semana que concuerda con el numero que elejiste fue Jueves")
if Numero == 5 :
    print ("El dia de la semana que concuerda con el numero que elejiste fue Viernes")
if Numero == 6 :
    print ("El dia de la semana que concuerda con el numero que elejiste fue Sabado")
if Numero == 7 :
    print ("El dia de la semana que concuerda con el numero que elejiste fue Domingo")

#Ejercicio 1.4
    
Par = True
Impar = False
Numero = int (input ("Coloca un numero: "))
if Numero % 2 :
    print ("Es ", Impar, "donde False es = Impar")
else :
    print ("Es ", Par, "donde True es = Par")

#Ejercicio 2.1

Numero = float (input ("Digite un numero positivo o negativo: "))
a = 10
positivo = -1
if Numero > 0 :
    if Numero % 2 :
        print ("Su numero es Impar")
    else :
        print ("Su numero es", "(",Numero,")", "+ 10 es =", Numero+a)
        print ("Su numero es par")
else :
    print ("Su Numero es Negativo", "(",Numero,")", "x -1 da =", Numero*positivo)
    if Numero % 2 :
        print ("Su Numero es Impar")
    else :
        print ("Su Numero es Par")

#Ejercicio 2.2

Dinero = float (input("Digite el dinero para apostar: "))
print ("Su Dinero es: ",Dinero)
print ("Numeros Ganadores:")
import random
Numero_1 = random.randrange(0, 4)
Numero_2 = random.randrange(0, 4)
Numero_3 = random.randrange(0, 4)
print (Numero_1)
print (Numero_2)
print (Numero_3)
if Numero_1 == Numero_2 and Numero_2 == Numero_3 and Numero_1 == Numero_3 :
    print ("Ganaste!!!!(x3), Ahora tu dinero es: ",Dinero*3)
if Numero_1 == Numero_2 or Numero_2 == Numero_3 or Numero_1 == Numero_3 and Numero_1 == Numero_2 or Numero_2 == Numero_3 or Numero_1 == Numero_3 :
    print ("Ganaste!!!!(x2), Ahora tu dinero es: ",Dinero*1.5)
if Numero_1 != Numero_2 and Numero_2 != Numero_3 and Numero_1 != Numero_3 :
    print ("No Ganaste nada :c, Ahora tu dinero es: ",Dinero*0)

#Ejercicio 2.3

Numero = float (input ("Digite un numero positivo o negativo: "))
if Numero > 0 :
    print ("Es Positivo")
if Numero < 0 :
    if Numero > -10 :
        print ("Es Negativo Chiquito")
    else :
        print ("Es Negativo Grande")

#Ejercicio 2.4

Numero_1 = float (input ("Digite el Primer numero: "))
Numero_2 = float (input ("Digite el Segundo numero: "))
Numero_3 = float (input ("Digite el Tercer numero: "))
print ("Numero 1:", Numero_1)
print ("Numero 2:", Numero_2)
print ("Numero 3:", Numero_3)
if Numero_1 == Numero_2 and Numero_2 == Numero_3 and Numero_1 == Numero_3 :
    print ("Los numeros escogidos son iguales")
elif Numero_1 > Numero_2 and Numero_1 > Numero_3 :
    print ("El Mayor numero es el: ",Numero_1)
else :
    if Numero_2 > Numero_1 and Numero_2 > Numero_3 :
        print ("El Mayor numero es el: ",Numero_2)
    else :
        print ("El Mayor numero es el: ",Numero_3)

#Ejercicio 3.1

Numero = int(input("Digite un numero del 1 al 12: "))
if Numero == 1 or Numero == 3 or Numero == 5 or Numero == 7 or Numero == 8 or Numero == 10 or Numero == 12 :
    print ("Este mes tiene 31 dias")
if Numero == 4 or Numero == 6 or Numero == 9 or Numero == 11 :
    print ("Este mes tiene 30 dias")
if Numero == 2 :
        print ("Este mes tiene 28 dias")
elif Numero > 12 or Numero < 1 :
        print ("lo siento el número no corresponde a un mes del año")

#Ejercicio 3.2

print ("Banco Usereros Asociados")
Prestamo = int(input("Digite el prestamo a pedir: "))  #5/100 = 0,05
print ("Prestamo pedido: ",Prestamo)
a = Prestamo*0.05
b = Prestamo*0.10
c = Prestamo*0.15
a1 = Prestamo+a
b1 = Prestamo+b
c1 = Prestamo+c
if Prestamo < 500000 :
    print ("Tasa insteres del 5% en 6 meses, su valor a cancelar es de: ",Prestamo ,"+" ,a, "=", a1)
    print ("(Cuota Mensual a pagar)")
    print ("Primer Mes: ",a1)
    print ("Segundo Mes: ",a1)
    print ("Tercer Mes: ",a1)
    print ("Cuarto Mes: ",a1)
    print ("Quinto Mes: ",a1)
    print ("Sexto Mes: ",a1)
    print ("Valor total: ",a1*6)
if Prestamo >= 500000 and Prestamo < 2000000 :
    print ("Tasa de interes 10% en 12 meses, su valor a cancelar de es: ",Prestamo ,"+" ,b, "=", b1)
    print ("(Cuota Mensual a pagar)")
    print ("Primer Mes: ",b1)
    print ("Segundo Mes: ",b1)
    print ("Tercer Mes: ",b1)
    print ("Cuarto Mes: ",b1)
    print ("Quinto Mes: ",b1)
    print ("Sexto Mes: ",b1)
    print ("Septimo Mes: ",b1)
    print ("Octavo Mes: ",b1)
    print ("Noveno Mes: ",b1)
    print ("Decimo Mes: ",b1)
    print ("Onceavo Mes: ",b1)
    print ("Doceavo Mes: ",b1)
    print ("Valor total: ",b1*12)
if Prestamo > 2000000 :
    print ("Tasa de interes del 15% en 2 años, su valor a cancelar de es: ",Prestamo ,"+" ,c, "=", c1)
    print ("(Cuota Mensual a pagar)")
    print ("Primer año: ",c1*12)
    print ("Segundo año: ",c1*12)
    print ("Valor total: ",c1*24)


#Ejercicio 3.3

Numero = int(input("Digite un numero del 1 al 12: "))
if Numero == 1 :
    print("De acuerdo al numero escogido su mes es: Enero")
if Numero == 2 :
    print("De acuerdo al numero escogido su mes es: Febrero")
if Numero == 3 :
    print("De acuerdo al numero escogido su mes es: Marzo")
if Numero == 4 :
    print("De acuerdo al numero escogido su mes es: Abril")
if Numero == 5 :
    print("De acuerdo al numero escogido su mes es: Mayo")
if Numero == 6 :
    print("De acuerdo al numero escogido su mes es: Junio")
if Numero == 7 :
    print("De acuerdo al numero escogido su mes es: Julio")
if Numero == 8 :
    print("De acuerdo al numero escogido su mes es: Agosto")
if Numero == 9 :
    print("De acuerdo al numero escogido su mes es: Septiembre")
if Numero == 10 :
    print("De acuerdo al numero escogido su mes es: Octubre")
if Numero == 11 :
    print("De acuerdo al numero escogido su mes es: Noviembre")
if Numero == 12 :
    print("De acuerdo al numero escogido su mes es: Diciembre")
elif Numero > 12 or Numero < 1 :
        print ("lo siento el número no corresponde a un mes del año")

#Ejercicio 3.4

X = 11
Y = 9
Z = 10
W = 4

if Y + W > Z :
    print("True")
if X*W+Y-W or W*X+W-Z:
    print ("False")

#Ejercicios del 4 Valieron verga xD

#Ejercicio 1.1

Numero = 0
while Numero <= 7 :
    print (Numero)
    Numero = Numero + 1

#Ejercicio 1.2

Numero = 23
while Numero >= -7 :
    print (Numero)
    Numero = Numero -6

#Ejercicio 1.3

Numero = 10
while Numero >= 0 :
    print (Numero)
    Numero = Numero -1

#Ejercicio 1.4

Numero = 12
while Numero <= 34 :
    print (Numero)
    Numero = Numero + 2

#Ejercicio 1.5

Numero = 3
while Numero <= 50 :
    print (Numero)
    Numero = Numero + 3

#Ejercicio 1.6

Numero = 0
while Numero <= 100 :
    if Numero % 3 ==0 and Numero % 4 ==0 :
        print (Numero)
    Numero = Numero + 1
        
#Ejercicio 1.7

Numero = 50
while Numero <= 65 :
    print (Numero) 
    Numero = Numero + 1

#Ejercicio 2.1

N = float (input ("Digite el numero de 'N': " ))
K = 1
while K <= N :
    print (K ** 2)
    K = K + 1

#Ejercicio 2.2

Numero = 10
N = 1
Suma = 0
while N <= Numero :
    Suma = Suma + ((N**3)+(N)+(2))
    N = N + 1
print ("Resulado de la suma es:",Suma)

#Ejercicio 2.3

Numero = 1
Suma = 0
while Numero <=28 :
    print (Numero)
    Suma = Suma+Numero
    Numero = Numero + 2
print (Numero)

#Ejercicio 2.4

Numero_1 = int(input("Digite el Numero 1 [Cualquiera]: "))
Numero_2 = int(input("Digite el Numero 2 [Cualquiera]: "))
Numero_3 = int(input("Digite el Numero 3 [Cualquiera]: "))
Numero_4 = int(input("Digite el Numero 4 [Cualquiera]: "))
Numero_5 = int(input("Digite el Numero 5 [Cualquiera]: "))
Numero_6 = int(input("Digite el Numero 6 [Cualquiera]: "))
Numero_7 = int(input("Digite el Numero 7 [Cualquiera]: "))
Numero_8 = int(input("Digite el Numero 8 [Cualquiera]: "))
Numero_9 = int(input("Digite el Numero 9 [Cualquiera]: "))
Numero_10 = int(input("Digite el Numero 10 [Cualquiera]: "))
print ("La suma de los numeros digitados da:", Numero_1+Numero_2+Numero_3+Numero_4+Numero_5+Numero_6+Numero_7+Numero_8+Numero_9+Numero_10)

########################################################
### Forma con while (CICLOOOOOOOOOOOOOOOOOOOOOOOOOO) ###
########################################################

Suma = 0
Inicio = 1
Limite = 10
while Inicio <= Limite :
    Numero_N = int(input("Digite un Numero [Cualquiera]: "))
    Suma = Suma + Numero_N
    Inicio = Inicio + 1
print ("La suma de los numeros digitados da: ", Suma)

#Ejercicio 2.5

Suma = 0
Inicio = 1
Trabajadores = int(input("Digite el numero de trabajadores: "))
while Inicio <= Trabajadores :
    Nombre = input("Digite su Nombre: ")
    Edad = int(input("Digite su Edad: "))
    Salario = float(input("Digite su Salario: "))
    Gasto_Mensual = float(input("Digite su Gasto Mensual: "))
    Suma = Suma + (Salario - Gasto_Mensual)
    Inicio = Inicio + 1
print ("El salario restante es de todos los trabajadores: ", Suma)

#Ejercicio 2.6 VALE VERGA XD

#Ejercicio 3.1

Numero = 0
while Numero != 7 :
    Numero = int(input("Dijite un numero entre el 1 y el 10: "))
    if Numero < 1 or Numero > 10 :
        print ("El numero no esta en el rango")
    elif Numero == 7 :
        print ("Acertaste!!!!, el numero era el 7")
    else :
        print ("Vuelve a intentarlo")

#Ejercicio 3.2
        
Suma_par = 0
Suma_impar = 0
Numero = 1
while Numero != 0 :
    Numero = int (input ("Digite un numero: "))
    if Numero %2==0 :
        Suma_par = Suma_par + 1
    else :
        Suma_impar = Suma_impar +1
print ("Numero total escritos pares son: ",Suma_par)
print ("Numero total escritos impares son: ",Suma_impar)

#Ejercicio 3.3

import random
Aleatorio = random.randrange(0,101)
#print (Aleatorio) Para saber cual numero aleatorio sale quita el #
Numero = 0
Fallo = 0
while Numero != Aleatorio :
    Numero = int ( input("Digite un numero del 0 al 100: "))
    if Numero > Aleatorio :
        print ("El Numero digitado es mayor al que buscas")
        Fallo = Fallo + 1
    elif Numero < 0 or Numero > 100 :
        print ("El Numero digitado no esta dentro del rango")
    else :
        print ("El Numero digiado es menor al que buscas")
        Fallo = Fallo + 1
print ("Has acertado el numero!... que era: ",Numero)
print ("El total de veces falladas es de: ", Fallo)

#Ejercicio 3.4

Numero = 0
Suma = 0
Total = 0
while Numero != -1 :
    Numero = int (input ("Digite un numero: "))
    Suma = Suma + Numero
    Total = Total + 1
print ("La suma de todos los numeros digitados fue de: ",Suma)
print ("El total de numero ingresados fueron de: ",Total)

#Ejercicio 3.5

Numero = 0
Total = 0
Suma = 0
while Numero != -1 :
    Numero = int (input ("Digite un numero: "))
    Suma = Suma + Numero
    Total = Total + 1
print ("El promedio de numeros ingresados fueron de: ",Suma/Total)

#Ejercicio 4.1

Numero = 0
Inicio = 1
Bandera = 0
while Inicio <= 10 :
    Numero = int (input("Digite un numero: "))
    print ("Su numero digitado fue el: ",Numero)
    Inicio = Inicio + 1
    if Numero == 5 and Bandera == 0 :
        print ("Has sido Felicidado por este crack del Wembie papu!")
        Bandera = 1
print ("Has Terminado gracias por participar socito :v")


#Ejercicio 4.2

Bandera = 0
Numero = 1
while Numero != 0 :
    Numero = int (input ("Digite un numero: "))
    if Numero == 2 and Bandera == 0 :
        print ("Que buen numero")
        Bandera = 1
    elif Numero == 2 and Bandera == 1 :
        print ("Buena idea")
        Bandera = 2
print ("Has Terminado gracias por participar socito :v")


#Ejercicio 5.1

Indice = 1
Multiplicar = 1
N = int(input("Digite el valor de N: "))
while Indice < N :    
    Indice = Indice + 1
    Multiplicar *= Indice #ESTO ES IGUAL AH = Multiplicar = Multiplicar * Indice
    print (Multiplicar)


#Ejercicio 5.2 y 5.3

Numero = int(input("Digite un numero, socio: "))
def Primo(Numero):
    if Numero < 1 :
        return False
    elif Numero == 2 :
        return True
    else:
        for i in range(2, Numero):
            if Numero % i == 0:
                return False
        return True
Resultado = Primo(Numero)
if Resultado is True :
    print ("Es un Numero Primo")
else :
    print ("No es un Numero Primo")

#Ejercicio 5.4

Inicio = 1
N = int(input("Digite el valor de N: "))
while Inicio < N :
    Resultado = Primo(Inicio)
    if Resultado is True :
        print (Inicio)
    Inicio += 1

#Ejercicio 6.1

Mayor = 0
Menor = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Indice = 1
while Indice <= 10 :
    Numero = int(input("Digite un numero: "))
    print ("Numero digitado es: ",Numero)
    Indice += 1
    if Numero > Mayor :
        Mayor = Numero
print ("El numero mayor de los numeros digitados es el: ",Mayor)

#Ejercicio 6.2

Mayor = 0
Menor = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Indice = 1
while Indice <= 10 :
    Numero = int(input("Digite un numero: "))
    print ("Numero digitado es: ",Numero)
    Indice += 1
    if Numero > Mayor :
        Mayor = Numero
    if Numero < Menor :
        Menor = Numero
print ("El numero mayor de los numeros digitados es el: ",Mayor)
print ("El numero menor de los numeros digitados es el: ",Menor)

#Ejercicio 6.3


Mayor = 0
Menor = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Numero = 0
while Numero != -1 :
    Numero = int(input("Digite un numero: "))
    print ("Numero digitado es: ",Numero)
    if Numero > Mayor :
        Mayor = Numero
    if Numero < Menor :
        Menor = Numero
print ("El numero mayor de los numeros digitados es el: ",Mayor)
print ("El numero menor de los numeros digitados es el: ",Menor)

#Ejercicio 6.4

Nombre_Mayor = ""
Nombre_Menor = ""
Mayor = 0
Menor = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Indice = 1
while Indice <= 10 :
    Nombre = input("Digite el Nombre del usuario: ")
    Numero = int(input("Digite la nota del estudiante: "))
    print ("El nombre del usuario digitado es:",Nombre)
    print ("La nota del estudiante es:",Numero)
    Indice += 1   
    if Numero > Mayor :
        Mayor = Numero
        Nombre_Mayor = Nombre
    if Numero < Menor :
        Menor = Numero
        Nombre_Menor = Nombre
print ("El nombre que saco la mayor nota es de: ",Nombre_Mayor, ",y la nota fue de: ",Mayor)
print ("El nombre que saco la menor nota es de: ",Nombre_Menor, ",y la nota fue de: ",Menor)

########################
###EJERCICIO PAL QUIZ###
########################

Total = 0
Suma = 0
Bandera = 0
Numero = 0
while Numero != -1 :
    Numero = int (input ("Digite un numero: "))
    if Numero == 5 and Bandera == 0 :
        print ("Felicidades")
        Bandera = 1
        Total -= 1
    elif Numero == 5 and Bandera == 1 :
        print ("Felicidades y ven mañana por el premio")
        Bandera = 2
        Total -= 1
    elif Numero == 5 and Bandera == 2 :
        print ("Esta muy sospechoso!!")
        Bandera = 3
        Total -= 1
    if Numero < 1 or Numero > 30 :
        print ("El numero esta fuera del rango manito, esta mal digitado")
    Suma += 1
    Total += 1 
print ("El numero de veces que digitaste fue de: ",Suma)
print ("El promedio de numeros digitados sin tener el encuenta los del 5 son: ",Suma/Total)
print ("Has Terminado gracias por participar socito :v")

#Ejercicio 6.5

Numero = 0
Menor = 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
while Numero != -1 :
    Numero = int (input ("Digite un numero: "))
    if Numero < Menor and Numero % 3 ==0 :
        Menor = Numero
        print (Numero)
        print ("Es multiplo de 3")
    else :
        print (Numero)
        print ("No es multiplo de 3")
print ("El numero menor y multiplo de 3 es: ",Menor)

#Ejercicio 6.6

Numero = 0
Mayor = 0
Par = 0
Par1 = 0
FlagM = 0 # M = MAYOR
FlagN = 0 # N = MENOR
while Numero != -1 :
    Numero = int (input ("Digite un numero: "))
    if Numero > 50 and Numero % 2 == 0 :
        print (Numero)
    elif Numero < 50 and FlagM == 0 and Numero > 0 :
        print (Numero)
        FlagM = 1
    elif Numero > 50 and FlagN == 0 and Numero > 0  :
        print (Numero)
        FlagN = 1
    elif Numero > 50 :
        print (Numero)
    elif Numero < 50 :
        print (Numero)
    elif Numero % 3 == 0 and Par == 0 :
        print (Numero)
        Par = 1
    elif Numero % 2 == 0 and Par1 == 0 :
        print (Numero)
        Par1 = 1
    if Numero > Mayor :
        Mayor = Numero
if FlagM == 0 :
    print ("Tuve números grandes, pero ninguno era par")
elif FlagN == 0 :
    print ("Ningún número cumplía con las condiciones")
elif Par == 0 :
    print ("Lo siento el mayor no se puede encontrar,tuve pares pero no mayores a 50")
elif Par1 == 0 :
    print ("Ningún número cumplía con las condiciones")
print ("El mayor es: ",Mayor)

#Ejercicio 6.7

Suma = 0
Sum = 0
Indice = 0
Mayor = 0
Nombre_Mayor = ""
Trabajadores = int (input("Digite el numero de trabajadores en la fabrica: "))
while Indice < Trabajadores :
    Nombre = input("Digite el Nombre del trabajador: ")
    Edad = int(input("Digite la edad: "))
    Salario = int(input("Digite el salario: "))
    GastoM = int(input("Digite el gasto mensual: "))
    print ("El nombre del trabajador digitado es: ",Nombre)
    print ("La edad del trabajador es: ",Edad)
    print ("El salario del trabajador es: ",Salario)
    print ("El gasto mensual del trabajador es: ",GastoM)
    Indice += 1
    Suma += Salario
    Sum += GastoM
    if Salario > Mayor :
        Mayor = Salario
        Nombre_Mayor = Nombre
print ("El salario restantes es de todos los trabajadores: ",Suma-Sum)
print ("El empleado, ",Nombre_Mayor, ",tiene un mayor salario el cual es: ",Mayor)

#Ejercicio 7.1

Numero = 0
Indice = 0
Promedio = 0
Nota_3 = 0
Total = 0
N = int (input("Digite el numero de examenes en total: "))
while Indice < N :
    Numero = float (input("Digite la nota de el examen entre 0 y 5: ")) 
    if Numero > 3 :
        print ("Nota del examen: ",Numero)
        Nota_3 += 1
        Promedio += Numero
        Indice += 1
        Total += 1
    else :
        print ("Nota del examen: ",Numero)
        Promedio += Numero
        Indice += 1
        Total += 1
print ("cuantas notas fueron superiores a 3?: ",Nota_3," Veces, Y el promedio de las notas fue de: ",Promedio/Total)

#Ejercicio 7.2

Pisos = 0
Pisos_Total = 0
Valor = int(input("Digite el valor del primer piso: "))
Presupuesto = int(input("Digite el valor de la obra (Presupuesto): "))
while Pisos_Total < Presupuesto:        
    Pisos_Total = Valor*2
    Pisos +=1
    Valor *= 2
print ("Se pueden hacer", Pisos, "pisos en total")
    

#Ejercicio 7.3

Indice = 1
Pagar = 0
CopiaxHoja = 100
Tipo = input ("Digite el tipo de estudiante [Estudiante,Estudiante Becado,Profesor,Visitante,Colaborador]: ")
Clientes = int(input("Digite el numero de clientes: "))
Copias = int(input("Digite el numero de copias: "))

while Indice < Clientes :
    if Tipo == "Estudiante Becado" :
        CopiaxHoja = 50
        Pagar = CopiaxHoja*Copias
    else :
        Pagar = CopiaxHoja*Copias
    Indice +=1
print ("Total a pagar: ",Pagar)

#Ejercicio 7.4 VALEN VERGA

#EJERCICIOS DE CICLOS con for BY: Me

#1
for i in "DANIEL":
    print(f"Dame una {i}") # ESA F ANTES DE LAS " SIGNIFICA PARA COLOCAR LOS {} PARA DETERMINAR LA VARIABLE SIN LAS ,
print("¡DANIEL!")

#2
print("Comienzo")
for i in range(10):
    print("Hola ", end="")
print()
print("Final")

#3
veces = int(input("¿Cuántas veces quiere que le salude? "))
for i in range(veces):
    print("Hola ", end="")
print()
print("Adiós")

#4
print("Comienzo")
cuenta = 0
for i in range(1, 6):
    if i % 2 == 0:
        cuenta = cuenta + 1
print(f"Desde 1 hasta 5 hay {cuenta} múltiplos de 2")

#5
print("Comienzo")
suma = 0
for i in [1, 2, 3, 4]:
    suma = suma + i
print(f"La suma de los números de 1 a 4 es {suma}") 

    
#6 Ejercicio by Daniel

Contador = 0
for i in range(1,31) :
    if i % 3 == 0 :
        Contador += 1
print (f"Desde el 1 al 30 hay {Contador} multiplos de 3")

#

Contador_3 = 0
Contador_5 = 0
for i in range(1,31) :
    if i % 3 == 0 :
        Contador_3 += 1
    if i % 5 == 0 :
        Contador_5 += 1
print (f"Desde el 1 al 30 hay {Contador_3} multiplos de 3 y {Contador_5} multiplos de 5")

#

Cont = 0   
for i in "CASA":
    print(f"Dame una {i}")
    if i == "A":
        Cont += 1   
print("¡CASA!")
print (f"Las veces que se repite la A es {Cont}")

#EJERCICIO HECHO POR DANIEL DICTADO POR ME

CONT = 0
N = int(input("Digite hasta que numero va el rango: "))
for i in range (0,N):
    if i % 3 == 0:
        CONT += 1
print (f"Los multiplos de 3, de 0 hasta {N} son: {CONT}")
    
        
#Ejercicio normal

Cuantos_B = 0
Indice = 0
Bulto = 0
Bulto_N = 0
Provedores = int(input("Digite la cantidad de provedores: "))
while Indice < Provedores:
    Bulto_N = int(input("Digite el numero de bultos de naranja: "))
    if Bulto_N > 10 :
        Bulto = 28000
    else :
        Bulto = 25000
    Bulto *= Bulto_N
    Indice += 1
    Cuantos_B += Bulto_N
print (f"El Promedio de bultos de naranja es de {Bulto/Indice}, costaron {Bulto} y el total de bultos comprados son: {Cuantos_B}")

#ANIDADOS

N = 2
M = 3
Indice1 = 0
while Indice1 < N :
    Indice2 = 0
    while Indice2 < M :
        Indice2 += 1
    Indice1 += 1

#Ejercicio de las diapositivas

Altura = int(input("Digite la Altura: "))
Base = int(input("Digite la Base: "))
Indice1 = 0
while Indice1 < Altura :
    Indice2 = 0
    while Indice2 < Base :
        print ("X ",end="") #,end="" para que imprima al frente
        Indice2 += 1
    print ()
    Indice1 += 1

#por columnas

Altura = int(input("Digite la Altura: "))
Base = int(input("Digite la Base: "))
Indice1 = 0
while Indice1 < Altura :
    Indice2 = 0
    while Indice2 < Base :
        if Indice2 % 2 == 0 :
            print ("X ",end="")
        else :
            print ("Y ",end="") #,end="" para que imprima al frente
        Indice2 += 1
    print ()
    Indice1 += 1

#por filas

Altura = int(input("Digite la Altura: "))
Base = int(input("Digite la Base: "))
Indice1 = 0
while Indice1 < Altura :
    Indice2 = 0
    while Indice2 < Base :
        if Indice1 % 2 == 0 :
            print ("X ",end="") #,end="" para que imprima al frente
        else :
            print ("Y ",end="")
        Indice2 += 1
    print ()
    Indice1 += 1

#Otra
    
Altura = 5
Base = 10
Indice1 = 1
while Indice1 <= Altura :
    Indice2 = 1
    while Indice2 <= Base :
        if Indice1 == 3 :
            print ("O ",end = "")
        elif Indice2 == 9 :
            print ("O ",end = "")
        else:
            print ("X ",end = "")
        Indice2 += 1
    print ()
    Indice1 += 1

#################
### FUNCIONES ###
#################

def sumar (Valor1,Valor2):
    resultado = Valor1 + Valor2
    print (f"El resultado es: {resultado}")
#INVOCANDO
sumar(1,2)

#

a = 1
b = 2
def entiendo_ambito():
    c = 3
    print (f"El valor de c es: {c}")
print (f"El valor de a es: {a}")
print (f"El valor de b es: {b}")
entiendo_ambito()

####EJERCICIO####LARGO####


Opc = 1
Valor1 = int(input("Digite el valor #1: "))
Valor2 = int(input("Digite el valor #2: "))
def sumar (Valor1,Valor2):
    resultado = Valor1 + Valor2
    print (f"El resultado de la suma es: {resultado}")
def restar (Valor1,Valor2):
    resultado = Valor1 - Valor2
    print (f"El resultado de la resta es: {resultado}")
def multiplicar (Valor1,Valor2):
    resultado = Valor1 * Valor2
    print (f"El resultado de la multiplicacion es: {resultado}")
def dividir (Valor1,Valor2):
    if Valor2 == 0 :
        print("No se puede dividir por 0")
    else: 
        resultado = Valor1 / Valor2
        print (f"El resultado es: {resultado}")
def potencia (Valor1,Valor2):
    Base = int(input(f"Si quieres que la base sea {Valor1}, Digita [1], Si quieres que la base sea {Valor2}, Digita [2]"))
    if Base == 1 :
        Base = Valor1
    elif Base == 2 :
        Base = Valor2
    else:
        print("No se encuentra en el rango de 1 a 2")
    Potencia = int(input(f"Si quieres que la potencia sea {Valor1}, Digita [1], Si quieres que la potencia sea {Valor2}, Digita [2]"))
    if Potencia == 1 :
        Potencia = Valor1
    elif Potencia == 2 :
        Potencia = Valor2
    else:
        print("No se encuentra en el rango de 1 a 2")
    resultado = Base ** Potencia
    print (f"El resultado de la potencia es: {resultado}")
def mayor_o_igual (Valor1,Valor2):
    mayor = 0
    if Valor1 > Valor2 :
        mayor = Valor1
    elif Valor1 == Valor2 :
        print ("Son iguales")
    else:
        mayor = Valor2
    print (f"El mayor es: {mayor}")
def primo1(Valor1):
    if Valor1 < 1 :
        return False
    elif Valor1 == 2 :
        return True
    else:
        for i in range(2, Valor1):
            if Valor1 % i == 0:
                return False
        return True
    if Valor1 is True :
        print (f"El Numero 1 el cual es {Valor1}, Es un Numero Primo")
    else :
        print (f"El Numero 1 el cual es {Valor1}, No es un Numero Primo")
def primo2(Valor2):
    if Valor2 < 1 :
        return False
    elif Valor2 == 2 :
        return True
    else:
        for i in range(2, Valor2):
            if Valor2 % i == 0:
                return False
        return True
    if Valor2 is True :
        print (f"El Numero 2 el cual es {Valor2}, Es un Numero Primo")
    else :
        print (f"El Numero 2 el cual es {Valor2}, No es un Numero Primo")
while Opc != 0 :
    print("Digite 0 para salir.")
    print("Digite 1 para sumar.")
    print("Digite 2 para restar.")
    print("Digite 3 para multiplicar.")
    print("Digite 4 para dividir.")
    print("Digite 5 para potencia.")
    print("Digite 6 para cual es mayor o si son iguales.")
    print("Digite 7 para ver si son primos y cual.")
    Opc = int(input("Digite un numero [0,1,2,3,4,5,6,7]: "))
    if Opc == 1 :
        sumar(Valor1,Valor2)
    elif Opc == 2 :
        restar(Valor1,Valor2)
    elif Opc == 3 :
        multiplicar(Valor1,Valor2)
    elif Opc == 4 :
        dividir(Valor1,Valor2)
    elif Opc == 5 :
        potencia(Valor1,Valor2)
    elif Opc == 6 :
        mayor_o_igual(Valor1,Valor2)
    elif Opc == 7 :
       primo1(Valor1)
       primo2(Valor2)
print("Has terminado!, gracias")

def sumar (V1,V2) :
    suma = V1+V2
    return suma
if opc == 3 :
    total = sumar(5,10) ## HAY QUE GUARDARLO EN VARIABLE PARA QUE SE VAYA HACIENDO DEPENDIENDO DE LO QUE SE NECESITE
    print (total+1)

###        
###     
###      
###       
###
    
Opc = 1
Valor1 = int(input("Digite el valor #1: "))
Valor2 = int(input("Digite el valor #2: "))
def sumar (Valor1,Valor2):
    resultado = Valor1 + Valor2
    print (f"El resultado de la suma es: {resultado}")
def restar (Valor1,Valor2):
    resultado = Valor1 - Valor2
    print (f"El resultado de la resta es: {resultado}")
def multiplicar (Valor1,Valor2):
    resultado = Valor1 * Valor2
    return resultado #print (f"El resultado de la multiplicacion es: {resultado}")
def dividir (Valor1,Valor2):
    if Valor2 == 0 :
        print("No se puede dividir por 0")
    else: 
        resultado = Valor1 / Valor2
        print (f"El resultado es: {resultado}")
def potencia (Valor1,Valor2):
    Base = int(input(f"Si quieres que la base sea {Valor1}, Digita [1], Si quieres que la base sea {Valor2}, Digita [2]"))
    if Base == 1 :
        Base = Valor1
    elif Base == 2 :
        Base = Valor2
    else:
        print("No se encuentra en el rango de 1 a 2")
    Potencia = int(input(f"Si quieres que la potencia sea {Valor1}, Digita [1], Si quieres que la potencia sea {Valor2}, Digita [2]"))
    if Potencia == 1 :
        Potencia = Valor1
    elif Potencia == 2 :
        Potencia = Valor2
    else:
        print("No se encuentra en el rango de 1 a 2")
    resultado = Base ** Potencia
    print (f"El resultado de la potencia es: {resultado}")
def mayor_o_igual (Valor1,Valor2):
    mayor = 0
    if Valor1 > Valor2 :
        mayor = Valor1
        return mayor
    elif Valor1 == Valor2 :
        print ("Son iguales")
    else:
        mayor = Valor2
        return mayor
    return mayor #print (f"El mayor es: {mayor}")
def primo1(Valor1):
    if Valor1 < 1 :
        return False
    elif Valor1 == 2 :
        return True
    else:
        for i in range(2, Valor1):
            if Valor1 % i == 0:
                return False
        return True
    if Valor1 is True :
        print (f"El Numero 1 el cual es {Valor1}, Es un Numero Primo")
    else :
        print (f"El Numero 1 el cual es {Valor1}, No es un Numero Primo")
def primo2(Valor2):
    if Valor2 < 1 :
        return False
    elif Valor2 == 2 :
        return True
    else:
        for i in range(2, Valor2):
            if Valor2 % i == 0:
                return False
        return True
    if Valor2 is True :
        print (f"El Numero 2 el cual es {Valor2}, Es un Numero Primo")
    else :
        print (f"El Numero 2 el cual es {Valor2}, No es un Numero Primo")
while Opc != 0 :
    print("Digite 0 para salir.")
    print("Digite 1 para sumar.")
    print("Digite 2 para restar.")
    print("Digite 3 para multiplicar.")
    print("Digite 4 para dividir.")
    print("Digite 5 para potencia.")
    print("Digite 6 para cual es mayor o si son iguales.")
    print("Digite 7 para ver si son primos y cual.")
    Opc = int(input("Digite un numero [0,1,2,3,4,5,6,7]: "))
    if Opc == 1 :
        sumar(Valor1,Valor2)
    elif Opc == 2 :
        restar(Valor1,Valor2)
    elif Opc == 3 :
       Multi = multiplicar(Valor1,Valor2)
       print(Multi)
    elif Opc == 4 :
        dividir(Valor1,Valor2)
    elif Opc == 5 :
        potencia(Valor1,Valor2)
    elif Opc == 6 :
       May0r = mayor_o_igual(Valor1,Valor2)
       print(May0r)
    elif Opc == 7 :
       primo1(Valor1)
       primo2(Valor2)
print("Has terminado!, gracias")

#Ejercicio 1

Indice = 0
n = int(input("Digite el numero de cursos: "))
SumaC= 0
while Indice < n :
    m = int(input("Digite el numero de estudiantes: "))
    Indice1 = 0
    Suma = 0
    while Indice1 < m :
        Nombre = input("Digite el nombre del estudiante: ")
        Nota = float(input("Digite el la nota del estudiante: "))
        SumaC += Nota
        Suma += Nota
        Indice1 += 1
    print (f"La suma de las notas por curso es de {SumaC}")
    Indice += 1
    SumaC += Suma
print (f"Suma de todas las notas de los estudiantes es {Suma}")

#PRIMO

cont = 0
i = 1
while i <= Numero :
    Numero = int ( input ("Digite un numero: "))
    if Numero % i == 0 :
        cont += 1
if cont == 2 :
    print ("Es Primo")
else :
    print ("No es Primo")

#Ejercicio 2

Indice = 0
n = int(input("Digite el numero de cursos: "))
SumaC= 0
while Indice < n :
    NombreC = input("Digite el nombre del curso: ")
    m = int(input("Digite el numero de estudiantes: "))
    Indice1 = 0
    Suma = 0
    while Indice1 < m :
        Nombre = input("Digite el nombre del estudiante: ")
        Nota = float(input("Digite el la nota del estudiante: "))
        SumaC += Nota
        Suma += Nota
        Indice1 += 1
    print (f"La suma de las notas por curso es de {SumaC}")
    Indice += 1
    SumaC += Suma
print (f"Suma de todas las notas de los estudiantes es {Suma}")

#Ejercicio quiz

Valor1 = int(input("Digite Numero #1: "))
Valor2 = int(input("Digite Numero #2: "))
def sumar (Valor1,Valor2):
    resultado = Valor1 + Valor2
    return resultado
def P_I ():
    Valor = sumar(Valor1,Valor2)
    if Valor % 2 == 0:
        print ("Par")
    else:
        print ("Impar")
P_I()
        

#EJERCICIO 4 LARGUISIMOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO#

def Felicidades(Hora):
    if Hora >= 18 and  Hora <= 23 :
        print ("Felicitaciones Llegaste Temprano")
    else :
        print ("No Lleggaste Temprano :'c")
def Regañar(Contador):
    if Contador == 1 :
        print ("Regañado mijo")      
    elif Contador == 2 :
        print ("Castigado x 1 Semana")     
    elif Contador == 3 :
        print ("Castigado x 1 Mes")  
Hijos= int(input("Digite el Numero de hijos que tiene: "))
Indice1 = 0  
while Indice1 < Hijos :
    Bandera = 0     
    Indice2 = 0
    Contador += 1
    while Indice2 < 5:
        Hora = int(input("Digite el Numero de Horas: "))
        if Hora >= 0 and Hora < 24 :
            Felicidades(Hora)
            if Hora >= 0 and Hora <= 3:
                Contador += 1
            if Hora >= 3 and Hora <= 6 :
                Bandera = 1                    
        else :
            print("Valor de hora no válido")
        Indice2 += 1
    Regañar(Contador)
    if Bandera != 0 :
        print ("Castigado x por 1 semana")
    Indice1 += 1

#EJERCICIOS con FOR YA SE VINO LO MELO:

for i in range(3,10,2): 
    print (i)    # ## ####### de a cuanto va a aumentar
                 # ###
                 #   #Final
                 #Inicio
#Osea que imprime ("3,5,7,9")


#INCREMENTANDO
for i in range(1,0,1):
    print(i)            #0= NUMERO CUALQUIERA
#DECREMENTO
for i in range(10,0,-1):
    print(i)

#CONDICIONALES PARA FOR
#suma
suma= 0
for i in range(1,101):
    print(i)
    suma+=i
print(f"Suma es igual a: {suma}")

#CADENA DE CARACTERES CON FOR

for i in "Colombia":
    print(i)
#o mas bonito
Variable = "Colombia"
for i in Variable:
    print(i)
#Y SI QUIERE UNO AL LADO DEL OTRO
Variable = "Colombia"
for i in Variable:
    print(i, end="")
#SI QUEREMOS CONTAR CUANTOS CARACTERES HAY SERIA
Variable = "CoronaVirusColombia"
Contador = 0
for i in Variable:
    print(i, end="")
    Contador += 1
print('\n',f"la cantidad de caracteres que tiene es de: {Contador}")
    
#'\n' SALTO DE LINEA


#EJERCICIOS PRACTICA

#1) Elabore una función que reciba por parámetro una cadena y retorne como resultado cuántas vocales (mayúsculas o minúsculas) tenía la cadena en total
Caracter = input("Digite lo que quiera: ")
def May(Caracter):
    ContadorMayus = 0
    for i in Caracter:
        if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
            ContadorMayus += 1       
    return ContadorMayus
def Min(Caracter):
    ContadorMinus = 0
    for i in Caracter:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            ContadorMinus += 1
    return ContadorMinus
print('\n',f"la cantidad de vocales mayusculas que tiene es de: {May(Caracter)} y de vocales minusculas que tiene es de: {Min(Caracter)}")

#2) Elabore una función que reciba por parámetro una cadena y retorne como resultado cuántos caracteres tenía la cadena en total.
Caracter = input("Digite lo que quiera: ")
def Cuantos(Caracter):
    Contador = 0
    for i in Caracter:
        Contador += 1
    return Contador
print('\n',f"El total de caracteres tiene {Caracter} es de: {Cuantos(Caracter)}")

#3) Elabore un procedimiento que reciba por parámetro una cadena e imprima letra por letra los caracteres de la cadena, pero en mayúscula (busque la función que le permita lograr este comportamiento). 
Caracter = input("Digite lo que quiera: ")
for i in Caracter:
    print(i.upper())#,end="")     #.upper() MAYUSCULAS
                                #.lower() MINUSCULAS

#4) Elabore un procedimiento que reciba por parámetro una cadena e imprima letra por letra los caracteres de la cadena desde el último carácter de la cadena al primero.
Caracter = input("Digite lo que quiera: ")
Invertido = Caracter[::-1]
for i in Invertido:
    print(i)                                        # escritor = 'Fyodor Mikhailovich Dostoevsky'
                                                    # cadenaInvertida = escritor[::-1]
                                                    # print(cadenaInvertida)

#5) Elabore una función que reciba por parámetro una cadena e imprima letra por letra únicamente las vocales a y u que tenga la cadena. Retorne como resultado la cantidad de caracteres que no imprimió.
Caracter = input("Digite lo que quiera: ")
def JulianaElAmorDeMiVida(Caracter):
    Contador = 0
    for i in Caracter:
        if i == "u" or i == "U":
            print(i)
        elif i == "a" or i == "A":
            print(i)
        else:
            Contador +=1
    return Contador
print('\n',f"El total de caracteres que no eran a o u son:{JulianaElAmorDeMiVida(Caracter)}")

#6) Vuelva a hacer el ejercicio 5, pero ahora hágalo para un número n de cadenas que recibe por parámetro. Pida en cada iteración de n la cadena y luego sobre esta cadena solucione lo mismo que se pidió en el ejercicio 5. Utilice un while para recorrer las n cadenas y un for para analizar cada cadena en especial. 
ContadorWhile = 0
ContadorTodo = 0
N = int(input("Digite la cantidad de veces que se repita la cadena: "))
while ContadorWhile < N:
    Caracter = input("Digite lo que quiera: ")
    Contador = 0
    for i in Caracter:
        if i == "u" or i == "U":
            print(i)
        elif i == "a" or i == "A":
            print(i)
        else:
            Contador +=1
            ContadorTodo +=1
    print('\n',f"El total de caracteres que no eran a o u son: {Contador} por la cadena Numero: {ContadorWhile+1}")
    ContadorWhile += 1
print('\n',f"El total de caracteres que no eran a o u son:{ContadorTodo}")

#7) Elabore una función que reciba por parámetro una cadena y retorne True si la cadena es palíndroma (se lee igual de izquierda a derecha que de derecha a izquierda). Resuelva este ejercicio usando while y usando for. 
#USANDO FOR
Caracter = input("Digite lo que quiera: ")
Invertido = Caracter[::-1]
def Palindroma(Caracter):
    ContadorCadena = 0
    Bandera = 0
    for i in Caracter:
        ContadorCadena += 1
    j = ContadorCadena
    for i in Caracter:
        if i != j:
            Bandera = 1
        j -= 1
    if Bandera == 0:
        return False
    else:
        return True
if Palindroma(Caracter) is True:
    print("Es Palindroma")
else:
    print("No es Palindroma")
#USANDO WHILE
    
class Cadenas_Con_While:
    def __init__ (self, Caracter):
        self.Caracter=Caracter 
    def Palindromo(self):
        Caracter = self.Caracter
        c,i,nom,CaracterX,x = 0,0,'','',''
        i = len(Caracter)
        nom = Caracter.lower()
        while i != c:
            for x in nom:
                CaracterX = x + CaracterX
                c=c+1
            if nom==CaracterX:
                return str(Caracter + " Es Palindromo")
            else:
                return str(Caracter + " No es Palindromo")
Caracter = input('Dame una palabra: ')
Variable=Cadenas_Con_While(Caracter)
print(Variable.Palindromo())

  

#EJERICICIO DE COLOMBIA

Frase = "Colombia es un pais hermoso con una amplia variedad de sitios turisticos. No te quedes sin conocerlos"
Contador = 0
Bandera = 0
Contador_M = 0
for i in Frase:
    Contador +=1
    if i == "h" and Bandera == 0:
        print(f"la letra {i} se ecuentra en la posicion {Contador}")
        Bandera = 1
    elif i == "m" or i == "M":
        Contador_M += 1
print(f"Las veces que se repite la letra (M) o (m) es de : {Contador_M}")

#LISTAS########################################################################
#EMPIEZAN EN 0 y la ultima posision es -1

.append() #Adiciona elemento a la lista
.clear() #Borra todos los elementos de la lista
.copy() #retorna una copia de la lista
.count(e) #retorna el numero de elementos existentes en la lista que son iguales al elemento (e)
.index(e) #retorna el indice del primer elemento que sea igual al elemento (e)
.insert(p,e) #inserta un elemento (e) en la posicion (p) de la lista
.pop(p) #Borra el elemento que este en la posicion (p)
.extend(e,e,e,e) #etc Adiciona varios elementos a la vez donde (e) puede ser cualquiera
.sort() #Ordena la lista
 .sort() #Ordena la lista de manor a mayor
 .sort(reverse=True) #Ordena de mayor a menor
#
Lista = [23,47,34,53]
for i in range(len(Lista)):
    print (i)
    print(Lista[i])
print(Lista)
#
Lista = []
Lista.append("Casa")
Lista.append("Wembie")
Lista.append(3)
Lista.append(True)
print(Lista)
Lista[0] = "asaC"
print(Lista)
#
Lista = ["Webi","Manito",3,4,6,2,True]
for i in Lista:
    print(i)
Indices = len(Lista)
for i in range(Indices):
    print(i)
for i in range(Indices):
    print(i)
    print(Lista[i])
print(Lista)
#
def Suma(Lista):
    Indice = len(Lista)
    Suma = 0
    for i in range(Indice):
        Suma+= Lista[i]
    return Suma
def Mayor(Lista):
    Indice = len(Lista)
    May = Lista[0]
    Indice_Calcular = 0
    for i in range(Indice-1):
        if May<Lista[i+1]:
            May = Lista[i+1]
            Indice_Calcular = i+1
    return May , Indice_Calcular
def Menor(Lista):
    Indice = len(Lista)
    Men = Lista[0]
    Indice_Calcular = 0
    for i in range(Indice-1):
        if Men>Lista[i+1]:
            Men = Lista[i+1]
            Indice_Calcular = i+1
    return Men , Indice_Calcular 
import random as r
Lista = []
Tamaño = int(input("Digite hasta donde llegara la lista: "))
for i in range(Tamaño):
    Lista.append(r.randint(-100,100))
print(Lista)
P = Promedio(Lista)
print(f"El valor del promedio de la lista es de : {P}")
[M, I_C_1] = Mayor(Lista)
print(f"El valor mas grande de la lista es: {M}, y el indice es: {I_C_1}")
[Me, I_C_2] = Menor(Lista)
print(f"El valor mas grande de la lista es: {Me}, y el indice es: {I_C_2}")

#####"""""""""""""""""#####
#"#"#EJERCICIOS TALLER#"#"#
#####"""""""""""""""""#####

#1) Cree una función que le pregunte al usuario cuantos números desea que tenga una lista (por ejemplo 50), y con base en ese número, llene una lista por medio de números aleatorios (utilizando randint(0,101)) de manera que cada número aleatorio será cada valor de su lista. Como resultado usted debe retornar la lista llena de números.   
import random as Wembie
def Loqueseamijo():
    Lista = []
    Tam = int(input("Digite el numero de cuantos numeros tenga la lista: "))
    for i in range(Tam):
        Lista.append(Wembie.randint(0,101))
    return Lista
X = Loqueseamijo()
print (X)

#2) Realice un programa que, dada una lista de números enteros, retorne el número mayor de todos sus elementos.
import random as Wembie
Lista = []
Tam = int(input("Digite el numero de cuantos numeros tenga la lista: "))
for i in range(Tam):
    Lista.append(Wembie.randint(-1001,1001))
Mayor = Lista[0]
for i in range(Tam-1):
    if Mayor<Lista[i+1]:
        Mayor = Lista[i+1]
print(Lista)
print(f"El mayor numero de la lista es el: {Mayor}")

#3) Realice un programa que, dada una lista, retorne otra lista con los valores invertidos: Ejemplo, si la lista es [2,3,4], retorna [4,3,2]
Lista = ["Casita",5,2,3,6,262,34,235,25,23,523,526,7,8,8,234,2,2,1,1,23,4,"El Papu Wembie", "El Proximo Monitor :v"]
Invertida = Lista[::-1]
print(Invertida)

#4) Realice un programa que reciba como parámetro una Lista con números enteros (si desea puede usar el punto 1 para generar su lista) y un número, de manera que la función genere una nueva lista que contenga sólo los números que son divisibles por el número ingresado por el usuario. Ejemplo: Si se tiene la lista [6, 7, 8, 10, 12, 15, 3, 9, 22, 20] y el número ingresado por el usuario es 4, se deberá generar la lista [8, 12, 20]
Lista = [6, 7, 8, 10, 12, 15, 3, 9, 22, 20]
Nueva_Lista = []
Numero = int(input("Digite el numero que quiere que imprima los divisibles por ese numero: "))
for i in range(len(Lista)):
    if Lista[i]%Numero== 0:
        Nueva_Lista.append(Lista[i])
print(Lista)
print(Nueva_Lista)

#5) 5.	Diseñe una función que tome los elementos que se encuentran en las posiciones impares de una lista, los anexe a otra lista y la retorne. Ejemplo: Si se tiene la lista [1 , 2 , 4 , 5 , 6 , 4 , 3 , 2 , 1] se debe retornar la lista [2 , 5 , 4 , 2].
def Nose_XD():
    Lista = [1 , 2 , 4 , 5 , 6 , 4 , 3 , 2 , 1]
    Nueva_Lista = []
    for i in range(len(Lista)):
        if i%2!=0:
            Nueva_Lista.append(Lista[i])
    print(Lista)
    return Nueva_Lista
print(Nose_XD())

#6) Diseñe un procedimiento en Python al cual le ingrese una lista de números enteros positivos. La función debe crear e imprimir una lista con los elementos pares y una lista con los elementos impares. Ejemplo: Si se tiene la lista [6, 7, 8, 10, 12, 15, 3, 9, 22, 20] se debe imprimir una lista con  [6, 8, 10, 12, 22, 20] y otra lista con [7, 15, 3, 9]
def Wembie():
    Lista = [6, 7, 8, 10, 12, 15, 3, 9, 22, 20]
    Lista_Par = []
    Lista_Impar = []
    for i in range(len(Lista)):
        if Lista[i]%2==0:
            Lista_Par.append(Lista[i])
        else:
            Lista_Impar.append(Lista[i])
    print(Lista)
    print(Lista_Par)
    print(Lista_Impar)
Wembie()

#7) Realice un programa que se encargue de eliminar los espacios vacíos de una lista de caracteres (si los hay) al comienzo y final de la lista. Ejemplo. Si se tiene la lista [‘’,’a’,’b’,’e’,’’,’y’,’t’,’’] deberá quedar [’a’,’b’,’e’,’’,’y’,’t’].
Lista = ["","a","b","e","","y","t",""]
i = 0
while i <= len(Lista):
    if i == 0 and Lista[i] == "" or i == len(Lista)-1 and Lista[i] == "":
        Lista.pop(i)
    i += 1
print(Lista)

#8) Realice ahora un programa que se encargue de eliminar todos los espacios vacíos que se encuentren en una lista de caracteres.
Lista= ["","Hola",4,12,"",341,"",423,"",324,"",413,"","Wembie",True,False,"Fortnite","¿MLBB?","O","Miedo?","","Gei el que lo lea","","Holi profe xD"]
i = 0
while i < len(Lista):
    if Lista[i] == "":
        Lista.pop(i)
    i += 1
print(Lista)

#9) Realice una función que recibe como parámetro dos listas. La primera lista LE contiene los elementos a reorganizar, la segunda lista LP contiene las nuevas posiciones de los elementos de la lista LE. La función con los parámetros: LE = [”a”, ”b”, ”c”, ”d”] LP = [1, 3, 0, 2] debería retornar la lista [”c”, ”a”, ”d”, ”b”].
def Mobile_Legends():
    Lista_LE = ["a", "b", "c", "d"]
    Lista_LP = [1, 3, 0, 2]
    Lista_General = []
    for i in range(len(Lista_LE)):
        Lista_General.insert(Lista_LP[i],Lista_LE[i])
    return Lista_General
print("La nueva lista sería")
print(Mobile_Legends())

#10 Realice un programa que basado en 2 listas, construya la intersección de conjuntos de ellas (los elementos que están en la lista A y los elementos que están en la lista B) en una tercera lista, la nueva lista NO PUEDE tener elementos repetidos.
Lista_Wembie = ["Wembie",69,"Webi","Webita",6,9,"Habilidad"]
Lista_Fortnite =["Scar","Wembie","Construccion",69,"Habilidad","Ak-47",1,2,3,4,5,6,7,8,9]
Lista = []
for i in Lista_Wembie:
    for a in Lista_Fortnite:
        if i == a:
            if i not in Lista:
                Lista.append(i)
print(Lista_Wembie)
print(Lista_Fortnite)
print(Lista)

#o

Lista_Wembie = {"Wembie",69,"Webi",True,"Webita",False,6,9,"Habilidad"}
Lista_Fortnite ={"Scar","Wembie","Construccion",69,"Habilidad","Ak-47",1,2,3,4,5,6,7,8,9}
Lista = Lista_Wembie.intersection(Lista_Fortnite)
print(Lista)

#11) Realice un programa basado en 2 listas, que construya la diferencia de conjuntos de ellas (los elementos que se encuentran en la lista A y que no se encuentran en la lista B) en una tercera lista.
Lista1= [1,2,4,6,8,3]
Lista2= [1,5,6,4,9,10]
Lista = []
for i in Lista1:
    if i not in Lista2:
        Lista.append(i)
print(Lista1)
print(Lista2)
print(Lista)
#o

Lista1= {1,2,4,6,8,3}
Lista2= {1,5,6,4,9,10}
Lista = Lista1.difference(Lista2)
print(Lista)

#12) Realice un programa que permita ingresar una cantidad N de artículos y una cantidad M de precios en el mercado, con esos datos cree una lista similar a la siguiente: Articulos=[[“Jabon”,2000,1800,1300], [“arroz”,1350,1500,1600…..X]……[X]]
Lista = []
N = int(input("Digite la cantidad de articulos: "))
for i in range(N):
    ListaXD = []
    Articulo = input("Digite el articulo: ")
    M =int(input(f"Digite la cantidad de precios de {Articulo} en el mercado : "))
    ListaXD.append(Articulo)
    for j in range(M):
        Precio = float(input("Digite el precio del articulo: "))
        ListaXD.append(Precio)
    print(ListaXD)
    Lista.append(ListaXD)
print(Lista)

#MATRIZ

Matriz = [[1,2],[3,4]]
Filas = len(Matriz)
print (f"El numero de filas que tiene la matriz es de: {Filas}")
Columnas = len(Matriz[0])
print (f"El numero de columnas que tiene la matriz es de: {Columnas}")

Matriz = [["Hola",2],[True,4]]
print(Matriz)
print(Matriz[0][1]) # Imprime el 2
print(Matriz[1][1]) # Imprime el 4
Matriz[0][1] = "Wembie"
print(Matriz[0][1]) # Imprime "Wembie"
print(Matriz)

Matriz = [["Hola",2],[True,4]]
for i in Matriz:
    for w in i:
        print(w)

Matriz = [["Hola",2],[True,4]]
for i in range(len(Matriz)):
    for w in range(len(Matriz[0])):
        print(i,w)

Matriz = [["Hola",2],[True,4]]
for i in range(len(Matriz)):
    for w in range(len(Matriz[0])):
        print(f"Indices son: {i,w}")
        print(f"Valores son: {Matriz[i][w]}")
print(Matriz)

Filas = 3
Columnas = 3
Matriz = []
for i in range(Filas):
    Matriz.append([])
    for w in range(Columnas):
        Matriz[i].append(" ")
print(Matriz)


def Pares(Matriz):
    Lista = []
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            if Matriz[i][j] % 2 == 0:
                Lista.append(Matriz[i][j])
    return Lista
def Cont_Numero(Matriz):
    Cont_Positivo = 0
    Cont_Negativo = 0
    Cont_Neutro = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            if Matriz[i][j] == 0:
                Cont_Neutro += 1
            elif Matriz[i][j] < 0:
                Cont_Negativo += 1
            else:
                Cont_Positivo += 1
    return Cont_Positivo,Cont_Negativo,Cont_Neutro  
import random as Wembie
Filas = 3
Columnas = 3
Matriz = []
for i in range(Filas):
    Matriz.append([])
    for w in range(Columnas):
        Matriz[i].append(Wembie.randint(-10,10))
print(Matriz)
print(Pares(Matriz))
[Cont_P,Cont_N,Cont_O] = Cont_Numero(Matriz)
print(f"Positivos: {Cont_P}, Negativos: {Cont_N}, Cero: {Cont_O}")

#-#-####-#-#
#-#Taller#-#
#-#-####-#-#


#1) Una matriz es espejo de otra, cuando los elementos de cada posición de la primera matriz son exactamente iguales a los elementos de cada posición de la segunda matriz. Realice una función que recibe 2 matrices por parámetro y responde verdadero si son espejo o falso si no lo son. Debe validar que las 2 matrices sean del mismo tamaño.

def WembieXD(X,Y):
    Si = "Si"
    No = "No"
    if len(X) == len(Y) and len(X[0]) == len(Y[0]):
        for i in range(len(X)):
            for j in range(len(X[0])):
                if X[i][j] == Y[i][j]:
                    ()
                else:
                    return No
        return Si
    else:
        return No
import random as Wembie
Filas = Wembie.randint(1,3)
Columnas = Wembie.randint(1,3)
Matriz0 = []
for i in range(Filas):
    Matriz0.append([])
    for w in range(Columnas):
        Matriz0[i].append(Wembie.randint(0,2))
print(Matriz0)
Filas = Wembie.randint(1,3)
Columnas = Wembie.randint(1,3)
Matriz1 = []
for i in range(Filas):
    Matriz1.append([])
    for w in range(Columnas):
        Matriz1[i].append(Wembie.randint(0,2))
print(Matriz1)
print(f"Son espejo las matrices? Respuesta: {WembieXD(Matriz0,Matriz1)}")


#2) Una matriz identidad es una matriz cuadrada que presenta en su diagonal principal números 1 y en el resto posiciones números 0. Realice un programa que toma una matriz y responde verdadero si es una matriz identidad o 0 si no lo es. Debe validar que la matriz sea cuadrada.

#Como crear una identidad
Numero = int(input('Introduce un entero positivo: ')) 
Matriz = []
for i in range(Numero):
	Fila = []
	for j in range(Numero):
		Valor = 1 if i==j else 0
		Fila.append(Valor)
	Matriz.append(fila)
print(Matriz)
#
def Webita(X):
    Si = "Si"
    No = "No"
    if len(X) == len(X[0]):
        for i in range(len(X)):
            for j in range(len(X[i])):
                if X[i][j] == 1 and i == j :
                    ()
                elif X[i][j] == 0:
                    ()
                else:
                    return No
        return Si
    else:
        return No
import random as Wembie
Filas = Wembie.randint(2,4)
Columnas = Wembie.randint(2,4)
Matriz = []
for i in range(Filas):
    Matriz.append([])
    for w in range(Columnas):
        Matriz[i].append(Wembie.randint(0,1))
print(Matriz)
print(f"Son de identidad la matriz? Respuesta: {Webita(Matriz)}")


#3) Dada la siguiente matriz de números naturales, desarrolle los ejercicios propuestos.

Matriz_General = [[1,4,6,2],[12,16,1,5],[7,11,8,6],[15,4,9,10]]

#a) Cree una función que, dada una matriz, retorne el menor elemento de toda la matriz

Matriz_General = [[1,4,6,2],[12,16,1,5],[7,11,8,6],[15,4,9,10]]
def Menor(Matriz):
    menor = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            if Matriz[i][j] < menor:
                menor = Matriz[i][j]
    return menor
print(f"El menor de los numeros es: {Menor(Matriz_General)}")

#b) Cree una función que dada una matriz retorne el mayor elemento de toda la matriz.

Matriz_General = [[1,4,6,2],[12,16,1,5],[7,11,8,6],[15,4,9,10]]
def Mayor(Matriz):
    mayor = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            if Matriz[i][j] > mayor:
                mayor = Matriz[i][j]
    return mayor
print(f"El mayor de los numeros es: {Mayor(Matriz_General)}")

#c) Cree un procedimiento que, dada una matriz y un valor a buscar, diga cuantas veces se encuentra dicho valor dentro de la matriz.

Matriz_General = [[1,4,6,2],[12,16,1,5],[7,11,8,6],[15,4,9,10]]
def Contador(Matriz,Num):
    contador = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            if Matriz[i][j] == Num:
                contador += 1                
    return contador
Numero = int(input("Digite el numero deseado: "))
print(f"el numero {Numero} se repite: {Contador(Matriz_General,Numero)}")

#d) Cree un procedimiento, que, dada una matriz, muestre el promedio de los elementos de la matriz.

Matriz_General = [[1,4,6,2],[12,16,1,5],[7,11,8,6],[15,4,9,10]]
def Promedio(Matriz):
    promedio = 0
    total = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            promedio += Matriz[i][j]
            total += 1                
    return promedio/total
print(f"El promedio es: {Promedio(Matriz_General)}")

#e) Cree una función que, dada una matriz y un valor, y con la intención de encontrar los elementos que sean mayores al valor dado, retorne una nueva lista de listas en la cual se muestre para cada sublista, la posición de la columna de dónde se encuentra el valor encontrado, y cuál fue ese valor encontrado.

Matriz_General = [[1,4,6,2],[12,16,1,5],[7,11,8,6],[15,4,9,10]]
def Mayor14(Matriz,Num):
    Matrix = []
    for i in range(len(Matriz)):
        Lista = []
        for j in range(len(Matriz[0])):
            Mayor = Num
            if Matriz[i][j] > Num:
                Mayor = Matriz[i][j]
                Lista.append(j)
                Lista.append(Mayor)
                Matrix.append(Lista)
    return Matrix
Numero = int(input("Digite el numero deseado: "))
print(f"La nueva matriz es: {Mayor14(Matriz_General,Numero)}")


#4) A continuación usted encontrará una matriz (lista de listas) con la información de los primeros partidos que han jugado algunos equipos del fútbol colombiano en la Copa Aguila (primeras 3 fechas). Tenga en cuenta que, la primera columna tiene el nombre del equipo, y las siguientes muestran el tipo de resultado obtenido por el equipo en cada partido. Así entonces, si la matriz tiene la letra “G” simboliza que el partido fue ganado (obtuvo 3 puntos), si la letra es “E” simboliza que el partido fue empatado (obtuvo 1 punto), si la letra es “P” simboliza que el partido fue perdido (no obtuvo puntos).

Matriz_General = [["America","G","P","E"],["Cali","E","E","E"],["Huila","G","G","G"],["Once","P","P","G"],["Pasto","G","P","G"]]

#a) Crear una nueva lista de listas, que contenga sólo el nombre del equipo y el total de puntos obtenidos por todos los partidos. Ejemplo: Resultado= [['America',4],['Cali',3],['Huila',9],['Once',3],['Pasto',6]]

Matriz_General = [["America","G","P","E"],["Cali","E","E","E"],["Huila","G","G","G"],["Once","P","P","G"],["Pasto","G","P","G"]]
Matriz = []
for i in range(len(Matriz_General)):
    Lista = []
    Puntos = 0
    for j in range(len(Matriz_General[0])):
        if Matriz_General[i][j] and j == 0:
            ()
        elif Matriz_General[i][j] == "G":
            Puntos += 3
        elif Matriz_General[i][j] == "E":
            Puntos += 1
        else:
            Puntos += 0
    Lista.append(Matriz_General[i][0])
    Lista.append(Puntos)
    Matriz.append(Lista)
print(Matriz)

#b) Dado un número de partido  y un tipo de resultado, mostrar en pantalla los nombres de los equipos que obtuvieron ese resultado, en esa fecha. Ejemplo: para el número de partido 2 y el tipo de resultado P se debería mostrar: (América, Once y Pasto)

Matriz_General = [["America","G","P","E"],["Cali","E","E","E"],["Huila","G","G","G"],["Once","P","P","G"],["Pasto","G","P","G"]]
Numero = 0
while 0 != 1:
    Numero = int(input("Digite un Numero del 1 al 3: "))
    if Numero > 0 and Numero < 4:
        break
    else:
        print("El numero no se encuentra en el rango")        
Resultado = input("Digite el Resultado [G,E,P]: ")
Matriz = []
for i in range(len(Matriz_General)):
    if Resultado == "g" or Resultado == "G":
        if Matriz_General[i][Numero] == "G":
            Matriz.append(Matriz_General[i][0])   
    elif Resultado == "e" or Resultado == "E":
        if Matriz_General[i][Numero] == "E":
            Matriz.append(Matriz_General[i][0]) 
    elif Resultado == "p" or Resultado == "P":
        if Matriz_General[i][Numero] == "P":
            Matriz.append(Matriz_General[i][0]) 
print(Matriz)

#c) Pida al usuario el registro de un equipo de futbol (Nombre y el tipo de resultado de las primeras 3 fechas), y adiciónelo como una nueva fila a la matriz de partidos. Pero, si el usuario escribe el nombre de un equipo que ya se encuentra en la matriz, entonces sólo actualice los datos de la fila correspondiente a ese equipo.

Matriz_General = [["America","G","P","E"],["Cali","E","E","E"],["Huila","G","G","G"],["Once","P","P","G"],["Pasto","G","P","G"]]
print(Matriz_General)
for i in range(len(Matriz_General)):
        Partido = []
        Equipo = input("Digite el nombre del equipo: ")
        Resultado1 = input("Digite el Resultado del primer partido [G,E,P]: ")
        Resultado2 = input("Digite el Resultado del segundo partido [G,E,P]: ")
        Resultado3 = input("Digite el Resultado del tercer partido [G,E,P]: ")
        Partido.append(Equipo)
        Partido.append(Resultado1.upper())
        Partido.append(Resultado2.upper())
        Partido.append(Resultado3.upper())
        Bandera = 0
        for j in range(len(Matriz_General[i])):
            if Equipo == Matriz_General[j][0]:
                Matriz_General[j] = Partido
                Bandera = 1
        if Bandera == 0:
            Matriz_General.append(Partido)
        print(Matriz_General)          
#5) La agencia de Turismo Viajemos Tours posee información acerca de todos los planes vacacionales que ofrecen, pero cuando llega un cliente es muy difícil brindarle la atención adecuada, debido a la demora en encontrar lo que se requiere. Por tal motivo lo han contratado a usted para agilizar el proceso. 
        
Paquetes=[["San Andres",2000000,"Blue Reef",20,"Todo Incluido",True],["Cartagena",1500000,"Sol Caribe",0,"Hospedaje",False],["Santa Marta",1300000,"Mar y Sol",10,"Todo Incluido",False],["San Andres",3000000,"El Dorado",5,"Hospedaje",True]]
    
#a) Una función en Python que dada una matriz de Viajes y un destino, retorne en una lista de listas, el nombre del hotel y la tarifa, para todos aquellos paquetes que cumplan con dicho destino y que además incluyan los pasajes.  Ejemplo. Resultado1=[ [“Blue Reef”, 2000000], [“El Dorado”, 3000000] ]

def Wembie():
    Paquetes = [["San Andres",2000000,"Blue Reef",20,"Todo Incluido",True],["Cartagena",1500000,"Sol Caribe",0,"Hospedaje",False],["Santa Marta",1300000,"Mar y Sol",10,"Todo Incluido",False],["San Andres",3000000,"El Dorado",5,"Hospedaje",True]]
    Nueva_Lista = []
    Destino = input("Digite el Destino: ")
    for i in range(len(Paquetes)):
        Lista = []
        if Destino == Paquetes[i][0] and Paquetes[i][len(Paquetes[i])-1] == True:
            Lista.append(Paquetes[i][2])
            Lista.append(Paquetes[i][1])
        Nueva_Lista.append(Lista)              
    return Nueva_Lista
while 1 != 0:
    print(Wembie())
    Stop = input("Quieres para el programa? : [Si] o [No]: ")
    if Stop == "SI" or Stop == "Si" or Stop == "sI" or Stop == "si":
        break

#b) Un procedimiento que dada una matriz de Viajes y un valor de pago por persona indicado por el cliente, imprima en pantalla toda la información de todos aquellos paquetes cuyo costo sea menor o igual al valor de pago indicado. Tenga en cuenta el valor de descuento del paquete turístico.

def Sapo():
    Paquetes = [["San Andres",2000000,"Blue Reef",20,"Todo Incluido",True],["Cartagena",1500000,"Sol Caribe",0,"Hospedaje",False],["Santa Marta",1300000,"Mar y Sol",10,"Todo Incluido",False],["San Andres",3000000,"El Dorado",5,"Hospedaje",True]]
    Nueva_Lista = []
    Valor = int(input("Digite el Valor: "))
    for i in range(len(Paquetes)):
        Porcentaje = Paquetes[i][3]/100
        Decrementar = 1-Porcentaje
        Total = Decrementar * Paquetes[i][1]
        Lista = []
        if Valor == Total or Valor > Total:
            Lista.append(Paquetes[i])
            print(Lista,end='\n')
            print(f"Su paquete tiene un descuento del {Paquetes[i][3]}% y tu total seria: {Total}",end='\n')
        Nueva_Lista.append(Lista)
    print(Nueva_Lista)   
Sapo()       


#c) Una función que permita ingresar un nuevo paquete turístico (con toda la información) a la matriz. Debe tener en cuenta que si el paquete turístico ya existe para la ciudad y hotel definidos, se debe modificar la información y NO adicionarla. Al final debe retornar la matriz actualizada.

def Holi():
    Paquetes = [["San Andres",2000000,"Blue Reef",20,"Todo Incluido",True],["Cartagena",1500000,"Sol Caribe",0,"Hospedaje",False],["Santa Marta",1300000,"Mar y Sol",10,"Todo Incluido",False],["San Andres",3000000,"El Dorado",5,"Hospedaje",True]]
    print(Paquetes)
    Pack = []
    Destino = input("Digite el nombre del destino: ")
    Precio = int(input("Digite el precio: "))
    Hotel = input("Digite el nombre del hotel: ")
    Descuento = int(input("Digite el descuento: "))
    Incluido = input("Digite [Todo Incluido , Hospedaje]: ")
    Vuelo = bool(input("Digite si tiene vuelos incluidos [True] de lo contrario [False]: "))
    Pack.append(Destino)
    Pack.append(Precio)
    Pack.append(Hotel)
    Pack.append(Descuento)
    Pack.append(Incluido)
    Pack.append(Vuelo)
    Bandera = 0
    for i in range(len(Paquetes)):
        if Destino == Paquetes[i][0] and Hotel == Paquetes[i][2]:
            Paquetes[i] = Pack
            Bandera = 1
    if Bandera == 0:
        Paquetes.append(Pack)
    print(Paquetes)
Holi()


#6) Un estudiante necesita conocer cómo ha sido su rendimiento en las materias del actual semestre de su carrera.  Con base en esa hipótesis, desarrolle los siguientes ejercicios propuestos.

#a) Cree una matriz, en la cual pida al usuario el nombre de cada materia y las 4 notas que obtuvo durante el curso (Cada materia y sus notas, conforman una fila de la matriz). Retorne la matriz para que pueda usarla en los siguientes ejercicios.    

def Acostica():
    Matriz = []
    Materias = int(input("Digite la cantidad de materias: "))
    for i in range(Materia):
        Lista = []
        Materia = input("Digite la materia: ")
        Lista.append(Materia)
        for j in range(4):
            Nota = float(input(f"Digite la nota de {Materia}: "))
            Lista.append(Nota)
        print(Lista)
        Matriz.append(Lista)
    return Matriz
Matriz = Acostica()
print(Matriz)

#[["Matematicas", 3.5, 4.0, 5.0, 4.9], ["Programacion", 5.0, 5.0, 5.0, 5.0], ["Estatica", 4.0, 3.0, 3.0, 4.4]]

#b) Usando la matriz del punto A, genere una nueva matriz, en la cual aparezca por cada fila sólo el nombre de la materia y el promedio de las notas (se parte de la base de que todas las notas tienen el mismo porcentaje).

Matriz = [["Matematicas", 3.5, 4.0, 5.0, 4.9], ["Programacion", 5.0, 5.0, 5.0, 5.0], ["Estatica", 4.0, 3.0, 3.0, 4.4]]
Matriz_Nueva = []
for i in range(len(Matriz)):
    Promedio = 0
    Lista = []
    Lista.append(Matriz[i][0])
    for j in range(len(Matriz[i])):
        if type(Matriz[i][j]) != str:
            Promedio += Matriz[i][j]   
    Lista.append(Promedio/4)
    Matriz_Nueva.append(Lista)
print(Matriz)
print(Matriz_Nueva)

#[['Matematicas', 4.35], ['Programacion', 5.0], ['Estatica', 3.6]]

#c) Haciendo uso de la matriz obtenida en el punto B, muestre en pantalla, cuál fue la materia que le quedó más alta al estudiante, es decir, que presentó mejor promedio.

Matriz = [['Matematicas', 4.35], ['Programacion', 5.0], ['Estatica', 3.6]]
Mayor = 0
for i in range(len(Matriz)):
    for j in range(len(Matriz[i])):
        if type(Matriz[i][j]) == float: 
            if Matriz[i][j] > Mayor:
                Mayor = Matriz[i][j]
for i in range(len(Matriz)):
    if Mayor == Matriz[i][1]:
        print(Matriz[i])

#d) Usando la matriz del punto A, muestre  en pantalla cuál fue la mejor nota y de qué materia, obtenida durante todo el semestre.

Matriz = [["Matematicas", 3.5, 4.0, 5.0, 4.9], ["Programacion", 5.0, 5.0, 5.0, 5.0], ["Estatica", 4.0, 3.0, 3.0, 4.4]]
M = []
for i in range(len(Matriz)):
    Mayor = 0
    Lista = []
    for j in range(len(Matriz[i])):
        if type(Matriz[i][j]) == float: 
            if Matriz[i][j] > Mayor:
                Mayor = Matriz[i][j]
                print(Matriz[i][j])
    if Mayor in Matriz[i]:
        Lista.append(Matriz[i][0])
        Lista.append(Mayor)
    M.append(Lista)
print(M)

#e) Cree una función que le permita al estudiante ingresar una nueva materia a la matriz obtenida en el punto A.

def Agregar():
    Matriz = [["Matematicas", 3.5, 4.0, 5.0, 4.9], ["Programacion", 5.0, 5.0, 5.0, 5.0], ["Estatica", 4.0, 3.0, 3.0, 4.4]]
    Estudio = []
    Materia = input("Digite la Materia: ")
    Nota1 = float(input("Digite la nota 1: "))
    Nota2 = float(input("Digite la nota 2: "))
    Nota3 = float(input("Digite la nota 3: "))
    Nota4 = float(input("Digite la nota 4: "))
    Estudio.append(Materia)
    Estudio.append(Nota1)
    Estudio.append(Nota2)
    Estudio.append(Nota3)
    Estudio.append(Nota4)
    Matriz.append(Estudio)
    return Matriz
print(Agregar())
    

#f) Cree una función que le permita al estudiante modificar una materia de la matriz obtenida en el punto A (podrá modificar el registro completo, donde coincida el nombre de una materia dada).

def Agregarx2():
    Matriz = [["Matematicas", 3.5, 4.0, 5.0, 4.9], ["Programacion", 5.0, 5.0, 5.0, 5.0], ["Estatica", 4.0, 3.0, 3.0, 4.4]]
    print(Matriz)
    Estudio = []
    Materia = input("Digite la Materia: ")
    Nota1 = float(input("Digite la nota 1: "))
    Nota2 = float(input("Digite la nota 2: "))
    Nota3 = float(input("Digite la nota 3: "))
    Nota4 = float(input("Digite la nota 4: "))
    Estudio.append(Materia)
    Estudio.append(Nota1)
    Estudio.append(Nota2)
    Estudio.append(Nota3)
    Estudio.append(Nota4)
    Bandera = 0
    for i in range(len(Matriz)):
        if Materia == Matriz[i][0]:
            Matriz[i] = Estudio
            Bandera = 1
    if Bandera == 0:
        Matriz.append(Estudio)
    print(Matriz)
Agregarx2()


#DICCIONARIOS#
Diccionario = {}
Diccionario = dict() #es lo mismo

Diccionario = {"Nota":5}
Diccionario = {"Nota1":5, "Nota2":4, "Nota3":4}
Diccionario = {"Nota1":5, 2:"Nota2", "Nota3":4, 20.20:True}
print(Diccionario)
print(Diccionario["Nota1"])

#Agregar

Diccionario["Nombre"] = "Juan"

#

Diccionario = {"Notas": [3,4,5,2,1]}
print(Diccionario["Notas"][0]) #3
Diccionario["Notas"].append(3)
print(Diccionario["Notas"])
Diccionario = {"Notas": [3,4,5,[3,5],2,1]}
print(Diccionario["Notas"][3][1]).append(2) # Agrega el 2 en la lista dentro de la lista [3,5,2] quedaria
print(Diccionario["Notas"])

#ciclo
Diccionario = {"Nota1":5, 2:"Nota2", "Nota3":4, 20.20:True}
for key in Diccionario:
    print(f"La llave es:{key} y su valor es: {Diccionario[key]}")

#dict()
Diccionario = dict(Nombre="Juan", Apellido="Acosta", Años=18)
print(Diccionario)
Diccionario = dict(Nombre=dict(Nombre1="Juan",Nombre2="Esteban") Apellido="Acosta", Años=18)

#zip()
Diccionario = dict(zip("abcd",[1,2,3,4]))
print(Diccionario)
#{'a': 1, 'b': 2, 'c': 3, 'd': 4}
Lista1 = ["Arroz","Papa","Yuca"]
Lista2 = [2000,3000,1000]
Diccionario = dict(zip(Lista1,Lista2))
print(Diccionario)
#{'Arroz': 2000, 'Papa': 3000, 'Yuca': 1000}

#items()
Diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
items = #Falta

#keys()
Diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Llaves = Diccionario.keys()
print(Llaves)

#values()
Diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Valores = Diccionario.values()
print(Valores)

#clear()
Diccionario.clear()
#Borrar#

#copy()
Diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Diccionario1 = Diccionario.copy()

#fromkeys()

#get() si esta normal pero si no esta le da none y no se acaba el programa
Diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Valor = Diccionario.get("b")
print(Valor)

#update() si los valores son iguales se reemplazan y si no estan se añaden
Diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Diccionario1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
Diccionario.update(Diccionario1)
print(Diccionario)

################
#=#=#EXAMEN#=#=#
################
Clinica = [[["O"],["O"],["O"],["O"]],[["O"],["O"],["O"],["O"]],[["O"],["O"],["O"],["O"]],[["O"],["O"],["O"],["O"]],[["O"],["O"],["O"],["O"]]]
def Cupo(Matriz):
    print("***** TENGA EN CUENTA *****")
    print("0 = 1, 1 = 2, 2 = 3, 3 = 4, 4 = 5")
    Piso = int(input("Digite el Piso al que sera asignado [0,1,2,3,4]: ")) #0=1, 1=2, 2=3, 3=4, 4=5
    ContadorVacios = 0
    for i in range(len(Matriz[Piso])):
        if Matriz[Piso][i] == ["O"]:
            ContadorVacios += 1
    print(f"La cantidad de habitaciones disponibles en el piso {Piso+1} es de: {ContadorVacios}")
def Registrar(Matriz):
    print("***** TENGA EN CUENTA *****")
    print("0 = 1, 1 = 2, 2 = 3, 3 = 4, 4 = 5")
    Piso = int(input("Digite el Piso [0,1,2,3,4]: ")) #0=1, 1=2, 2=3, 3=4, 4=5
    Paciente = []
    Cedula = int(input("Digite la cedula: "))
    Nombre = input("Digite el nombre: ")
    Enfermedad_Principal = input("Digite la enfermedad principal: ")
    Edad = int(input("Digite la edad: "))
    Sexo = input("Digite el sexo [M,F]: ")
    Eps = input("Digite que tipo de Eps tiene [Coomeva,Famisanar,Sura,Suramericana,Compensar,Ninguna]: ")
    Paciente.append(Cedula)
    Paciente.append(Nombre)
    Paciente.append(Enfermedad_Principal)
    Paciente.append(Edad)
    Paciente.append(Sexo)
    Paciente.append(Eps)
    print(Paciente)
    Bandera = 0
    if ["O"] not in Matriz[Piso]:
        print("No Hay espacio disponible")
    for i in range(len(Matriz[Piso])):
        if Matriz[Piso][i] == ["O"] and Bandera == 0:
            Matriz[Piso][i] = Paciente
            Bandera = 1
def Retirar(Matriz):
    Encontrada = 0
    Cedula_Paciente = int(input("Digite la cedula: ")) 
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if Cedula_Paciente == Matriz[i][j][0]:
                Matriz[i][j] = ["O"]
                Encontrada = 1
    if Encontrada == 0:
        print("Cedula no encontrada")
def Buscar(Matriz):
    Encontrada = 0
    Cedula_Paciente = int(input("Digite la cedula: "))
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if Cedula_Paciente == Matriz[i][j][0]:
                print(f"El paciente se encuentra en el piso {i+1} y en la habitacion {j+1}.")
                Encontrada = 1
    if Encontrada == 0:
        print("Cedula no encontrada")
def Mover(Matriz):
    Encontrada = 0
    Cedula_Paciente = int(input("Digite la cedula: "))
    Paciente = []
    Bandera = 0
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if Cedula_Paciente == Matriz[i][j][0]:
                Paciente = Matriz[i][j]
                Encontrada = 1
                Matriz[i][j] = ["O"]
    if Encontrada == 0:
        print("Cedula no encontrada")
    print("***** TENGA EN CUENTA *****")
    print("0 = 1, 1 = 2, 2 = 3, 3 = 4, 4 = 5")
    Piso = int(input("Digite el Piso al que lo quiere mover [0,1,2,3,4]: ")) #0=1, 1=2, 2=3, 3=4, 4=5    
    if ["O"] not in Matriz[Piso]:
        print("No Hay espacio disponible")
    for i in range(len(Matriz[Piso])):
        if Matriz[Piso][i] == ["O"] and Bandera == 0:
            Matriz[Piso][i] = Paciente
            Bandera = 1
def Ocupacion(Matriz):
    print(Matriz)
def Wembie(Matriz):
    Encontrada = 0
    Cedula_Paciente = int(input("Digite la cedula para saber cuanto % tiene de descuento: "))
    for i in range(len(Matriz)):
        for j in range(len(Matriz[i])):
            if Cedula_Paciente == Matriz[i][j][0]:
                if Matriz[i][j][5] == "Coomeva":
                    print("Su descuento sera del 20% al precio asignado")
                elif Matriz[i][j][5] == "Famisanar":
                    print("Su descuento sera del 30% al precio asignado")
                elif Matriz[i][j][5] == "Sura":
                    print("Su descuento sera del 15% al precio asignado")
                elif Matriz[i][j][5] == "Suramericana":
                    print("Su descuento sera del 25% al precio asignado")
                elif Matriz[i][j][5] == "Compensar":
                    print("Su descuento sera del 35% al precio asignado")
                elif Matriz[i][j][5] == "Ninguna":
                    print("Su descuento sera del 0% ya que no tienes eps")  
                Encontrada = 1
    if Encontrada == 0:
        print("Cedula no encontrada")        
Numero = 1
while Numero != 0:
    print("***** SOFTWARE DE LA CLINICA BIENVENIDOS *****")
    print("1. Conocer cupo de un piso.")
    print("2. Registrar un paciente.")
    print("3. Retirar un paciente.")
    print("4. Buscar un paciente.")
    print("5. Mover un paciente de piso.")
    print("6. Mostrar ocupacion de la clinica.")
    print("7. Cuanto porcentaje de descuento tiene un paciente") #BONUS
    print("0. Salir.")
    Numero = int(input("Digite el Numero deseado [1,2,3,4,5,6,0]: "))
    if Numero == 1: #1.	Cupo de un piso: Desarrolle una función o procedimiento que, según un piso dado por el usuario, indique cuántas habitaciones disponibles (no ocupadas) quedan en ese piso
        Cupo(Clinica)
    if Numero == 2: #2.	Registrar un paciente: Desarrolle una función o procedimiento que le ingresa como parámetro un paciente y un piso, de manera que el paciente debe quedar registrado dentro de la clínica en el respectivo piso (siempre y cuando haya cupo en el piso). Es recomendable que elabore una función para crear al paciente, de manera que se le pidan al usuario los datos del paciente (cédula, nombre, enfermedad principal, edad, sexo) y retorne el paciente creado para luego ser registrado en la clínica.
        Registrar(Clinica)
    if Numero == 3: #3.	Retirar un paciente: Desarrolle una función o procedimiento que, dada una cédula de un paciente, lo retire de la habitación en que se encuentra y por ende también de la clínica.
        Retirar(Clinica)
    if Numero == 4: #4.	Buscar un paciente: Desarrolle una función o procedimiento que dada una cédula indique si el paciente se encuentra en la clínica, en qué piso y en qué habitación (las habitaciones son la 1, 2, 3 y 4). Por ejemplo (“El paciente se encuentra registrado en el segundo piso, habitación 2”).
        Buscar(Clinica)
    if Numero == 5: #5.	Mover un paciente de piso: Desarrolle una función o procedimiento que recibe como parámetro una cédula y un piso, de manera que el paciente sea retirado del piso en que está y quede registrado en el nuevo piso (siempre y cuando haya cupo en el piso).
        Mover(Clinica)
    if Numero == 6: #6.	Mostrar ocupación de clínica: realice una función o procedimiento que muestre gráficamente (en forma de matriz, por ejemplo) qué habitaciones se encuentran ocupadas (con los datos del paciente) y qué habitaciones se encuentras disponibles (marcadas con una O), abajo hay una imagen de ejemplo donde se observan 2 habitaciones ocupadas, una en el segundo piso, y otra en el quinto piso, el resto de las habitaciones se encuentras disponibles.
        Ocupacion(Clinica)
    if Numero == 7: #7. Bonus By: Wembie (Digitando la cedula del paciente se verificara cuanto porcentaje de descuento se le sera asignado dependiendo de que eps tenga)
        Wembie(Clinica)
        
#PARCIAL ANA AZCARATE
        
def Covid():
    Matriz =[]
    N = int(input("Digite la cantidad de personas del pais: "))
    for i in range(N):
        Lista = []
        Nombre = input(f"Digite el Nombre de la persona {i+1}: ")
        Apellido = input(f"Digite el Apellido de la persona {i+1}: ")
        Edad = int(input(f"Digite la edad de la persona {i+1}: "))
        Contagiado = int(input(f"Digite si esta contagiado [0] de lo contrario [1] de la persona {i+1}: "))
        while Contagiado != -100:
            if Contagiado == 0:
                Contagiado = True
                break
            elif Contagiado == 1:
                Contagiado = False
                break
            else:
                print("No se cuentra en el rango")
        Lista.append(Nombre)
        Lista.append(Apellido)
        Lista.append(Edad)
        Lista.append(Contagiado)
        Matriz.append(Lista)
    return Matriz
Corona_Virus = Covid()
print(Corona_Virus)
def Positivo(Matriz):
    Positivos = []
    for i in range(len(Matriz)):
        if Matriz[i][3] == True:
            Positivos.append(Matriz[i])
    return Positivos
Positivos = Positivo(Corona_Virus)
print(Positivos)
def Menor(Matriz):
    Menos = Matriz[0][2]
    for i in range(len(Matriz)):
        if Matriz[i][3] == True:
            if Matriz[i][2] < Menos:
                Menos = Matriz[i][2]
    return Menos
print(f"La menor edad de las personas fue de: {Menor(Corona_Virus)}")

####################################################################

def Division():
    A = int(input("Digite el Numero 1: "))
    B = int(input("Digite el Numero 2: "))
    while 1 != 0:
        A= A//B
        if A%2==0:
            print(f"El resultado es: {A} y es Par")
        else:
            print(f"El resultado es: {A} y es ImPar")
        if A == 0:
            break
Division()

#Siguiendo diccionarios


#?#?#?#TALLER#?#?#?#

#1

Dic ={}
Tamaño = int(input("Digite cuantas notas van a ver: "))
i = 1
while i<Tamaño:
    Nombre= "Nota"+str(i)
    Nota = float(input(f"Digite la nota{i} que saco: "))
    Dic[Nombre] = Nota
    i +=1
print(Dic)

#2

Nombre = input("Digite el Nombre: ")
Edad = int(input("Digite la Edad: "))
Direccion = input("Digite la Direccion: ")
Telefono = int(input("Digite el Telefono: "))
Dic = {"Name":Nombre, "Age":Edad,"Direction":Direccion, "Telephone":Telefono}
print(f"{Dic['Name']} tiene {Dic['Age']} años, vive en {Dic['Direction']} y su numero de telefono es {Dic['Telephone']}")

#3

Dic = {'Banano': 600, 'Mango':1000, 'Pera': 700, 'Manzana':300}
Fruta = input("Digite la fruta que desea: ")
Kilos = int(input("Digite la cantidad de kilos: "))
if Fruta in Dic:
    print(f"{Kilos}kilos de {Fruta} cuestan: {Dic[Fruta]*Kilos}")
else:
    print("La fruta no se encuentra")

#4

Morse = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}
Palabra = input("Digite la Palabra deseada: ")
Palabra = Palabra.upper()
Resultado = ""
for i in Palabra:
    Resultado += Morse[i]
print(Resultado)

#5

Almacen = {}
Tamaño = int(input("Digite la cantidad de celulares a registrar: "))
i = 0
while i < Tamaño:
    Nombre= "Celular"+str(i+1)
    Id = int(input(f"Digite el ID del celular{i+1}: "))
    Marca = input(f"Digite la Marca del celular{i+1}: ")
    Modelo = input(f"Digite el Modelo del celular{i+1}: ")
    Año = int(input(f"Digite el Año de elaboracion del celular{i+1}: "))
    Gama = input(f"Digite la Gama del celular{i+1} [Baja,Media,Alta]: ")
    Costo = int(input(f"Digite el Costo del celular{i+1}: "))
    Precio = int(input(f"Digite el Precio del celular{i+1}: "))
    Dic = {"ID":Id,"MARCA":Marca,"MODELO":Modelo,"AÑO":Año,"GAMA":Gama,"COSTO":Costo,"PRECIO":Precio}
    Almacen[Nombre] = Dic
    i +=1
print(Almacen)

#Almacen = {'Celular1': {'ID': 123, 'MARCA': 'Sapox2', 'MODELO': 'Sapo', 'AÑO': 123, 'GAMA': 'Alta','COSTO':1300, 'PRECIO': 1200}, 'Celular2': {'ID': 321, 'MARCA': 'Sapox2', 'MODELO': 'Sapox2', 'AÑO': 213, 'GAMA': 'Alto','COSTO':1100, 'PRECIO': 1199}}    
#for i in Dic:
    #print(i)
    #for j in Dic[i]:
        #print(Dic[i][j])

def Buscar(Dic):
    Id = int(input("Digite el ID a buscar: "))
    for i in Dic:
        if Id == Dic[i]['ID']:
            print(Dic[i])
Buscar(Almacen)
def Mostrar(Dic):
    Diccionario = {}
    Marca = int(input("Digite la Marca a buscar: "))
    for i in Dic:
        if Marca == Dic[i]['MARCA']:
            Diccionario[i] = Dic[i]
    print(Diccionario)
Mostrar(Almacen)
def Vender(Dic):
    Id = int(input("Digite el ID a buscar: "))
    for i in Dic.copy():
        if Id == Dic[i]['ID']:
            Celular = Dic.pop(i)
    print(Dic)
Vender(Almacen)
def Ganancia(Dic):
    Diccionario = {}
    for i in Dic:
        Diccionario[i] = Dic[i]['ID']
        Diccionario[i] = Dic[i]['PRECIO']-Dic[i]['COSTO']
    print(Diccionario)
Ganancia(Almacen)

#6

Estudiantes = [
    {'nombre':'Juan David',
     'codigo':'10000001',
     'carrera':'Ingeniería Electrónica',
     'edad':19,
     'materias':{'Algebra':2.1, 'Sonidos':4.3, 'Fisica':3.9, 'Ondas':2.2, 'Religion':4.6},
     'semestre':2
    },
    {'nombre':'Maria Claudia',
     'codigo':'10000002',
     'carrera':'Medicina',
     'edad':21,
     'materias':{'Textos escritos':5, 'Calculo':4, 'Fisica':2.9, 'Pediatría':2.8, 'Religion':4.9},
     'semestre':1
    },
    {'nombre':'Carmenza',
     'codigo':'10000003',
     'carrera':'Ingeniería Civil',
     'edad':21,
     'materias':{'Topografía':3.3, 'Máquinas':4.1, 'Textos escritos':3.4, 'Etica':2, 'Financiera':1.9},
     'semestre':4
    },
    {'nombre':'Luisa',
     'codigo':'10000004',
     'carrera':'Ingeniería de Alimentos',
     'edad':17,
     'materias':{'Algebra':3, 'Financiera':5, 'Cuerpo Humano':3.9, 'Proteinas':5, 'Auditoria':3.7},
     'semestre':4
    },
    {'nombre':'Juan Esteban',
     'codigo':'10000005',
     'carrera':'Artes escénicas',
     'edad':24,
     'materias':{'Teatro':1, 'Financiera':0.8, 'Audiciones':4.4, 'Etica':4.3, 'Expresión oral':1.1},
     'semestre':3
    },
    {'nombre':'Luis Felipe',
     'codigo':'10000006',
     'carrera':'Contaduría Pública',
     'edad':18,
     'materias':{'Matemáticas 1':3.2, 'Contabilidad':4.1, 'Humanidades':1.9, 'Etica':3.5, 'Religion':3.8},
     'semestre':7
    },
    {'nombre':'Carlos Mario',
     'codigo':'10000007',
     'carrera':'Medicina',
     'edad':20,
     'materias':{'Sistema circulatoria':1, 'Calculo':2, 'Fisica':3, 'Etica':4.4, 'Sistema digestivo':5},
     'semestre':6
    },
    {'nombre':'Juan Jacobo',
     'codigo':'10000008',
     'carrera':'Ingeniería Informática',
     'edad':19,
     'materias':{'Programación 1':3.2, 'Programación 2':0, 'Software':5, 'Bases de datos':5, 'Algebra':4.7},
     'semestre':1
    },
    {'nombre':'Andrea',
     'codigo':'10000009',
     'carrera':'Ingeniería Mecánica',
     'edad':21,
     'materias':{'Robots':1.7, 'Logística':2.5, 'Variables':3.8, 'Electrónica':4.2, 'Fisica':5},
     'semestre':7
    },
    {'nombre':'Valeria',
     'codigo':'100000010',
     'carrera':'Ingeniería Eléctrica',
     'edad':20,
     'materias':{'Algebra':3, 'Calculo':3, 'Fisica':3, 'Etica':3, 'Religion':4},
     'semestre':4
    }]

#A

Nombre = input("Digite el Nombre: ")
for i in range(len(Estudiantes)):
    if Nombre == Estudiantes[i]['nombre']:
        print(Estudiantes[i])

#B

Codigo = input("Digite el Codigo: ")
for i in range(len(Estudiantes)):
    if Codigo == Estudiantes[i]['codigo']:
        print(Estudiantes[i])

#C

Carrera = input("Digite la Carrera: ")
for i in range(len(Estudiantes)):
    if Carrera == Estudiantes[i]['carrera']:
        print(Estudiantes[i])

#D

Contador = 0
Carrera = input("Digite la Carrera: ")
for i in range(len(Estudiantes)):
    if Carrera == Estudiantes[i]['carrera']:
        Contador += 1
print(f"La cantidad de estudiantes que cursan la carrera son: {Contador}")

#E

Matriz = []
Semestre = int(input("Digite el Semestre: "))
for i in range(len(Estudiantes)):
    Lista = []
    if Semestre == Estudiantes[i]['semestre']:
        Lista.append(Estudiantes[i]['nombre'])
        Lista.append(Estudiantes[i]['codigo'])
        Matriz.append(Lista)
print(Matriz)

#F

Total = 0
Suma = 0
for i in range(len(Estudiantes)):
    Suma += Estudiantes[i]['edad']
    Total += 1
print(f"El promedio de los años es de: {Suma/Total}") 
                     
#G

Materia = input("Digite la Materia: ")
for i in range(len(Estudiantes)):
    for j in Estudiantes[i]['materias']:
        if Materia == j:
            if Estudiantes[i]['materias'][j] < 3.0:
                print(Estudiantes[i]['nombre'])

#H

Mayor = 0
for i in range(len(Estudiantes)):
    if Estudiantes[i]['semestre'] > Mayor:
        Mayor = Estudiantes[i]['semestre']
for j in range(len(Estudiantes)):
    if Estudiantes[j]['semestre'] == Mayor:
        print(Estudiantes[j]['nombre'])

#I

Matriz = []
for i in range(len(Estudiantes)):
    Total = 0
    Suma = 0
    Lista = []
    for j in Estudiantes[i]['materias']:
        Suma += Estudiantes[i]['materias'][j]
        Total += 1
    Promedio = Suma/Total
    Lista.append(Estudiantes[i]['nombre'])
    Lista.append(Promedio)
    Matriz.append(Lista)
print(Matriz)

#J

Aprobados = 0
Cursados = 0
Materia = input("Digite la Materia: ")
for i in range(len(Estudiantes)):
    for j in Estudiantes[i]['materias']:
        if Materia == j:
            Cursados += 1
            if Estudiantes[i]['materias'][j] >= 3.0:
                Aprobados +=1
print(f"El total de cursados fueron de: {Cursados} y los que aprobaron fueron: {Aprobados}")

#K
Edad_Menor = Estudiantes[0]['edad']
Materia = input("Digite la Materia: ")
for i in range(len(Estudiantes)):
    for j in Estudiantes[i]['materias']:
        if Materia == j:
            if Estudiantes[i]['materias'][j] >= 3.0:
                if Edad_Menor > Estudiantes[i]['edad']:
                    Edad_Menor = Estudiantes[i]['edad']
print(f"La edad del menor que gano la materia de {Materia} fue de: {Edad_Menor}")

# GUIA
from random import randrange
def cuenta (x,y):
    suma = 0
    for a in range (x-1,x+2):
        for b in range (y-1,y+2):
            if a>=0 and a<=l_matriz-1 and b>=0 and b<=l_matriz-1:
                if matriz[a][b]=="*":
                    suma = suma + 1
    return suma
def print_matriz (a):
    print "\n"
    for x in a:
        for y in x:
            print y," ",
        print "\n"
print "Reglas:"
print "     Ganas"
print "         a) Si descubres la posicion de todas las minas"
print "     Pierdes:"
print "         a) Si pisas una mina"
print "         b) Si fallas al indicar la posicion de una mina"
print "Configuracion:"
l_matriz = input (" 1- Ingresa largo:    ")
minas = input ("    2- Ingresa cantidad de minas:   ")
 
#Crear matriz oculta
matriz = []
for A in range (l_matriz):
    matriz2 = []
    for B in range (l_matriz):
        matriz2.append (0)
    matriz.append (matriz2)
#Crear matriz visible
matriz2 = []
for A in range (l_matriz):
    matriz3 = []
    for B in range (l_matriz):
        matriz3.append ("#")
    matriz2.append (matriz3)
#Rellenar matriz con minas
suma = 0
while suma!=minas:
    random1 = randrange(0,l_matriz)
    random2 = randrange(0,l_matriz)
    if matriz[random1][random2] != '*':
        matriz[random1][random2] = '*'
        suma = suma + 1
#Conteo de minas
for C in range (l_matriz):
    for D in range (l_matriz):
        e = cuenta(C,D)
        if matriz[C][D]!="*":
            matriz[C][D]=e
#Desarrollo del juego
suma = 0
while suma!=minas:
    print "\n"
    print "---------------------------------------------------------------------"
    z = raw_input ("Escribe MINA en caso que encuentres una o en caso contrario presiona Enter  ")
    if z=="MINA":
        print "Ingresa coordenadas de un lugar con minas"
        y2 = input ("   Ingresa coordenada x:  ") -1
        x2 = input ("   Ingresa coordenada y:  ") -1
        if matriz[x2][y2]=="*":
            suma = suma + 1
            matriz2[x2][y2]="*"
            if suma==minas:
                print_matriz (matriz2)
                print "Felicidades. Has ganado"
                break
        else:
            print_matriz (matriz)
            print "Has perdido"
            break
    print "Ingrese coordenadas de un lugar sin minas"
    y = input ("    Ingresa coordenada x:   ") -1
    x = input ("    Ingresa coordenada y:   ") -1
    if matriz[x][y]!="*":
        matriz2[x][y]=matriz[x][y]
    else:
        print_matriz (matriz)
        print "Has perdido"
        break
    print_matriz (matriz2)
    print "Aun te quedan",minas-suma,"minas por descubrir"
print "\n"
asdf = input ("Apreta un boton para cerrar")

#### ARCHIVOS ####

## pycharm
## Persistencia
## tipos de archivos (mp3, pdf, jpg, mp4, doc, gif, xls, txt, csv, html, ibook,)
## txt
## 1. Crear archivos
## 1.1 rutas absolutas
## 1.2 rutas relativas
## 2. Agregar a un archivo
## 3. Cargar un archivo
## 4. Archivos binarios o serializados
######## w --> escribir el archivo, si no existe, lo crea, y si ya existe, lo sobreescribe
######## a --> agreagar información al final del archivo
######## r --> leer un archivo

import marshal

def crearArchivo():
    archivo = open("numeros.txt","w")
    archivo.close()

def editarArchivo():
    archivo = open("numeros.txt","a")
    for i in range(5):
        archivo.write(input("digite un dato")+"\n")
    archivo.close()

def leerArchivo():
    archivo = open("numeros.txt","r")
    linea = archivo.readline()
    print(linea)
    archivo.close()


def leerVariasLineas():
    archivo = open("numeros.txt","r")
    lista = []
    linea = "cualquier cosa"
    while linea!="":
        linea = archivo.readline()
        lista.append(linea)
        
    archivo.close()
    print(lista)
    print(lista[1])

def editarArchivoLista():
    archivo = open("lista.txt","w")
    lista = [5,6,7,8,9,10]
    archivo.write(str(lista))
    archivo.close()

def leerArchivoLista():
    archivo = open("lista.txt","r")
    linea = archivo.readline()
    print(linea)
    print(linea[2])
    archivo.close()
    #print(lista)
    #print(lista[1])    

def crearSerializado():
    lista = {5:'H',6:'J'}
    archivo = open("numerosSerializado.gon", "bw")
    marshal.dump(lista,archivo)
    archivo.close()


def leerSerializado():
    archivo = open("numerosSerializado.gon", "br")
    dato = marshal.load(archivo)
    print(dato)
    print(dato[6])
    archivo.close()

crearSerializado()
leerSerializado()
#leerArchivoLista()
#editarArchivoLista()
#crearArchivo()
#editarArchivo()
#leerArchivo()
#leerVariasLineas()


#para buscaminas
Archivo = open("Guardar_Partida/Score.wembie","bw")
Archivo.close()
Archivo = open("Scores/Facil/Score.wembie","ba")
Archivo.close()
Archivo = open("Scores/Normal/Score.wembie","ba")
Archivo.close()
Archivo = open("Scores/Dificil/Score.wembie","ba")
Archivo.close()
Archivo = open("Scores/Wembie/Score.wembie","ba")
Archivo.close()

#Practica Archivos

#1.	Realice un programa que se encargue donde usted como usuario ingresa por medio de la instrucción input un texto largo (párrafo), ese texto debe quedar guardado en un archivo con extensión .doc posteriormente cree una función que se encargue de leer ese archivo .doc y lo muestre en pantalla con todos sus caracteres convertidos a minúscula.

import marshal
Texto = input("Digite el texto deseado: ")
Minusculas = Texto.lower()
Archivo = open("Texto.doc", "bw")
marshal.dump(Minusculas,Archivo)
Archivo.close()
def Leer():
    Archivo = open("Texto.doc", "br")
    Dato = marshal.load(Archivo)
    print(Dato)
    Archivo.close()
Leer()

###############
#PROYECTO ISIS#
###############


#Proyecto Jimenez
import random
import marshal
Lista = []
def Menu():
    print("Proyecto Jimenez")
    print("1. Nueva")
    print("2. Cargar")
def Niveles():
    print("1. Bajo")
    print("2. Medio")
    print("3. Alto")
def Bombas(Numero,Dinamita):
    Las_Bombas = []
    Empieza = 0
    while Empieza != Dinamita:
        Columna = random.randint(0,Numero)
        Fila = random.randint(0,Numero)
        if Tablero[Columna][Fila] == " #":
            Jugada = Columna, Fila
            Las_Bombas.append(Jugada)
            Empieza = Empieza + 1
    return Las_Bombas
Menu()
Main = int(input("Digite un Numero: "))
if Main == 1:
    Nombre = input("Digite su Nombre: ")
    Niveles()
    Levels = int(input("Digite un Numero: "))
    if Levels == 1:
        print("Nivel Bajo")
        Vidas = 3
        Jugadas = 0
        Points = 0
        Bandera = 0
        entro = 0
        Tablero = ["0"," 1"," 2"," 3"," 4"," 5"],["1"," #"," #"," #"," #"," #"],["2"," #"," #"," #"," #"," #"],["3"," #"," #"," #"," #"," #"],["4"," #"," #"," #"," #"," #"],["5"," #"," #"," #"," #"," #"]
        Granadas = Bombas(5,6)
        while Jugadas != 19:
            print(Tablero[0])
            print(Tablero[1])
            print(Tablero[2])
            print(Tablero[3])
            print(Tablero[4])
            print(Tablero[5])
            Columna = int(input("Digite la Columna del 1 al 5: "))
            Fila = int(input("Digite la Fila del 1 al 5: "))
            Jugada = Columna, Fila
            if Jugada not in Granadas :
                Tablero[Fila][Columna] = " O"
                if Bandera == 0:
                    Points = Points + 10
                    Bandera = 1
                else:
                    Points = Points + (Points*1.1)
                print("Puntos: ",Points)
            else:
                Tablero[Fila][Columna] = ":("
                Vidas = Vidas - 1
                print("Vidas: ",Vidas)
                print("Puntos: ",Points)
            if Vidas == 0:
                print(Tablero[0])
                print(Tablero[1])
                print(Tablero[2])
                print(Tablero[3])
                print(Tablero[4])
                print(Tablero[5])
                exit()
            if entro == 0:
                Lista.append(Nombre)
                Lista.append(Vidas)
                Lista.append(Jugadas)
                Lista.append(Points)
                Lista.append(Bandera)
                Lista.append(Tablero)
                Lista.append(Granadas)
                Lista.append(Levels)
            else:
                Lista[0] = Nombre
                Lista[1] = Vidas
                Lista[2] = Jugadas
                Lista[3] = Points
                Lista[4] = Bandera
                Lista[5] = Tablero
                Lista[6] = Granadas
                Lista[7] = Levels
                entro = 1             
            Archivo = open("GuardarPartida.jimenez","bw")
            marshal.dump(Lista,Archivo)
            Archivo.close()
        print("Ganaste")
if Main == 2:
    Archivo = open("GuardarPartida.jimenez","br")
    Dato = marshal.load(Archivo)
    Lista = Dato
    Archivo.close()
    if Lista[7] == 1:
        print("Nivel Bajo")
        Nombre = Lista[0]
        Vidas = Lista[1]
        Jugadas = Lista[2]
        Points = Lista[3]
        Bandera = Lista[4]
        Tablero = Lista[5]
        Granadas = Lista[6]
        Levels = Lista[7]
        while Jugadas != 19:
            print(Tablero[0])
            print(Tablero[1])
            print(Tablero[2])
            print(Tablero[3])
            print(Tablero[4])
            print(Tablero[5])
            Columna = int(input("Digite la Columna del 1 al 5: "))
            Fila = int(input("Digite la Fila del 1 al 5: "))
            Jugada = Columna, Fila
            if Jugada not in Granadas :
                Tablero[Fila][Columna] = " O"
                if Bandera == 0:
                    Points = Points + 10
                    Bandera = 1
                else:
                    Points = Points + (Points*1.1)
                print("Puntos: ",Points)
            else:
                Tablero[Fila][Columna] = ":("
                Vidas = Vidas - 1
                print("Vidas: ",Vidas)
                print("Puntos: ",Points)
            if Vidas == 0:
                print(Tablero[0])
                print(Tablero[1])
                print(Tablero[2])
                print(Tablero[3])
                print(Tablero[4])
                print(Tablero[5])
                exit()
            Lista[0] = Nombre
            Lista[1] = Vidas
            Lista[2] = Jugadas
            Lista[3] = Points
            Lista[4] = Bandera
            Lista[5] = Tablero
            Lista[6] = Granadas
            Lista[7] = Levels
            Archivo = open("GuardarPartida.jimenez","bw")
            marshal.dump(Lista,Archivo)
            Archivo.close()
        print("Ganaste")
 #################
####BUSCA MINAS####
 #################

import sys
import random
import operator
import marshal
###Informacion de Operator para entendimiento###
#The operator module exports a set of efficient functions corresponding to the intrinsic operators of Python. For example, operator.add(x, y) is equivalent to the expression x+y.
#Many function names are those used for special methods, without the double underscores. For backward compatibility, many of these have a variant with the double underscores kept.
#The variants without the double underscores are preferred for clarity.
#The functions fall into categories that perform object comparisons, logical operations, mathematical operations and sequence operations.
#The object comparison functions are useful for all objects, and are named after the rich comparison operators they support:
#https://www.analyticslane.com/2019/01/14/ordenacion-de-diccionarios-en-python-mediante-clave-o-valor/
#########################################
#Enumerate es una función incorporada de Python. Su utilidad no puede resumirse en una sola línea.
#Sin embargo, la mayoría de los recién llegados e incluso algunos programadores avanzados no lo saben.
#Nos permite recorrer algo y tener un contador automático. Aquí hay un ejemplo:
Diccionario = {}
print("============={ Busca Minas }=============")
print("============={ By : Wembie }=============")
print("")
print("( ͡° ͜ʖ ͡°) MENU ( ͡° ͜ʖ ͡°)")
print("1. Comenzar nueva partida.")
print("2. Continuar nuevamente.")
print("3. Salir.")
while 1 != 0:
    Menu = int(input("Digite el Numero deseado [1,2,3]: "))
    if Menu == 1 or Menu == 2 or Menu == 3:
        break
    else:
        print("👉Numero Invalido")
        print("👉Digitelo Nuevamente")
if Menu == 1:
    Nombre = input("Digita tu Nombre: ")
    print("ಠ_ಠ DIFICULTADES ಠ_ಠ")
    print("1. Facil.")
    print("2. Normal.")
    print("3. Dificil.")
    print("4. Wembie.")
    while 1 != 0:
        Dificultad = int(input("Digite el Numero deseado [1,2,3,4]: "))
        if Dificultad == 1 or Dificultad == 2 or Dificultad == 3 or Dificultad == 4:      
           break
        else:
            print("👉Numero Invalido")
            print("👉Digitelo Nuevamente")
    if Dificultad == 1:
        print("ᕦ( ͡° ͜ʖ ͡°)ᕤ BIENVENIDO AL NIVEL ᕦ( ͡° ͜ʖ ͡°)ᕤ")
        print("ᕦ( ͡° ͜ʖ ͡°)ᕤ       FACIL         ᕦ( ͡° ͜ʖ ͡°)ᕤ")
        Vidas = 3
        Bombas = 6
        Indice = 0
        Puntos = 0
        Bandera = 0
        Jugadas = []
        Ganar = 0
        Score = {}
        Archivo_Score = open("Scores/Facil/Score.wembie","br")
        Dato_Score = marshal.load(Archivo_Score)
        Score = Dato_Score
        Archivo_Score.close()
        Posicion = 0
        Tablero_Oculto = ["0"," 1"," 2"," 3"," 4"," 5"],["1"," O"," O"," O"," O"," O"],["2"," O"," O"," O"," O"," O"],["3"," O"," O"," O"," O"," O"],["4"," O"," O"," O"," O"," O"],["5"," O"," O"," O"," O"," O"]
        Tablero_Visible = ["0"," 1"," 2"," 3"," 4"," 5"],["1"," #"," #"," #"," #"," #"],["2"," #"," #"," #"," #"," #"],["3"," #"," #"," #"," #"," #"],["4"," #"," #"," #"," #"," #"],["5"," #"," #"," #"," #"," #"]
        while Indice != Bombas:
            X_Bombas = random.randint(0,5)
            Y_Bombas = random.randint(0,5)
            if Tablero_Oculto[Y_Bombas][X_Bombas] == " O":
                Tablero_Oculto[Y_Bombas][X_Bombas] = ":("
                Indice +=1
                None
        while Ganar != 19:
            if Vidas == 0:
                print(Tablero_Visible[0])
                print(Tablero_Visible[1])
                print(Tablero_Visible[2])
                print(Tablero_Visible[3])
                print(Tablero_Visible[4])
                print(Tablero_Visible[5])
                Score[Nombre] = Puntos
                Archivo_Score = open("Scores/Facil/Score.wembie","bw")
                marshal.dump(Score,Archivo_Score)
                Archivo_Score.close()
                Score_Ordenado = sorted(Score)
                Score_Ordenado = sorted(Score.items())
                Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
                print("👉Has Perdido!, Se te acabaron las vidas :(")
                print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
                for Wembie in enumerate(Score_Ordenado):
                    Posicion += 1
                    print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
                sys.exit()
            print(Tablero_Visible[0])
            print(Tablero_Visible[1])
            print(Tablero_Visible[2])
            print(Tablero_Visible[3])
            print(Tablero_Visible[4])
            print(Tablero_Visible[5])
            while 1 != 0:
                X = int(input("Digite la Posicion X [1,2,3,4,5]: "))
                if X == 1 or X == 2 or X == 3 or X == 4 or X == 5:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            while 1 != 0:
                Y = int(input("Digite la Posicion Y [1,2,3,4,5]: "))
                if Y == 1 or Y == 2 or Y == 3 or Y == 4 or Y == 5:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            Movimiento = X,Y
            Bombitas = 0
            if Movimiento not in Jugadas:
                if Tablero_Oculto[Y][X] == " O":
                    if Movimiento == (5, 1) or Movimiento == (5, 2) or Movimiento == (5, 3) or Movimiento == (5, 4):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (1, 5) or Movimiento == (2, 5) or Movimiento == (3, 5) or Movimiento == (4, 5):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (5, 5):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1 
                    else:
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1                             
                    Tablero_Visible[Y][X] = " "+str(Bombitas)
                    if Bandera == 0:
                        Puntos += 10
                        Bandera = 1
                    else:
                        Puntos += (Puntos*1.1)
                    print("👉Felicidades, No has pegado en una bomba!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                    Ganar += 1
                elif Tablero_Oculto[Y][X] == ":(":
                    Vidas -= 1
                    Tablero_Visible[Y][X] = ":("
                    print("👉Fallaste :C, has pegado en una bomba! BOOOM!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                Jugadas.append(Movimiento)
            else:
                print("👉Ya has hecho esa jugada!.. intenta nuevamente")
            Diccionario['Nombre'] = Nombre
            Diccionario['Dificultad'] = Dificultad
            Diccionario['Tablero_Oculto'] = Tablero_Oculto
            Diccionario['Tablero_Visible'] = Tablero_Visible
            Diccionario['Vidas'] = Vidas
            Diccionario['Jugadas'] = Jugadas
            Diccionario['Ganar'] = Ganar
            Diccionario['Bandera'] = Bandera
            Diccionario['Puntos'] = Puntos
            Archivo = open("Guardar_Partida/Partida.wembie","bw")
            marshal.dump(Diccionario,Archivo)
            Archivo.close()
        print("👉!!!!!!!!!!!!!!!!!!Felicidades!!!!!!!!!!!!!!!!!!!!")
        print("👉!!!!!!!!!!!!!!!!! HAS GANADO !!!!!!!!!!!!!!!!!!!!")
        Score[Nombre] = Puntos
        Archivo_Score = open("Scores/Facil/Score.wembie","bw")
        marshal.dump(Score,Archivo_Score)
        Archivo_Score.close()            
        Score_Ordenado = sorted(Score)
        Score_Ordenado = sorted(Score.items())
        Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
        print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
        for Wembie in enumerate(Score_Ordenado):
            Posicion += 1
            print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
    if Dificultad == 2:
        print("¯\_(ツ)_/¯ BIENVENIDO AL NIVEL ¯\_(ツ)_/¯")
        print("¯\_(ツ)_/¯       NORMAL        ¯\_(ツ)_/¯")
        Vidas = 3
        Bombas = 10
        Indice = 0
        Puntos = 0
        Bandera = 0
        Jugadas = []
        Ganar = 0
        Score = {}
        Archivo_Score = open("Scores/Normal/Score.wembie","br")
        Dato_Score = marshal.load(Archivo_Score)
        Score = Dato_Score
        Archivo_Score.close()
        Posicion = 0
        Tablero_Oculto = ["0"," 1"," 2"," 3"," 4"," 5", " 6"," 7"],["1"," O"," O"," O"," O"," O"," O"," O"],["2"," O"," O"," O"," O"," O"," O"," O"],["3"," O"," O"," O"," O"," O"," O"," O"],["4"," O"," O"," O"," O"," O"," O"," O"],["5"," O"," O"," O"," O"," O"," O"," O"],["6"," O"," O"," O"," O"," O"," O"," O"],["7"," O"," O"," O"," O"," O"," O"," O"]
        Tablero_Visible = ["0"," 1"," 2"," 3"," 4"," 5", " 6"," 7"],["1"," #"," #"," #"," #"," #"," #"," #"],["2"," #"," #"," #"," #"," #"," #"," #"],["3"," #"," #"," #"," #"," #"," #"," #"],["4"," #"," #"," #"," #"," #"," #"," #"],["5"," #"," #"," #"," #"," #"," #"," #"],["6"," #"," #"," #"," #"," #"," #"," #"],["7"," #"," #"," #"," #"," #"," #"," #"]
        while Indice != Bombas:
            X_Bombas = random.randint(0,7)
            Y_Bombas = random.randint(0,7)
            if Tablero_Oculto[Y_Bombas][X_Bombas] == " O":
                Tablero_Oculto[Y_Bombas][X_Bombas] = ":("
                Indice +=1    
        while Ganar != 39:
            if Vidas == 0:
                print(Tablero_Visible[0])
                print(Tablero_Visible[1])
                print(Tablero_Visible[2])
                print(Tablero_Visible[3])
                print(Tablero_Visible[4])
                print(Tablero_Visible[5])
                print(Tablero_Visible[6])
                print(Tablero_Visible[7])
                Score[Nombre] = Puntos
                Archivo_Score = open("Scores/Normal/Score.wembie","bw")
                marshal.dump(Score,Archivo_Score)
                Archivo_Score.close()
                Score_Ordenado = sorted(Score)
                Score_Ordenado = sorted(Score.items())
                Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
                print("👉Has Perdido!, Se te acabaron las vidas :(")
                print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
                for Wembie in enumerate(Score_Ordenado):
                    Posicion += 1
                    print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
                sys.exit()
            print(Tablero_Visible[0])
            print(Tablero_Visible[1])
            print(Tablero_Visible[2])
            print(Tablero_Visible[3])
            print(Tablero_Visible[4])
            print(Tablero_Visible[5])
            print(Tablero_Visible[6])
            print(Tablero_Visible[7])
            while 1 != 0:
                X = int(input("Digite la Posicion X [1,2,3,4,5,6,7]: "))
                if X == 1 or X == 2 or X == 3 or X == 4 or X == 5 or X == 6 or X == 7:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            while 1 != 0:
                Y = int(input("Digite la Posicion Y [1,2,3,4,5,6,7]: "))
                if Y == 1 or Y == 2 or Y == 3 or Y == 4 or Y == 5 or Y == 6 or Y == 7:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            Movimiento = X,Y
            Bombitas = 0
            if Movimiento not in Jugadas:
                if Tablero_Oculto[Y][X] == " O":
                    if Movimiento == (7, 1) or Movimiento == (7, 2) or Movimiento == (7, 3) or Movimiento == (7, 4) or Movimiento == (7, 5) or Movimiento == (7, 6):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (1, 7) or Movimiento == (2, 7) or Movimiento == (3, 7) or Movimiento == (4, 7) or Movimiento == (5, 7) or Movimiento == (6, 7):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (7, 7):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1 
                    else:
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1                             
                    Tablero_Visible[Y][X] = " "+str(Bombitas)
                    if Bandera == 0:
                        Puntos += 10
                        Bandera = 1
                    else:
                        Puntos += (Puntos*1.1)
                    print("👉Felicidades, No has pegado en una bomba!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                    Ganar += 1
                elif Tablero_Oculto[Y][X] == ":(":
                    Vidas -= 1
                    Tablero_Visible[Y][X] = ":("
                    print("👉Fallaste :C, has pegado en una bomba! BOOOM!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                Jugadas.append(Movimiento)
            else:
                print("👉Ya has hecho esa jugada!.. intenta nuevamente")
            Diccionario['Nombre'] = Nombre
            Diccionario['Dificultad'] = Dificultad
            Diccionario['Tablero_Oculto'] = Tablero_Oculto
            Diccionario['Tablero_Visible'] = Tablero_Visible
            Diccionario['Vidas'] = Vidas
            Diccionario['Jugadas'] = Jugadas
            Diccionario['Ganar'] = Ganar
            Diccionario['Bandera'] = Bandera
            Diccionario['Puntos'] = Puntos
            Archivo = open("Guardar_Partida/Partida.wembie","bw")
            marshal.dump(Diccionario,Archivo)
            Archivo.close()
        print("👉!!!!!!!!!!!!!!!!!!Felicidades!!!!!!!!!!!!!!!!!!!!")
        print("👉!!!!!!!!!!!!!!!!! HAS GANADO !!!!!!!!!!!!!!!!!!!!")
        Score[Nombre] = Puntos
        Archivo_Score = open("Scores/Normal/Score.wembie","bw")
        marshal.dump(Score,Archivo_Score)
        Archivo_Score.close()
        Score_Ordenado = sorted(Score)
        Score_Ordenado = sorted(Score.items())
        Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
        print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
        for Wembie in enumerate(Score_Ordenado):
            Posicion += 1
            print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
    if Dificultad == 3:
        print("[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] BIENVENIDO AL NIVEL [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]") 
        print("[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]       DIFICIL       [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]")
        Vidas = 3
        Bombas = 14
        Indice = 0
        Puntos = 0
        Bandera = 0
        Jugadas = []
        Ganar = 0
        Score = {}
        Archivo_Score = open("Scores/Dificil/Score.wembie","br")
        Dato_Score = marshal.load(Archivo_Score)
        Score = Dato_Score
        Posicion = 0
        Tablero_Oculto = ["0"," 1"," 2"," 3"," 4"," 5", " 6"," 7"," 8"," 9"],["1"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["2"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["3"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["4"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["5"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["6"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["7"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["8"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["9"," O"," O"," O"," O"," O"," O"," O"," O"," O"]
        Tablero_Visible = ["0"," 1"," 2"," 3"," 4"," 5", " 6"," 7"," 8"," 9"],["1"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["2"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["3"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["4"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["5"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["6"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["7"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["8"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["9"," #"," #"," #"," #"," #"," #"," #"," #"," #"]
        while Indice != Bombas:
            X_Bombas = random.randint(0,9)
            Y_Bombas = random.randint(0,9)
            if Tablero_Oculto[Y_Bombas][X_Bombas] == " O":
                Tablero_Oculto[Y_Bombas][X_Bombas] = ":("
                Indice +=1    
        while Ganar != 67:
            if Vidas == 0:
                print(Tablero_Visible[0])
                print(Tablero_Visible[1])
                print(Tablero_Visible[2])
                print(Tablero_Visible[3])
                print(Tablero_Visible[4])
                print(Tablero_Visible[5])
                print(Tablero_Visible[6])
                print(Tablero_Visible[7])
                print(Tablero_Visible[8])
                print(Tablero_Visible[9])
                Score[Nombre] = Puntos
                Archivo_Score = open("Scores/Dificil/Score.wembie","bw")
                marshal.dump(Score,Archivo_Score)
                Archivo_Score.close()
                Score_Ordenado = sorted(Score)
                Score_Ordenado = sorted(Score.items())
                Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
                print("👉Has Perdido!, Se te acabaron las vidas :(")
                print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
                for Wembie in enumerate(Score_Ordenado):
                    Posicion += 1
                    print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
                sys.exit()
            print(Tablero_Visible[0])
            print(Tablero_Visible[1])
            print(Tablero_Visible[2])
            print(Tablero_Visible[3])
            print(Tablero_Visible[4])
            print(Tablero_Visible[5])
            print(Tablero_Visible[6])
            print(Tablero_Visible[7])
            print(Tablero_Visible[8])
            print(Tablero_Visible[9])
            while 1 != 0:
                X = int(input("Digite la Posicion X [1,2,3,4,5,6,7,8,9]: "))
                if X == 1 or X == 2 or X == 3 or X == 4 or X == 5 or X == 6 or X == 7 or X == 8 or X == 9:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            while 1 != 0:
                Y = int(input("Digite la Posicion Y [1,2,3,4,5,6,7,8,9]: "))
                if Y == 1 or Y == 2 or Y == 3 or Y == 4 or Y == 5 or Y == 6 or Y == 7 or Y == 8 or Y == 9:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            Movimiento = X,Y
            Bombitas = 0
            if Movimiento not in Jugadas:
                if Tablero_Oculto[Y][X] == " O":
                    if Movimiento == (9, 1) or Movimiento == (9, 2) or Movimiento == (9, 3) or Movimiento == (9, 4) or Movimiento == (9, 5) or Movimiento == (9, 6) or Movimiento == (9, 7) or Movimiento == (9, 8):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (1, 9) or Movimiento == (2, 9) or Movimiento == (3, 9) or Movimiento == (4, 9) or Movimiento == (5, 9) or Movimiento == (6, 9) or Movimiento == (7, 9) or Movimiento == (8, 9):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (9, 9):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1 
                    else:
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1                             
                    Tablero_Visible[Y][X] = " "+str(Bombitas)
                    if Bandera == 0:
                        Puntos += 10
                        Bandera = 1
                    else:
                        Puntos += (Puntos*1.1)
                    print("👉Felicidades, No has pegado en una bomba!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                    Ganar += 1
                elif Tablero_Oculto[Y][X] == ":(":
                    Vidas -= 1
                    Tablero_Visible[Y][X] = ":("
                    print("👉Fallaste :C, has pegado en una bomba! BOOOM!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                Jugadas.append(Movimiento)
            else:
                print("👉Ya has hecho esa jugada!.. intenta nuevamente")
            Diccionario['Nombre'] = Nombre
            Diccionario['Dificultad'] = Dificultad
            Diccionario['Tablero_Oculto'] = Tablero_Oculto
            Diccionario['Tablero_Visible'] = Tablero_Visible
            Diccionario['Vidas'] = Vidas
            Diccionario['Jugadas'] = Jugadas
            Diccionario['Ganar'] = Ganar
            Diccionario['Bandera'] = Bandera
            Diccionario['Puntos'] = Puntos
            Archivo = open("Guardar_Partida/Partida.wembie","bw")
            marshal.dump(Diccionario,Archivo)
            Archivo.close()
        print("👉!!!!!!!!!!!!!!!!!!Felicidades!!!!!!!!!!!!!!!!!!!!")
        print("👉!!!!!!!!!!!!!!!!! HAS GANADO !!!!!!!!!!!!!!!!!!!!")
        Score[Nombre] = Puntos
        Archivo_Score = open("Scores/Dificil/Score.wembie","bw")
        marshal.dump(Score,Archivo_Score)
        Archivo_Score.close()
        Score_Ordenado = sorted(Score)
        Score_Ordenado = sorted(Score.items())
        Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
        print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
        for Wembie in enumerate(Score_Ordenado):
            Posicion += 1
            print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
    if Dificultad == 4:
        print("㍿㍿㍿㍿㍿㍿㍿ BIENVENIDO AL NIVEL ㍿㍿㍿㍿㍿㍿㍿") 
        print("㍿㍿㍿㍿㍿㍿㍿        WEMBIE       ㍿㍿㍿㍿㍿㍿㍿")
        Vidas = 3
        Bombas = 25
        Indice = 0
        Puntos = 0
        Bandera = 0
        Jugadas = []
        Ganar = 0
        Score = {}
        Archivo_Score = open("Scores/Wembie/Score.wembie","br")
        Dato_Score = marshal.load(Archivo_Score)
        Score = Dato_Score
        Posicion = 0
        Tablero_Oculto = [" 0"," 1"," 2"," 3"," 4"," 5", " 6"," 7"," 8"," 9","10","11","12"],[" 1"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],[" 2"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],[" 3"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],[" 4"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],[" 5"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],[" 6"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],[" 7"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],[" 8"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],[" 9"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["10"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["11"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"],["12"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"," O"]
        Tablero_Visible = [" 0"," 1"," 2"," 3"," 4"," 5", " 6"," 7"," 8"," 9","10","11","12"],[" 1"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],[" 2"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],[" 3"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],[" 4"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],[" 5"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],[" 6"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],[" 7"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],[" 8"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],[" 9"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["10"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["11"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"],["12"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"," #"]
        while Indice != Bombas:
            X_Bombas = random.randint(0,12)
            Y_Bombas = random.randint(0,12)
            if Tablero_Oculto[Y_Bombas][X_Bombas] == " O":
                Tablero_Oculto[Y_Bombas][X_Bombas] = ":("
                Indice +=1    
        while Ganar != 119:
            if Vidas == 0:
                print(Tablero_Visible[0])
                print(Tablero_Visible[1])
                print(Tablero_Visible[2])
                print(Tablero_Visible[3])
                print(Tablero_Visible[4])
                print(Tablero_Visible[5])
                print(Tablero_Visible[6])
                print(Tablero_Visible[7])
                print(Tablero_Visible[8])
                print(Tablero_Visible[9])
                print(Tablero_Visible[10])
                print(Tablero_Visible[11])
                print(Tablero_Visible[12])
                Score[Nombre] = Puntos
                Archivo_Score = open("Scores/Wembie/Score.wembie","bw")
                marshal.dump(Score,Archivo_Score)
                Archivo_Score.close()
                Score_Ordenado = sorted(Score)
                Score_Ordenado = sorted(Score.items())
                Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
                print("👉Has Perdido!, Se te acabaron las vidas :(")
                print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
                for Wembie in enumerate(Score_Ordenado):
                    Posicion += 1
                    print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
                sys.exit()
            print(Tablero_Visible[0])
            print(Tablero_Visible[1])
            print(Tablero_Visible[2])
            print(Tablero_Visible[3])
            print(Tablero_Visible[4])
            print(Tablero_Visible[5])
            print(Tablero_Visible[6])
            print(Tablero_Visible[7])
            print(Tablero_Visible[8])
            print(Tablero_Visible[9])
            print(Tablero_Visible[10])
            print(Tablero_Visible[11])
            print(Tablero_Visible[12])
            while 1 != 0:
                X = int(input("Digite la Posicion X [1,2,3,4,5,6,7,8,9,10,11,12]: "))
                if X == 1 or X == 2 or X == 3 or X == 4 or X == 5 or X == 6 or X == 7 or X == 8 or X == 9 or X == 10 or X == 11 or X == 12:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            while 1 != 0:
                Y = int(input("Digite la Posicion Y [1,2,3,4,5,6,7,8,9,10,11,12]: "))
                if Y == 1 or Y == 2 or Y == 3 or Y == 4 or Y == 5 or Y == 6 or Y == 7 or Y == 8 or Y == 9 or Y == 10 or Y == 11 or Y == 12:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            Movimiento = X,Y
            Bombitas = 0
            if Movimiento not in Jugadas:
                if Tablero_Oculto[Y][X] == " O":
                    if Movimiento == (12, 1) or Movimiento == (12, 2) or Movimiento == (12, 3) or Movimiento == (12, 4) or Movimiento == (12, 5) or Movimiento == (12, 6) or Movimiento == (12, 7) or Movimiento == (12, 8) or Movimiento == (12, 9) or Movimiento == (12, 10) or Movimiento == (12, 11):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (1, 12) or Movimiento == (2, 12) or Movimiento == (3, 12) or Movimiento == (4, 12) or Movimiento == (5, 12) or Movimiento == (6, 12) or Movimiento == (7, 12) or Movimiento == (8, 12) or Movimiento == (9, 12) or Movimiento == (10, 12) or Movimiento == (11, 12):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (12, 12):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1 
                    else:
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1                             
                    Tablero_Visible[Y][X] = " "+str(Bombitas)
                    if Bandera == 0:
                        Puntos += 10
                        Bandera = 1
                    else:
                        Puntos += (Puntos*1.1)
                    print("👉Felicidades, No has pegado en una bomba!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                    Ganar += 1
                elif Tablero_Oculto[Y][X] == ":(":
                    Vidas -= 1
                    Tablero_Visible[Y][X] = ":("
                    print("👉Fallaste :C, has pegado en una bomba! BOOOM!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                Jugadas.append(Movimiento)
            else:
                print("👉Ya has hecho esa jugada!.. intenta nuevamente")
            Diccionario['Nombre'] = Nombre
            Diccionario['Dificultad'] = Dificultad
            Diccionario['Tablero_Oculto'] = Tablero_Oculto
            Diccionario['Tablero_Visible'] = Tablero_Visible
            Diccionario['Vidas'] = Vidas
            Diccionario['Jugadas'] = Jugadas
            Diccionario['Ganar'] = Ganar
            Diccionario['Bandera'] = Bandera
            Diccionario['Puntos'] = Puntos
            Archivo = open("Guardar_Partida/Partida.wembie","bw")
            marshal.dump(Diccionario,Archivo)
            Archivo.close()
        print("👉!!!!!!!!!!!!!!!!!!Felicidades!!!!!!!!!!!!!!!!!!!!")
        print("👉!!!!!!!!!!!!!!!!! HAS GANADO !!!!!!!!!!!!!!!!!!!!")
        Score[Nombre] = Puntos
        Archivo_Score = open("Scores/Wembie/Score.wembie","bw")
        marshal.dump(Score,Archivo_Score)
        Archivo_Score.close()
        Score_Ordenado = sorted(Score)
        Score_Ordenado = sorted(Score.items())
        Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
        print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
        for Wembie in enumerate(Score_Ordenado):
            Posicion += 1
            print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
if Menu == 2: #CONTINUAR LA PARTIDA
    Archivo = open("Guardar_Partida/Partida.wembie","br")
    Dato = marshal.load(Archivo)
    Diccionario = Dato
    Archivo.close()
    if Diccionario['Dificultad'] == 1:
        print("ᕦ( ͡° ͜ʖ ͡°)ᕤ BIENVENIDO AL NIVEL ᕦ( ͡° ͜ʖ ͡°)ᕤ")
        print("ᕦ( ͡° ͜ʖ ͡°)ᕤ       FACIL         ᕦ( ͡° ͜ʖ ͡°)ᕤ")
        print("ᕦ( ͡° ͜ʖ ͡°)ᕤ     DE NUEVO :V     ᕦ( ͡° ͜ʖ ͡°)ᕤ")
        Dificultad = Diccionario['Dificultad']
        Nombre = Diccionario['Nombre']
        Vidas = Diccionario['Vidas']
        Puntos = Diccionario['Puntos']
        Bandera = Diccionario['Bandera']
        Jugadas = Diccionario['Jugadas']
        Ganar = Diccionario['Ganar']
        Score = {}
        Archivo_Score = open("Scores/Facil/Score.wembie","br")
        Dato_Score = marshal.load(Archivo_Score)
        Score = Dato_Score
        Archivo_Score.close()
        Posicion = 0
        Tablero_Oculto = Diccionario['Tablero_Oculto']
        Tablero_Visible = Diccionario['Tablero_Visible']
        while Ganar != 19:
            if Vidas == 0:
                print(Tablero_Visible[0])
                print(Tablero_Visible[1])
                print(Tablero_Visible[2])
                print(Tablero_Visible[3])
                print(Tablero_Visible[4])
                print(Tablero_Visible[5])
                Score[Nombre] = Puntos
                Archivo_Score = open("Scores/Facil/Score.wembie","bw")
                marshal.dump(Score,Archivo_Score)
                Archivo_Score.close()
                Score_Ordenado = sorted(Score)
                Score_Ordenado = sorted(Score.items())
                Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
                print("👉Has Perdido!, Se te acabaron las vidas :(")
                print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
                for Wembie in enumerate(Score_Ordenado):
                    Posicion += 1
                    print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
                sys.exit()
            print(Tablero_Visible[0])
            print(Tablero_Visible[1])
            print(Tablero_Visible[2])
            print(Tablero_Visible[3])
            print(Tablero_Visible[4])
            print(Tablero_Visible[5])
            while 1 != 0:
                X = int(input("Digite la Posicion X [1,2,3,4,5]: "))
                if X == 1 or X == 2 or X == 3 or X == 4 or X == 5:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            while 1 != 0:
                Y = int(input("Digite la Posicion Y [1,2,3,4,5]: "))
                if Y == 1 or Y == 2 or Y == 3 or Y == 4 or Y == 5:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            Movimiento = X,Y
            Bombitas = 0
            if Movimiento not in Jugadas:
                if Tablero_Oculto[Y][X] == " O":
                    if Movimiento == (5, 1) or Movimiento == (5, 2) or Movimiento == (5, 3) or Movimiento == (5, 4):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (1, 5) or Movimiento == (2, 5) or Movimiento == (3, 5) or Movimiento == (4, 5):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (5, 5):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1 
                    else:
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1                             
                    Tablero_Visible[Y][X] = " "+str(Bombitas)
                    if Bandera == 0:
                        Puntos += 10
                        Bandera = 1
                    else:
                        Puntos += (Puntos*1.1)
                    print("👉Felicidades, No has pegado en una bomba!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                    Ganar += 1
                elif Tablero_Oculto[Y][X] == ":(":
                    Vidas -= 1
                    Tablero_Visible[Y][X] = ":("
                    print("👉Fallaste :C, has pegado en una bomba! BOOOM!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                Jugadas.append(Movimiento)
            else:
                print("👉Ya has hecho esa jugada!.. intenta nuevamente")
            Diccionario['Nombre'] = Nombre
            Diccionario['Dificultad'] = Dificultad
            Diccionario['Tablero_Oculto'] = Tablero_Oculto
            Diccionario['Tablero_Visible'] = Tablero_Visible
            Diccionario['Vidas'] = Vidas
            Diccionario['Jugadas'] = Jugadas
            Diccionario['Ganar'] = Ganar
            Diccionario['Bandera'] = Bandera
            Diccionario['Puntos'] = Puntos
            Archivo = open("Guardar_Partida/Partida.wembie","bw")
            marshal.dump(Diccionario,Archivo)
            Archivo.close()
        print("👉!!!!!!!!!!!!!!!!!!Felicidades!!!!!!!!!!!!!!!!!!!!")
        print("👉!!!!!!!!!!!!!!!!! HAS GANADO !!!!!!!!!!!!!!!!!!!!")
        Score[Nombre] = Puntos
        Archivo_Score = open("Scores/Facil/Score.wembie","bw")
        marshal.dump(Score,Archivo_Score)
        Archivo_Score.close()
        Score_Ordenado = sorted(Score)
        Score_Ordenado = sorted(Score.items())
        Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
        print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
        for Wembie in enumerate(Score_Ordenado):
            Posicion += 1
            print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
    if Diccionario['Dificultad'] == 2:
        print("¯\_(ツ)_/¯ BIENVENIDO AL NIVEL ¯\_(ツ)_/¯")
        print("¯\_(ツ)_/¯       NORMAL        ¯\_(ツ)_/¯")
        print("¯\_(ツ)_/¯     DE NUEVO :V     ¯\_(ツ)_/¯")
        Dificultad = Diccionario['Dificultad']
        Nombre = Diccionario['Nombre']
        Vidas = Diccionario['Vidas']
        Puntos = Diccionario['Puntos']
        Bandera = Diccionario['Bandera']
        Jugadas = Diccionario['Jugadas']
        Ganar = Diccionario['Ganar']
        Score = {}
        Archivo_Score = open("Scores/Normal/Score.wembie","br")
        Dato_Score = marshal.load(Archivo_Score)
        Score = Dato_Score
        Archivo_Score.close()
        Posicion = 0
        Tablero_Oculto = Diccionario['Tablero_Oculto']
        Tablero_Visible = Diccionario['Tablero_Visible']   
        while Ganar != 39:
            if Vidas == 0:
                print(Tablero_Visible[0])
                print(Tablero_Visible[1])
                print(Tablero_Visible[2])
                print(Tablero_Visible[3])
                print(Tablero_Visible[4])
                print(Tablero_Visible[5])
                print(Tablero_Visible[6])
                print(Tablero_Visible[7])
                Score[Nombre] = Puntos
                Archivo_Score = open("Scores/Normal/Score.wembie","bw")
                marshal.dump(Score,Archivo_Score)
                Archivo_Score.close()
                Score_Ordenado = sorted(Score)
                Score_Ordenado = sorted(Score.items())
                Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
                print("👉Has Perdido!, Se te acabaron las vidas :(")
                print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
                for Wembie in enumerate(Score_Ordenado):
                    Posicion += 1
                    print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
                sys.exit()
            print(Tablero_Visible[0])
            print(Tablero_Visible[1])
            print(Tablero_Visible[2])
            print(Tablero_Visible[3])
            print(Tablero_Visible[4])
            print(Tablero_Visible[5])
            print(Tablero_Visible[6])
            print(Tablero_Visible[7])
            while 1 != 0:
                X = int(input("Digite la Posicion X [1,2,3,4,5,6,7]: "))
                if X == 1 or X == 2 or X == 3 or X == 4 or X == 5 or X == 6 or X == 7:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            while 1 != 0:
                Y = int(input("Digite la Posicion Y [1,2,3,4,5,6,7]: "))
                if Y == 1 or Y == 2 or Y == 3 or Y == 4 or Y == 5 or Y == 6 or Y == 7:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            Movimiento = X,Y
            Bombitas = 0
            if Movimiento not in Jugadas:
                if Tablero_Oculto[Y][X] == " O":
                    if Movimiento == (7, 1) or Movimiento == (7, 2) or Movimiento == (7, 3) or Movimiento == (7, 4) or Movimiento == (7, 5) or Movimiento == (7, 6):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (1, 7) or Movimiento == (2, 7) or Movimiento == (3, 7) or Movimiento == (4, 7) or Movimiento == (5, 7) or Movimiento == (6, 7):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (7, 7):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1 
                    else:
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1                             
                    Tablero_Visible[Y][X] = " "+str(Bombitas)
                    if Bandera == 0:
                        Puntos += 10
                        Bandera = 1
                    else:
                        Puntos += (Puntos*1.1)
                    print("👉Felicidades, No has pegado en una bomba!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                    Ganar += 1
                elif Tablero_Oculto[Y][X] == ":(":
                    Vidas -= 1
                    Tablero_Visible[Y][X] = ":("
                    print("👉Fallaste :C, has pegado en una bomba! BOOOM!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                Jugadas.append(Movimiento)
            else:
                print("👉Ya has hecho esa jugada!.. intenta nuevamente")
            Diccionario['Nombre'] = Nombre
            Diccionario['Dificultad'] = Dificultad
            Diccionario['Tablero_Oculto'] = Tablero_Oculto
            Diccionario['Tablero_Visible'] = Tablero_Visible
            Diccionario['Vidas'] = Vidas
            Diccionario['Jugadas'] = Jugadas
            Diccionario['Ganar'] = Ganar
            Diccionario['Bandera'] = Bandera
            Diccionario['Puntos'] = Puntos
            Archivo = open("Guardar_Partida/Partida.wembie","bw")
            marshal.dump(Diccionario,Archivo)
            Archivo.close()
        print("👉!!!!!!!!!!!!!!!!!!Felicidades!!!!!!!!!!!!!!!!!!!!")
        print("👉!!!!!!!!!!!!!!!!! HAS GANADO !!!!!!!!!!!!!!!!!!!!")
        Score[Nombre] = Puntos
        Archivo_Score = open("Scores/Normal/Score.wembie","bw")
        marshal.dump(Score,Archivo_Score)
        Archivo_Score.close()
        Score_Ordenado = sorted(Score)
        Score_Ordenado = sorted(Score.items())
        Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
        print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
        for Wembie in enumerate(Score_Ordenado):
            Posicion += 1
            print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
    if Diccionario['Dificultad'] == 3:
        print("[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅] BIENVENIDO AL NIVEL [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]") 
        print("[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]       DIFICIL       [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]")
        print("[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]     DE NUEVO :V     [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]")
        Dificultad = Diccionario['Dificultad']
        Nombre = Diccionario['Nombre']
        Vidas = Diccionario['Vidas']
        Puntos = Diccionario['Puntos']
        Bandera = Diccionario['Bandera']
        Jugadas = Diccionario['Jugadas']
        Ganar = Diccionario['Ganar']
        Score = {}
        Archivo_Score = open("Scores/Dificil/Score.wembie","br")
        Dato_Score = marshal.load(Archivo_Score)
        Score = Dato_Score
        Archivo_Score.close()
        Posicion = 0
        Tablero_Oculto = Diccionario['Tablero_Oculto']
        Tablero_Visible = Diccionario['Tablero_Visible']  
        while Ganar != 67:
            if Vidas == 0:
                print(Tablero_Visible[0])
                print(Tablero_Visible[1])
                print(Tablero_Visible[2])
                print(Tablero_Visible[3])
                print(Tablero_Visible[4])
                print(Tablero_Visible[5])
                print(Tablero_Visible[6])
                print(Tablero_Visible[7])
                print(Tablero_Visible[8])
                print(Tablero_Visible[9])
                Score[Nombre] = Puntos
                Archivo_Score = open("Scores/Dificil/Score.wembie","bw")
                marshal.dump(Score,Archivo_Score)
                Archivo_Score.close()
                Score_Ordenado = sorted(Score)
                Score_Ordenado = sorted(Score.items())
                Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
                print("👉Has Perdido!, Se te acabaron las vidas :(")
                print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
                for Wembie in enumerate(Score_Ordenado):
                    Posicion += 1
                    print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
                sys.exit()
            print(Tablero_Visible[0])
            print(Tablero_Visible[1])
            print(Tablero_Visible[2])
            print(Tablero_Visible[3])
            print(Tablero_Visible[4])
            print(Tablero_Visible[5])
            print(Tablero_Visible[6])
            print(Tablero_Visible[7])
            print(Tablero_Visible[8])
            print(Tablero_Visible[9])
            while 1 != 0:
                X = int(input("Digite la Posicion X [1,2,3,4,5,6,7,8,9]: "))
                if X == 1 or X == 2 or X == 3 or X == 4 or X == 5 or X == 6 or X == 7 or X == 8 or X == 9:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            while 1 != 0:
                Y = int(input("Digite la Posicion Y [1,2,3,4,5,6,7,8,9]: "))
                if Y == 1 or Y == 2 or Y == 3 or Y == 4 or Y == 5 or Y == 6 or Y == 7 or Y == 8 or Y == 9:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            Movimiento = X,Y
            Bombitas = 0
            if Movimiento not in Jugadas:
                if Tablero_Oculto[Y][X] == " O":
                    if Movimiento == (9, 1) or Movimiento == (9, 2) or Movimiento == (9, 3) or Movimiento == (9, 4) or Movimiento == (9, 5) or Movimiento == (9, 6) or Movimiento == (9, 7) or Movimiento == (9, 8):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (1, 9) or Movimiento == (2, 9) or Movimiento == (3, 9) or Movimiento == (4, 9) or Movimiento == (5, 9) or Movimiento == (6, 9) or Movimiento == (7, 9) or Movimiento == (8, 9):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (9, 9):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1 
                    else:
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1                             
                    Tablero_Visible[Y][X] = " "+str(Bombitas)
                    if Bandera == 0:
                        Puntos += 10
                        Bandera = 1
                    else:
                        Puntos += (Puntos*1.1)
                    print("👉Felicidades, No has pegado en una bomba!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                    Ganar += 1
                elif Tablero_Oculto[Y][X] == ":(":
                    Vidas -= 1
                    Tablero_Visible[Y][X] = ":("
                    print("👉Fallaste :C, has pegado en una bomba! BOOOM!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                Jugadas.append(Movimiento)
            else:
                print("👉Ya has hecho esa jugada!.. intenta nuevamente")
            Diccionario['Nombre'] = Nombre
            Diccionario['Dificultad'] = Dificultad
            Diccionario['Tablero_Oculto'] = Tablero_Oculto
            Diccionario['Tablero_Visible'] = Tablero_Visible
            Diccionario['Vidas'] = Vidas
            Diccionario['Jugadas'] = Jugadas
            Diccionario['Ganar'] = Ganar
            Diccionario['Bandera'] = Bandera
            Diccionario['Puntos'] = Puntos
            Archivo = open("Guardar_Partida/Partida.wembie","bw")
            marshal.dump(Diccionario,Archivo)
            Archivo.close()
        print("👉!!!!!!!!!!!!!!!!!!Felicidades!!!!!!!!!!!!!!!!!!!!")
        print("👉!!!!!!!!!!!!!!!!! HAS GANADO !!!!!!!!!!!!!!!!!!!!")
        Score[Nombre] = Puntos
        Archivo_Score = open("Scores/Dificil/Score.wembie","bw")
        marshal.dump(Score,Archivo_Score)
        Archivo_Score.close()
        Score_Ordenado = sorted(Score)
        Score_Ordenado = sorted(Score.items())
        Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
        print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
        for Wembie in enumerate(Score_Ordenado):
            Posicion += 1
            print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
    if Diccionario['Dificultad'] == 4:
        print("㍿㍿㍿㍿㍿㍿㍿ BIENVENIDO AL NIVEL ㍿㍿㍿㍿㍿㍿㍿") 
        print("㍿㍿㍿㍿㍿㍿㍿        WEMBIE       ㍿㍿㍿㍿㍿㍿㍿")
        print("㍿㍿㍿㍿㍿㍿㍿     DE NUEVO :V     ㍿㍿㍿㍿㍿㍿㍿")
        Dificultad = Diccionario['Dificultad']
        Nombre = Diccionario['Nombre']
        Vidas = Diccionario['Vidas']
        Puntos = Diccionario['Puntos']
        Bandera = Diccionario['Bandera']
        Jugadas = Diccionario['Jugadas']
        Ganar = Diccionario['Ganar']
        Score = {}
        Archivo_Score = open("Scores/Wembie/Score.wembie","br")
        Dato_Score = marshal.load(Archivo_Score)
        Score = Dato_Score
        Archivo_Score.close()
        Posicion = 0
        Tablero_Oculto = Diccionario['Tablero_Oculto']
        Tablero_Visible = Diccionario['Tablero_Visible']     
        while Ganar != 119:
            if Vidas == 0:
                print(Tablero_Visible[0])
                print(Tablero_Visible[1])
                print(Tablero_Visible[2])
                print(Tablero_Visible[3])
                print(Tablero_Visible[4])
                print(Tablero_Visible[5])
                print(Tablero_Visible[6])
                print(Tablero_Visible[7])
                print(Tablero_Visible[8])
                print(Tablero_Visible[9])
                print(Tablero_Visible[10])
                print(Tablero_Visible[11])
                print(Tablero_Visible[12])
                Score[Nombre] = Puntos
                Archivo_Score = open("Scores/Wembie/Score.wembie","bw")
                marshal.dump(Score,Archivo_Score)
                Archivo_Score.close()
                Score_Ordenado = sorted(Score)
                Score_Ordenado = sorted(Score.items())
                Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
                print("👉Has Perdido!, Se te acabaron las vidas :(")
                print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
                for Wembie in enumerate(Score_Ordenado):
                    Posicion += 1
                    print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
                sys.exit()
            print(Tablero_Visible[0])
            print(Tablero_Visible[1])
            print(Tablero_Visible[2])
            print(Tablero_Visible[3])
            print(Tablero_Visible[4])
            print(Tablero_Visible[5])
            print(Tablero_Visible[6])
            print(Tablero_Visible[7])
            print(Tablero_Visible[8])
            print(Tablero_Visible[9])
            print(Tablero_Visible[10])
            print(Tablero_Visible[11])
            print(Tablero_Visible[12])
            while 1 != 0:
                X = int(input("Digite la Posicion X [1,2,3,4,5,6,7,8,9,10,11,12]: "))
                if X == 1 or X == 2 or X == 3 or X == 4 or X == 5 or X == 6 or X == 7 or X == 8 or X == 9 or X == 10 or X == 11 or X == 12:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            while 1 != 0:
                Y = int(input("Digite la Posicion Y [1,2,3,4,5,6,7,8,9,10,11,12]: "))
                if Y == 1 or Y == 2 or Y == 3 or Y == 4 or Y == 5 or Y == 6 or Y == 7 or Y == 8 or Y == 9 or Y == 10 or Y == 11 or Y == 12:
                    break
                else:
                    print("👉Numero Invalido")
                    print("👉Digitelo Nuevamente")
            Movimiento = X,Y
            Bombitas = 0
            if Movimiento not in Jugadas:
                if Tablero_Oculto[Y][X] == " O":
                    if Movimiento == (12, 1) or Movimiento == (12, 2) or Movimiento == (12, 3) or Movimiento == (12, 4) or Movimiento == (12, 5) or Movimiento == (12, 6) or Movimiento == (12, 7) or Movimiento == (12, 8) or Movimiento == (12, 9) or Movimiento == (12, 10) or Movimiento == (12, 11):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (1, 12) or Movimiento == (2, 12) or Movimiento == (3, 12) or Movimiento == (4, 12) or Movimiento == (5, 12) or Movimiento == (6, 12) or Movimiento == (7, 12) or Movimiento == (8, 12) or Movimiento == (9, 12) or Movimiento == (10, 12) or Movimiento == (11, 12):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                    elif Movimiento == (12, 12):
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1 
                    else:
                        if Tablero_Oculto[Y-1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X-1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X+1] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y+1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y-1][X] == ":(":
                            Bombitas += 1
                        if Tablero_Oculto[Y][X-1] == ":(":
                            Bombitas += 1                             
                    Tablero_Visible[Y][X] = " "+str(Bombitas)
                    if Bandera == 0:
                        Puntos += 10
                        Bandera = 1
                    else:
                        Puntos += (Puntos*1.1)
                    print("👉Felicidades, No has pegado en una bomba!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                    Ganar += 1
                elif Tablero_Oculto[Y][X] == ":(":
                    Vidas -= 1
                    Tablero_Visible[Y][X] = ":("
                    print("👉Fallaste :C, has pegado en una bomba! BOOOM!")
                    print(f"👉Puntos obtenidos: {Puntos}")
                    print(f"👉Vidas Restantes: {Vidas}")
                Jugadas.append(Movimiento)
            else:
                print("👉Ya has hecho esa jugada!.. intenta nuevamente")
            Diccionario['Nombre'] = Nombre
            Diccionario['Dificultad'] = Dificultad
            Diccionario['Tablero_Oculto'] = Tablero_Oculto
            Diccionario['Tablero_Visible'] = Tablero_Visible
            Diccionario['Vidas'] = Vidas
            Diccionario['Jugadas'] = Jugadas
            Diccionario['Ganar'] = Ganar
            Diccionario['Bandera'] = Bandera
            Diccionario['Puntos'] = Puntos
            Archivo = open("Guardar_Partida/Partida.wembie","bw")
            marshal.dump(Diccionario,Archivo)
            Archivo.close()
        print("👉!!!!!!!!!!!!!!!!!!Felicidades!!!!!!!!!!!!!!!!!!!!")
        print("👉!!!!!!!!!!!!!!!!! HAS GANADO !!!!!!!!!!!!!!!!!!!!")
        Score[Nombre] = Puntos
        Archivo_Score = open("Scores/Wembie/Score.wembie","bw")
        marshal.dump(Score,Archivo_Score)
        Archivo_Score.close()
        Score_Ordenado = sorted(Score)
        Score_Ordenado = sorted(Score.items())
        Score_Ordenado = sorted(Score.items(), key=operator.itemgetter(1), reverse=True)
        print("( ✧≖ ͜ʖ≖)   SCORE   ( ✧≖ ͜ʖ≖)")
        for Wembie in enumerate(Score_Ordenado):
            Posicion += 1
            print(f"{Posicion}. Nombre = {Wembie[1][0]}, Puntos = {Score[Wembie[1][0]]}")
if Menu == 3:
    print("Has salido con exito!")
    sys.exit()


#taller izi
    
#1. Elaborar un algoritmo para calcular el área de un triangulo cuya altura es de 30 cm y la base de 50cm. Realizar una versión genérica de este algoritmo para calcular el area de un triangulo dada unaaltura y una base cualquiera, ¿Qué cambio se debe hacer?

def Area():
    Altura = int(input("Digite la ALtura: "))
    Base = int(input("Digite la Base: "))
    Area = (Base*Altura)/2
    print(f"La Area del triangulo cuya altura es: {Altura} y base es: {Base} es de: {Area}")
Area()

#3. Elaborar un algoritmo que realice la transformación de grados Celsius a Fahrenheit
def Transformacion():
    Celsius = int(input("Digite los grados en Celsius: "))
    Fahrenheit = (Celsius*(9/5))+32
    print(f"La conversion de {Celsius}°C a Fahrenheit es de: {Fahrenheit}°F")
Transformacion()

#7. Elaborar un algoritmo que permita hallar el estudiante con mejor promedio de un curso de 30 estudiantes

def Encontrar(Lista):
    Mayor = Lista[0][1]
    Nombre = ""
    for i in range(len(Lista)):
        if Lista[i][1] > Mayor:
            Mayor = Lista[i][1]
            Nombre = Lista[i][0]
    return Mayor,Nombre                   
Estudiantes = [["Juan", 2.9],["Jose", 3.0],["Mariela", 2.8],["Isabella", 4.0],["Esteban", 3.9]] #Y asi sucesivamente
Promedio_Mayor, Nombre = Encontrar(Estudiantes)
print(f"El mayor promedio de los estudiantes fue: {Promedio_Mayor} y el nombre del estudiante fue: {Nombre}")

#adivinar ciclos              
#programa que simula el juego de adivinar un número con 3 oportunidades
#entradas: n (el numero a adivinar) y 3 números adivinados por el usuario
#salida: el sistema imprime en pantalla si el número adivinado por el usuario
# el menor o mayor al numero a adivinar, también indica si ganó o perdió luego
# de las 3 oportunidades disponibles

#este archivo contiene errores, utilice las estrategias de depuración para solucionarlos
def adivinarConCiclos(n):

    oportunidad = 1
    while oportunidad <= 3:
        numero = int(input("Cual es el numero?: "))
        if numero == n:
            print("Advino!!!")
            oportunidad = 3
            #break
            #tambien podemos usar el break para forzar al ciclo a terminar
        else:
            if oportunidad == 3:
                print(f"Perdio! el numero era: {n}")
            else:
                if numero > n:
                    print("El numero a adivinar es menor.")
                else:
                    print("El numero a adivinar es mayor.")
        oportunidad += 1
    print("Fin del ciclo")

#Llamadas a las funciones

adivinarConCiclos(8)

#Modificado por Juan Esteban Acosta Lopez

#No tuve q usar uso de los depuradores solo lei el codigo y fui solucionando
#cada cosa en el codigo, puesto que ya se python.
#y comode los espacios ya que me estresaban jajajaa para una mejor
#visualisacion del codigo

#Software de la Universidad SuperFast
#Funcionamiento:
#Primero digite el numero 1, para asi calcular el costo del domicilio
#Segundo digite el numero 2, para asi calcular el costo de lo que quieras llevar del menu
#Tercero digite el numero 3, para asi terminar el pedido
#Si deseas salir digite el numero 0.

def menu():
    print("Menu:")
    print("1. Calcular valor domicilio.")
    print("2. Ver precios y escoger pedido.")
    print("3. Realizar pedido.")
    print("0. Salir.")
    
def carta():
    print("Carta:")
    print("1. Hamburguesas")
    print("2. Perros")
    print("3. Pizzas")
    print("4. Ver carrito")
    print("5. Borrar producto")
    print("6. Terminar pedido.")
    print("0. Salir")
    
def cartaHamburguesa():
    print("1. Sencilla -> $12000")
    print("2. Doble -> $18000")
    print("0. Volver.")
    
def cartaPerro():
    print("1. Sencillo -> $10000")
    print("2. Tocineta -> $12000")
    print("0. Volver.")
    
def cartaPizza():
    print("1. Hawaiana -> $16000")
    print("2. Pollo con Champiñones -> $17500")
    print("0. Volver.")
    
print("             Bienvenid@             ")
print("Software de la Universidad SuperFast")
print("")                            
opcion = -1
suma = 0
bandera = 0
salir = 0
while salir != 3:
    menu()
    while True:
        try:
            opcion = int(input("Digite el numero deseado [0,1,2,3]: "))
        except ValueError:
            print("Solo se recibe numeros enteros")
        else:
            if opcion == 1 or opcion == 2 or opcion == 3 or opcion == 0:
                if opcion == 2 and bandera == 0:
                    print("Lo siento :c, primero debes realizar la opcion 1.")
                elif opcion == 3 and bandera == 0:
                    print("Lo siento :c, primero debes realizar la opcion 1.")
                elif opcion == 3 and bandera == 1:
                    print("Lo siento :c, primero debes realizar la opcion 2.")
                elif opcion == 1 and bandera == 1:
                    print("Ya has realizado este proceso.")
                elif opcion == 1 and bandera == 2:
                    print("Ya has realizado este proceso.")
                elif opcion == 2 and bandera == 2:
                    print("Ya has realizado este proceso.")                    
                break
            else:
                print("Numero invalido")
                print("Por favor digitelo nuevamente")
    eleccion = -1
    carrito = [] 
    if opcion == 1 and bandera == 0:
        bandera = 1
        nombre = input("Por favor digite su nombre: ")
        print(f"Señor@ {nombre} por favor...")
        nombreBarrio = input("Digite el nombre del barrio en el cual reside: ")
        kilometros = 0
        while True:     
            try:
                kilometros = int(input("Digite cantidad de km que hay desde la universidad a su casa: "))
            except ValueError:
                print("Solo se recibe numeros enteros")
            else:
                break
        valorDomicilio = kilometros * 255
        print(f"El valor a pagar de su domicilio hasta {nombreBarrio} es de: ${valorDomicilio}")  
    elif opcion == 2 and bandera == 1:
        bandera = 2
        while True:
            carta()
            while True:
                try:
                    eleccion = int(input("Digite el numero deseado [0,1,2,3,4,5,6]: "))
                except ValueError:
                    print("Solo se recibe numeros enteros")
                else:                
                    if eleccion == 1 or eleccion == 2 or eleccion == 3 or eleccion == 4 or eleccion == 5 or eleccion ==6 or eleccion == 0:
                        break
                    else:
                        print("Numero invalido")
                        print("Por favor digitelo nuevamente")
            paquete = []
            if eleccion == 1:
                cartaHamburguesa()
                while True:
                    try:
                        seleccion = int(input("Digite el numero deseado [0,1,2]: "))
                    except ValueError:
                        print("Solo se recibe numeros enteros")
                    else: 
                        if seleccion == 1 or seleccion == 2 or seleccion == 0:
                            break
                        else:
                            print("Numero invalido")
                            print("Por favor digitelo nuevamente")
                if seleccion == 1:
                    tipo = "Hamburguesa sencilla"
                    cantidad = 0
                    while True:
                        try:           
                            cantidad = int(input("Cuantas hamburguesas desea llevar?: "))
                        except ValueError:
                            print("Solo se recibe numeros enteros")
                        else:
                            if cantidad > 0:
                                break
                            else:
                                print("La cantidad debe ser mayor a 0.")
                    valor = 12000 * cantidad
                    suma += valor
                    paquete.append(tipo)
                    paquete.append(cantidad)
                    paquete.append("$"+str(valor))
                    carrito.append(paquete)
                if seleccion == 2:
                    tipo = "Hamburguesa doble"
                    cantidad = 0
                    while True:
                        try:           
                            cantidad = int(input("Cuantas hamburguesas desea llevar?: "))
                        except ValueError:
                            print("Solo se recibe numeros enteros")
                        else:
                            if cantidad > 0:
                                break
                            else:
                                print("La cantidad debe ser mayor a 0.")
                    valor = 18000 * cantidad
                    suma += valor
                    paquete.append(tipo)
                    paquete.append(cantidad)
                    paquete.append("$"+str(valor))
                    carrito.append(paquete)
                if seleccion == 0:
                    print("Volviendo...")
            if eleccion == 2:
                cartaPerro()
                while True:
                    try:
                        seleccion = int(input("Digite el numero deseado [0,1,2]: "))
                    except ValueError:
                        print("Solo se recibe numeros enteros")
                    else: 
                        if seleccion == 1 or seleccion == 2 or seleccion == 0:
                            break
                        else:
                            print("Numero invalido")
                            print("Por favor digitelo nuevamente")
                if seleccion == 1:
                    tipo = "Perro sencillo"
                    cantidad = 0
                    while True:
                        try:           
                            cantidad = int(input("Cuantos Perros desea llevar?: "))
                        except ValueError:
                            print("Solo se recibe numeros enteros")
                        else:
                            if cantidad > 0:
                                break
                            else:
                                print("La cantidad debe ser mayor a 0.")                   
                    valor = 10000 * cantidad
                    suma += valor
                    paquete.append(tipo)
                    paquete.append(cantidad)
                    paquete.append("$"+str(valor))
                    carrito.append(paquete)
                if seleccion == 2:
                    tipo = "Perro tocineta"
                    cantidad = 0
                    while True:
                        try:           
                            cantidad = int(input("Cuantos Perros desea llevar?: "))
                        except ValueError:
                            print("Solo se recibe numeros enteros")
                        else:
                            if cantidad > 0:
                                break
                            else:
                                print("La cantidad debe ser mayor a 0.")
                    valor = 12000 * cantidad
                    suma += valor
                    paquete.append(tipo)
                    paquete.append(cantidad)
                    paquete.append("$"+str(valor))
                    carrito.append(paquete)
                if seleccion == 0:
                    print("Volviendo...")
            if eleccion == 3:
                cartaPizza()
                while True:
                    try:
                        seleccion = int(input("Digite el numero deseado [0,1,2]: "))
                    except ValueError:
                        print("Solo se recibe numeros enteros")
                    else: 
                        if seleccion == 1 or seleccion == 2 or seleccion == 0:
                            break
                        else:
                            print("Numero invalido")
                            print("Por favor digitelo nuevamente")
                if seleccion == 1:
                    tipo = "Pizza hawaiana"
                    cantidad = 0
                    while True:
                        try:           
                            cantidad = int(input("Cuantas Pizzas desea llevar?: "))
                        except ValueError:
                            print("Solo se recibe numeros enteros")
                        else:
                            if cantidad > 0:
                                break
                            else:
                                print("La cantidad debe ser mayor a 0.")                     
                    valor = 16000 * cantidad
                    suma += valor
                    paquete.append(tipo)
                    paquete.append(cantidad)
                    paquete.append("$"+str(valor))
                    carrito.append(paquete)
                if seleccion == 2:
                    tipo = "Pizza pollo con champiñones"
                    cantidad = 0
                    while True:
                        try:           
                            cantidad = int(input("Cuantas Pizzas desea llevar?: "))
                        except ValueError:
                            print("Solo se recibe numeros enteros")
                        else:
                            if cantidad > 0:
                                break
                            else:
                                print("La cantidad debe ser mayor a 0.") 
                    valor = 17500 * cantidad
                    suma += valor
                    paquete.append(tipo)
                    paquete.append(cantidad)
                    paquete.append("$"+str(valor))
                    carrito.append(paquete)
                if seleccion == 0:
                    print("Volviendo...")
            if eleccion == 4:
                if len(carrito) > 0:
                    print("")
                    print("Carrito:")
                    print("")
                    for i in range(len(carrito)):
                        print(f"Numero = {i}")
                        print(f"Tipo = {carrito[i][0]}")
                        print(f"Cantidad = {carrito[i][1]}")
                        print(f"Valor = {carrito[i][2]}")
                        print("")
                else:
                    print("No has pedido nada.")
                    print("Por favor pide alguito :D")
            if eleccion == 5:
                if len(carrito) > 0:
                    print("")
                    print("Carrito:")
                    print("")
                    for i in range(len(carrito)):
                        print(f"Numero = {i}")
                        print(f"Tipo = {carrito[i][0]}")
                        print(f"Cantidad = {carrito[i][1]}")
                        print(f"Valor = {carrito[i][2]}")
                        print("")
                    borrar = -1
                    for i in range(len(carrito.copy())):
                        while True:
                            try:
                                borrar = int(input(f"Digite un numero del 0 hasta el {len(carrito)-1}: "))
                            except ValueError:
                                print("Solo se recibe numeros enteros")
                            else:
                                if borrar <= len(carrito)-1 and borrar >= 0:
                                    break
                                else:
                                    print("Numero invalido")
                                    print("Por favor digitelo nuevamente")
                        temporal = carrito[i][2]
                        numero = temporal.replace("$","")
                        numero = int(numero)
                        valor -= numero
                        carrito.pop(borrar)
                        break
                else:
                    print("No has pedido nada.")
                    print("Por favor pide alguito :D")
            if eleccion == 6:
                if len(carrito) == 0:
                    print("No has pedido nada.")
                    print("Por favor pide alguito :D")
                else:
                    break
            if eleccion == 0:
                exit()
    elif opcion == 3 and bandera == 2:
        salir = 3
    elif opcion == 0:
        exit()
total = suma + valorDomicilio
print(f"El valor total de su pedido a pagar es de : ${total}")
print("")
print("Gracias por comprar en Universidad SuperFast ")
print("")
print("Tu pedido ya va en camino!")
print("")
print(":D")
print("")
print("""Desarrolladores:
Juan Acosta (Wembie)
Valentina Agudelo (Valen la MEJOR)""")
print("Saliendo...")    
exit()

######################
##  ENVIAR EMAIL   ##
######################

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from smtplib import SMTP
mensaje = MIMEMultipart("plain")
mensaje["From"]="juanes500@hotmail.com"
mensaje["To"]= "juanes500@yahoo.com"
mensaje["Subject"] ="Correo de prueba desde Python 3"
adjunto = MIMEBase("application","octect-stream")
adjunto.set_payload(open("sapo.txt","rb").read())
adjunto.add_header("content-Disposition",'attachment; filename="mensaje.txt"')
mensaje.attach(adjunto)
smtp = SMTP("smtp.live.com")
#smtp.gmail.com for google accounts
#smtp.yahoo.com for yahoo accounts
smtp.starttls()
smtp.login("email","password")
smtp.sendmail("juanes500@hotmail.com","juanes500@yahoo.com",mensaje.as_string())
smtp.quit()

##############
##GAUSJORDAN##
##############

#Sistema 2x2
#a11X a12Y = b1
#a21X a22Y = b2

#definimos 2 funciones para encontrar el numero mayor entre los primeros coeficientes del sistema

def maximo(num1,num2):
	if(abs(num1)>abs(num2)):
		return num1
	else:
		return num2
def minimo(num1,num2):
	if(abs(num1)<abs(num2)):
		return num1
	else:
		return num2
#Creamos dos listas una donde almacenaremos nuestros coeficientes
#La otra la usaremos para acomodarlos y hacer mas fácil el trabajo
a=[]
aux=[]

#Agregamos a nuestra primera lista los coeficientes dados por el usuario
a.append(int(input("Introduce el primer coeficiente ")))
a.append(int(input("Introduce el segundo coeficiente ")))
a.append(int(input("Introduce el termino independiente ")))

a.append(int(input("Introduce el primer coeficiente ")))
a.append(int(input("Introduce el segundo coeficiente ")))
a.append(int(input("Introduce el termino independiente ")))

#Obtenemos el mayor y el menor sin tomar el signo para hacer una división
#Es por eso que en nuestras funciones tenemos la función abs()
#La cual nos regresa el valor absoluto de un numero

mayor = maximo(a[0],a[3])
menor = minimo(a[0],a[3])


#cambiar las listas
#Con esto acomodamos las listas
#Para tener el coeficiente menor siempre en a[0]

if (abs(a[0])>abs(a[3])):
	aux.extend([a[3],a[4],a[5]])
	a[3]=a[0]
	a[4]=a[1]
	a[5]=a[2]

	a[0]=aux[0]
	a[1]=aux[1]
	a[2]=aux[2]

#Con este multiplo sabremos como hacer la multiplicacion de la fila 1
#Con el signo negativo para que se cancele con la fila 2 y obtener el 0
multiplo = -(mayor/menor)

#multiplo*F1 + F2 -> F2

a[3] = a[0]*multiplo + a[3]
a[4]= a[1]*multiplo + a[4]
a[5] = a[2]*multiplo + a[5]

#condiciones para saber sobre las soluciones

#Esta primer condición nos determina que hay una unica solución

if(a[4]!=0):
	y = a[5]/a[4]
	x = (a[2]-a[1]*y)/a[0]
	print("\n\nUnica solución")
	print("y =",y)
	print("x =",x)

#Una segunda condición para saber si nuestro sistema no tiene solución
elif (a[4]==0 and a[5]!=0):
	print("No tiene solución")
  
#Si tenemos que en a[4] y en a[5] hay ceros significa una infinidad de soluciones

elif(a[4]==0 and a[5]==0):
	print("Tiene infinidad de soluciones: ")
#Aqui imprimimos una representación de la ecuación despejando X
if(a[0]>0):
	print("x = (",a[2],"",-a[1],"y)/",a[0])
else:
	print("x = (",-a[2],"",a[1],"y)/",-a[0])
	
########
#LOGIN#
########

	
#CREANDO LOGIN CON PYTHON Y TKINTER.

#IMPORTAMOS LIBRERÍAS NECESARIAS.
from tkinter import *
import os

#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=Tk()
    ventana_principal.geometry("300x250")#DIMENSIONES DE LA VENTANA
    ventana_principal.title("Login con tkinter")#TITULO DE LA VENTANA
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#ETIQUETA CON TEXTO
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack() #BOTÓN "Acceder"
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack() #BOTÓN "Registrarse".
    Label(text="").pack()
    ventana_principal.mainloop()

#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("300x250")
 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = StringVar() #DECLARAMOS "string" COMO TIPO DE DATO PARA "nombre_usuario"
    clave = StringVar() #DECLARAMOS "sytring" COMO TIPO DE DATO PARA "clave"
 
    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    etiqueta_nombre = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario) #ESPACIO PARA INTRODUCIR EL NOMBRE.
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') #ESPACIO PARA INTRODUCIR LA CONTRASEÑA.
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = registro_usuario).pack() #BOTÓN "Registrarse"

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x250")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
 
    global verifica_usuario
    global verifica_clave
 
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
 
    global entrada_login_usuario
    global entrada_login_clave
 
    Label(ventana_login, text="Nombre usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    entrada_login_usuario.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Nombre usuario *" AL MOSTRAR NUEVA VENTANA.
    entrada_login_clave.delete(0, END) #BORRA INFORMACIÓN DEL CAMPO "Contraseña *" AL MOSTRAR NUEVA VENTANA.
 
    lista_archivos = os.listdir() #GENERA LISTA DE ARCHIVOS UBICADOS EN EL DIRECTORIO.
    #SI EL NOMBRE SE ENCUENTRA EN LA LISTA DE ARCHIVOS..
    if usuario1 in lista_archivos:
        archivo1 = open(usuario1, "r") #APERTURA DE ARCHIVO EN MODO LECTURA
        verifica = archivo1.read().splitlines() #LECTURA DEL ARCHIVO QUE CONTIENE EL nombre Y contraseña.
        #SI LA CONTRASEÑA INTRODUCIDA SE ENCUENTRA EN EL ARCHIVO...
        if clave1 in verifica:
            exito_login() #...EJECUTAR FUNCIÓN "exito_login()"
        #SI LA CONTRASEÑA NO SE ENCUENTRA EN EL ARCHIVO....
        else:
            no_clave() #...EJECUTAR "no_clave()"
    #SI EL NOMBRE INTRODUCIDO NO SE ENCUENTRA EN EL DIRECTORIO...
    else:
        no_usuario() #..EJECUTA "no_usuario()".


# VENTANA "Login finalizado con exito".
 
def exito_login():
    global ventana_exito
    ventana_exito = Toplevel(ventana_login)
    ventana_exito.title("Exito")
    ventana_exito.geometry("150x100")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=borrar_exito_login).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS

def borrar_exito_login():
    ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()

#REGISTRO USUARIO
 
def registro_usuario():
 
    usuario_info = nombre_usuario.get()
    clave_info = clave.get()
 
    file = open(usuario_info, "w") #CREACION DE ARCHIVO CON "nombre" y "clave"
    file.write(usuario_info + "\n")
    file.write(clave_info)
    file.close()
 
    entrada_nombre.delete(0, END)
    entrada_clave.delete(0, END)
 
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
 
 
ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.


#GLOBAL sirve para un parametro de una funcion que no se pierda y se pueda usar afuera de la funcion
def mundo():
    global suma
    a = 5
    b = 4
    suma = a + b
    print(f"La suma es: {suma}")
mundo()
print(f"La suma es: {suma}")




