import numpy as np
import matplotlib.pyplot as plt

def muller( f, x0, x1, x2, tol = 1e-6, maxiter = 100 ):
    """
    Encuentra una raíz del polinomio 'f' utilizando el método de Muller.

    f: función polinómica en forma de lambda o función definida.
    x0: primera aproximación de la raíz.
    x1: segunda aproximación de la raíz.
    x2: tercera aproximación de la raíz.
    tol: tolerancia para la convergencia.
    maxiter: número máximo de iteraciones permitidas.
    Retorna la raíz encontrada y el número de iteraciones realizadas.
    """

    # Inicializar variables.
    x = [ x0, x1, x2 ]
    y = [ f( x0 ), f( x1 ), f( x2 ) ]
    converged = False
    niter = 0

    # Graficar la función.
    xs = np.linspace( -6, 6, 100 )
    ys = f( xs )
    plt.plot( xs, ys, label = 'Función' )

    # Graficar las iteraciones.
    plt.plot( x, y, 'o', label = 'Iteraciones' )

    # Iterar hasta que se alcance la convergencia o se alcance el número máximo de iteraciones.
    while not converged and niter < maxiter:
        # Calcular los coeficientes del polinomio cuadrático.
        h0, h1 = ( x[ -2 ] - x[ -3 ] ), ( x[ -1 ] - x[ -2 ] ) #Encontramos la diferencia entre las 2 ultimas aproximaciones de la raiz
        delta0, delta1 = ( f( x[ -2 ] ) - f( x[ -3 ] ) ) / ( x[ -2 ] - x[ -3 ] ), ( f( x[ -1 ] ) - f( x[ -2 ] ) ) / ( x[ -1 ] - x[ -2 ] ) #Encontramos la diferencia entre las evaluaciones de la funcion de las ultimas aproximaciones de la raiz divido por la diferencia entre las 2 ultimas aproximaciones de la raiz
        a = ( delta1 - delta0 ) / ( h1 + h0 ) #Encontramos el coeficiente cuadratico
        b = delta1 + a * h1 #Encontramos el coeficiente lineal
        c = f( x[ -1 ] ) #Encontramos el termino constante
        # Calcular las raíces del polinomio cuadrático.
        D = np.sqrt( b ** 2 - 4 * a * c ) #Encontramos la raiz cuadrada del discriminante
        if abs( b + D ) > abs( b - D ):
            E = b + D #Uno de los 2 posibles valores de la suma entre b y D
        else:
            E = b - D #Uno de los 2 posibles valores de la diferencia entre b y D
        dx = -2 * c / E #La diferencia entre la raiz aproximada de la iteracion actual y la raiz aproximada de la iteracion anteior
        # Actualizar las aproximaciones.
        xnew = x[ -1 ] + dx
        x.append( xnew )
        y.append( f( xnew ) )
        # Verificar si se alcanzó la convergencia.
        if abs( dx ) < tol:
            converged = True
        niter += 1
        # Graficar la iteración.
        
        plt.plot( xnew, f( xnew ), 'o' )
    # Mostrar la gráfica.
    plt.legend()
    plt.grid()
    plt.show()
    # Devolver la raíz y el número de iteraciones.
    return xnew, niter

# Definir la función polinómica.
f = lambda x: x ** 3 - 13 * x - 12  #Funcion usada en la prueba de escritorio

# Definir las aproximaciones iniciales.
x0 = 5.5
x1 = 4.5
x2 = 5

# Encontrar la raíz.
raiz, niter = muller( f, x0, x1, x2 )

# Imprimir el resultado.
print( f"Raíz encontrada: { raiz }" )
print( f"Número de iteraciones: { niter }" )