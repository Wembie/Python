#Punto 1)
#La universidad Javeriana se encuentra implementando un nuevo modelo de cargos
#y rangos salariales para sus empleados administrativos. Existen 4 cargos b´asicos: Auxiliar, Asistente, Coordinador y Director. 
#Se necesita implementar un programa en python que permita
#calcular y mostrar en pantalla el salario de un empleado
print("1. Auxiliar, 2. Asistente, 3. Coordinador, 4. Director")
cargoEmpleado = int(input("Digita el cargo: "))
horasTrabajadasMaximas = 192
auxiliar = 7500
asistente = 9400
coordinador = 13800
director = 20500
horasTrabajadas = int(input("Digita las horas trabajadas del empleado: "))
if horasTrabajadas >= 0 and horasTrabajadas <= horasTrabajadasMaximas:
    if cargoEmpleado == 1:
        if horasTrabajadas >= 160:
           auxiliar = auxiliar + auxiliar*0.15
        sueldo = auxiliar * horasTrabajadas
        print("el suelo del empleado auxiliar es: ", sueldo)
    elif cargoEmpleado == 2:
        sueldo = asistente * horasTrabajadas
        print("el suelo del empleado asistente es: ", sueldo)
    elif cargoEmpleado == 3:
        if horasTrabajadas == horasTrabajadasMaximas:
            coordinador = coordinador + coordinador*0.08
        sueldo = coordinador * horasTrabajadas
        print("el suelo del empleado coordinador es: ", sueldo)
    elif cargoEmpleado == 4:
        sueldo = director * horasTrabajadas
        print("el suelo del empleado director es: ", sueldo)
    else:
        print("Cargo no valido")
else:
    print("Horas trabajadas superadas o menores a 0")

#Punto 2)
#La empresa de cines Filmes S.A. est´a buscando optimizar el proceso de ventas
#de las entradas de las diferentes funciones a sus salas de cine. La empresa tiene sede en tres
#ciudades de Colombia: Bogot´a, Medell´ın y Cali. S´olo en Cali tienen una promoci´on para los
#estudiantes de escuelas p´ublicas, la cual consiste en descontar 50 % del valor de la entrada para
#las funciones 2D, exclusivamente. Unas de las caracter´ısticas m´as interesantes de Filmes S.A. es
#que los valores de las entradas son iguales para las tres ciudades. A continuaci´on se muestra una
#tabla con los diferentes precios para las diferentes salas de cine, adem´as incluye un descuento
#para compras en grupo.

print("1. Cali, 2. Medellin, 3. Bogota")
ciudad = int(input("Digita la ciudad donde te encuentras: "))
dosD = 7500
dosDMax = 8100
tresD = 13000
cuatroD = 25500
if ciudad == 1:
    estudiantePublica = int(input("Estudiante de escula publica? [ Si = 1, No = 0 ]: "))
    cuantasBoletas = int(input("Digita la cantidad de boletas a comprar: "))
    print("1. 2D\n2. 2D MAX\n3. 3D\n4. 4D ")
    salaCine = int(input("Digita la sala que desees: "))
    if salaCine == 1:
        if cuantasBoletas > 5:
            dosD  = 7000
        if estudiantePublica == 1:
            dosD = dosD - dosD*0.50 
        total = dosD * cuantasBoletas
        print("Valor a pagar para boletas 2D es de: ", total)
    elif salaCine == 2:
        if cuantasBoletas > 5:
            dosDMax  = 7300
        total = dosDMax * cuantasBoletas
        print("Valor a pagar para boletas 2D MAX es de: ", total)
    elif salaCine == 3:
        if cuantasBoletas > 5:  
            tresD = 11500
        total = tresD * cuantasBoletas
        print("Valor a pagar para boletas 3D es de: ", total)
    elif salaCine == 4:
        if cuantasBoletas > 5:  
            cuatroD = 23000
        total = cuatroD * cuantasBoletas
        print("Valor a pagar para boletas 4D es de: ", total)
    else:
        print("Sala de cine no validad")
