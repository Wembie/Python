#Developed by:

#Valen LA MEJOR & Wembie
#Valentina Agudelo & Juan Acosta

def menuBienvenida():
    print("""DESCUENTOS CAFETERIA JAVERIANA CALI

0. Salir
1. Profesor
2. Estudiante""")

def menuProducto():
    print("""\n0. Volver
1. Registrar Producto
2. Ver Carrito
3. Borrar Producto
4. Realizar Pedido""")
    

def crearProducto(codigo, precio):
    producto = {}
    producto['Codigo'] = codigo
    producto['Precio'] = precio
    return producto

def productosCreados():
    productos = {}
    productos['Cafe'] = crearProducto(100, 4500)
    productos['Leche'] = crearProducto(101, 1500)
    productos['Gatorade'] = crearProducto(102, 5000)
    productos['Agua'] = crearProducto(103, 3000)
    productos['Pan'] = crearProducto(104, 1400)
    productos['Pandebono'] = crearProducto(105, 1500)
    productos['Chicle'] = crearProducto(106, 400)
    productos['Gomitas'] = crearProducto(107, 1300)
    productos['Helado'] = crearProducto(108, 2500)
    productos['Almuerzo'] = crearProducto(109, 8900)
    productos['Gaseosa'] = crearProducto(110, 2100)
    return productos

def menu(productos, opcion):
    if opcion == 0:
        print("")
        for i in productos:
            print(f"""{i}
  Codigo: {productos[i]['Codigo']}
  Precio: ${productos[i]['Precio']}""")
    else:
        print("")
        for i in range(len(productos.copy())):
            print(f"""Numero: {i}
{productos[i][0]}
  Codigo: {productos[i][1]}
  Cantidad: {productos[i][2]}
  Precio Total: ${productos[i][3]}""")

def preguntarSiNo(pregunta):
    while True:
        opcion = input(f"\n{pregunta} [Si/No]: ")
        if opcion.lower() == "si" or opcion.lower() == "no":
            return opcion.lower()
        else:
            print("\nCaracter invalido")
            print("Por favor digitelo nuevamente")
      
def preguntarOpcion(inicio, final, recuadro):
    while True:
        try:
            opcion = int(input(f"\nDigite el numero deseado {recuadro}: "))
        except ValueError:
            print("\nSolo se recibe numeros enteros")
        else:
            if opcion >= inicio and opcion <= final:
                return opcion
            else:
                print("\nNumero invalido")
                print("Por favor digitelo nuevamente")

def preguntarEntero(recuadro):
    while True:
        try:
            opcion = int(input(f"\n{recuadro}: "))
        except ValueError:
            print("\nSolo se recibe numeros enteros")
        else:
            return opcion    

def registrarProducto(rol):
    producto = []
    codigos = []
    productos = productosCreados()
    for i in productos:
        codigos.append(productos[i]['Codigo'])
    while True:
        codigoProducto = preguntarEntero("Digite el codigo del producto")
        if codigoProducto in codigos:
            break
        else:
            print("""\nCodigo invalido
Por favor digitalo nuevamente""")  
    while True:
        cantidadProducto = preguntarEntero("Digite la cantidad del producto")
        estasSeguro = preguntarSiNo("Estas seguro de esa cantidad?")
        if estasSeguro == "si":
            if cantidadProducto > 0:
                break
            else:
                print("\nLa cantidad del producto debe ser mayor a 0")
    if rol == 1:
        descuento = 0.20
    elif rol == 2:
        descuento = 0.50
    precio = None
    nombre = None
    for i in productos:
        if codigoProducto == productos[i]['Codigo']:
            precio = productos[i]['Precio']
            nombre = i
    descuento *= precio
    precio -= descuento
    precio *= cantidadProducto
    producto.append(nombre)
    producto.append(codigoProducto)
    producto.append(cantidadProducto)
    producto.append(precio)
    return producto
              
def main():
    while True:
        carrito = []
        menuBienvenida()
        opcionBienvenida = preguntarOpcion(0, 2, "[0,1,2]")
        if opcionBienvenida == 0:
            break
        nombre = input("\nDigite su nombre: ")
        cedula = preguntarEntero("Digite su cedula")
        while True:
            menuProducto()
            opcionProducto = preguntarOpcion(0, 4, "[0,1,2,3,4]")
            if opcionProducto == 1: #registrar producto
                menu(productosCreados(), 0)
                producto = registrarProducto(opcionBienvenida)
                carrito.append(producto)
            elif opcionProducto == 2: #ver carrito
                if len(carrito) > 0:
                    menu(carrito, 1)
                else:
                    print("\nCarrito vacio")
            elif opcionProducto == 3:
                if len(carrito) > 0:
                    menu(carrito, 2)
                    borrarProducto = preguntarOpcion(0, len(carrito)-1, "a borrar")
                    carrito.pop(borrarProducto)
                else:
                    print("\nCarrito vacio")
            elif opcionProducto == 4: #realizar pedido
                if len(carrito) > 0:
                    if opcionBienvenida == 1:
                        opcionBienvenida = "Profesor(a)"
                    else:
                        opcionBienvenida = "Estudiante"
                    total = 0
                    for i in range(len(carrito)):
                        total += carrito[i][3]
                    print(f"\nEl {opcionBienvenida} {nombre} con Cedula {cedula} debe pagar ${total}\n")
                    break
                else:
                    print("\nPara realizar el pedido debes al menos pedir algo")
            else:
                print("")
                break
            
main()
