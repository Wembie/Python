--Punto 1:

listaDadaPunto1 :: (Eq a) => [a] -> [a] --significa que cualquier a en los parámetros de la función debe ser miembro de la clase Eq, que puede evaluarse como igual o desigual.
listaDadaPunto1 (x:xs) = x : listaDadaPunto1 (filter (/= x) xs) --Con filter devuelve una lista construida a partir de miembros de una lista (el segundo argumento) que cumple una condición dada por el primer argumento
listaDadaPunto1 [] = [] --se da la lista vacia


--Punto 2a:

listaDada :: [Int] -> [Int] --Se recibe una lista de tipo int y va a retornar una lista de tipo int
listaDada [] = [] --Se define una lista vacia
listaDada (x:xs) = x: (listaDada (borrarElementoDado x xs)) --Entonces para ello recibimos un x y con ello que se llama a la funcion y con ello remueve el elemento dado
    where --Donde
        borrarElementoDado :: Int -> [Int] -> [Int] -- Va a recibir un int el cual va el index de la lista recibida y con ello va a retornar el resto de la lista
        borrarElementoDado x [] = [] --Se define una lista vacia para las eliminaciones
        borrarElementoDado x (y:ys) --Y esto removera cuando le den un x si el y es igual al s
            --Condiciones
            | x==y = borrarElementoDado x ys --Entonces si x es igual a el output, sera removido
            --De otro modo si no funciona lo de arriba = otherwise
            | otherwise = y:(borrarElementoDado x ys) --Removera x

--Punto 3:

compararListas lista1 lista2 = (take(length lista1) lista2) == lista1 --Comparando las listas desde el primer index

comparacionListas listaN1 (listaN2:listaN3) | length listaN1 > length (listaN2:listaN3) = False --Si es mas grande el lenght de la primera que la segunda lista da false
                                            | compararListas listaN1 (listaN2:listaN3) = True --En el caso que los lengths de las 2 listas o iguales daria o retorna true
                                            | compararListas listaN1 (listaN2:listaN3) == False = comparacionListas listaN1 listaN3 --y si nada de los demas sirve lo que haria es que comprara la primera lista con la segunda lista sin su primer index