elif ciudad == 2 or ciudad == 3:
    cuantasBoletas = int(input("Digita la cantidad de boletas a comprar: "))
    print("1. 2D\n2. 2D MAX\n3. 3D\n4. 4D ")
    salaCine = int(input("Digita la sala que desees: "))
    if salaCine == 1:
        if cuantasBoletas > 5:
            dosD  = 7000
        total = dosD * cuantasBoletas
        print("Valor a pagar para boletas 2D es de: ", total)
    elif salaCine == 2:
        if cuantasBoletas > 5:
            dosDMax  = 7300
        total = dosDMax * cuantasBoletas
        print("Valor a pagar para boletas 2D MAX es de: ", total)
    elif salaCine == 3:
        if cuantasBoletas > 5:  
            tresD = 11500
        total = tresD * cuantasBoletas
        print("Valor a pagar para boletas 3D es de: ", total)
    elif salaCine == 4:
        if cuantasBoletas > 5:  
            cuatroD = 23000
        total = cuatroD * cuantasBoletas
        print("Valor a pagar para boletas 4D es de: ", total)
    else:
        print("Sala de cine no validad")
else:
    print("Ciudad no validad")

#Punto 3)
#Revise el programa e identifique que errores tiene. Indique el n´umero de la
#l´ınnea donde se encuentra el error y explique que error tiene.
#Corrija las l´ınneas indicadas en el numeral anterior para que el algoritmo
#cumpla con lo requerido por la empresa

#-o-

#Linea 1-> si preguntas por el estrato se refiere a un tipo INT no un tipo STRING y quitarle el ; 
#Linea 2-> quitarle el ;
#Linea 3-> si preguntas por el consumo se refiere a un tipo INT o FLOAT entonces colocamos EVAL para manejar los 2 tipos no un tipo STRING y quitarle el ;

#Linea 5-> falta los :
#Linea 6-> falta los :
#Linea 7-> quitar los ;
#Linea 8-> falta los :
#Linea 9-> quitar el ;
#Linea 10-> cambiar el elseif por elif y colocar los :
#Linea 11-> falta los :
#Linea 12-> quitar el ;
#Linea 13-> falta los :
#Linea 14-> quitar el ;
#Linea 15-> end no existe en python
#Linea 16-> cambiar el elseif por elif y colocar los :
#Linea 17-> quitar el ;
#Linea 18-> cambiar el elseif por elif y colocar los :
#Linea 19-> quitar el ;
#Linea 20-> cambiar el elseif por elif y colocar los :
#Linea 21-> siguiendo la estructura que llevan los demas la agrupacion esta mal y el operando es una suma en vez de una resta y quitar el ;
#Linea 22-> cambiar el elseif por elif y colocar los :
#Linea 23-> siguiendo la estructura que llevan los demas la agrupacion esta mal y el operando es una suma en vez de una resta y quitar el ;
#Linea 24-> falta los :
#Linea 25-> en python no se usa el fprintf de error como en c si no print solito
#Linea 26-> end no existe en python

#Linea 28-> falta los :
#Linea 29-> quitar el ;
#Linea 30-> end no existe en python

#Linea 32-> falta los :
#Linea 33-> acomodar las agrupaciones y quitar el ;
#Linea 34-> end no existe en python

#Linea 36-> en python no se usa el fprintf como en c si no print solito y deberia imprimir factura no consumo

estrato = int(input("Bienvenido al sistema de facturacion de energia de Cali, por favor digite su estrato: "))
uso = input("Por favor digite el tipo de uso de la vivienda: --Comercial --Residencial: ")
consumo = eval(input("Por favor digite el consumo del mes: "))

if estrato == 1:
    if(consumo <= 130):
        factura = (consumo * 224) - (consumo * 224 * 0.1)
    else:
        factura = (consumo * 440) - (consumo * 440 * 0.05)
elif estrato == 2:
    if(consumo <= 130):
        factura = (consumo * 280) - (consumo * 280 * 0.05)
    else:
        factura = (consumo * 550) - (consumo * 550 * 0.03)
    #end
elif estrato == 3:
    factura = consumo * 412 * 0.02
elif estrato == 4:
    factura = consumo * 580
elif estrato == 5:
    factura = (consumo * 620) - (consumo * 620 * 0.1)
elif estrato == 6:
    factura = (consumo * 670) - (consumo * 670 * 0.2)
else:
    print("El estrato no existe")
#end

if uso == "Comercial":
    factura = factura + 60000
#end

if(consumo > 600):
    factura = factura + (factura * 0.16)
#end

print("El valor de su factura es: ", factura)
