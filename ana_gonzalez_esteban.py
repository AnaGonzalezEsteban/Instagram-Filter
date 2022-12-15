# 0.- Importo las funciones de python que voy a utilizar

from functools import reduce


######################## FUNCIONES CON LISTAS ########################


# 1.- Implemento una función que obtenga los INDICES de los vecinos horizontales de un elemento de la lista sin incluir dicho elemento

def get_neighbour_indices(index,elements):
    """ RECIBE el índice del elemento y la lista de todos los elementos.
        DEVUELVE: una lista con los INDICES de los vecinos. """
    indices = []
    indices.append(index - 1)
    indices.append(index + 1)
    # elimino los indices imposibles menores que cero o mayores  iguales a la longitud de la lista haciendo un filter
    filtered_indices=filter(lambda x: x>=0 and x<len(elements),indices)
    # Devuelvo la lista de los índices de los vecinos
    return list(filtered_indices)


# 2.- Implemento una función para obtener los VALORES de los vecinos horizontales de un elemento de la lista sin inlcuir dicho elemento

def get_neighbour_values(indices,elements):
    """ RECIBE: los índices de los vecinos y la lista de todos los elementos. 
        DEVUELVE: una lista con los VALORES vecinos. """
    # Creo una lista vacía donde iré acumulando los valores de los elementos
    values = []
    # Recorro la lista de indices
    for index in indices:
        # Añado a la lista vacía los elementos que tengan los índices de la lista de vecinos
        values.append(elements[index])
    # Devuelvo la lista de los valores de los vecinos
    return values


# 3.- Implemento una función que transforma un único elemento de una lista. 
#   Para un elemento, obtiene sus vecinos y devuelve la suma de ellos, sin incluir dicho elemento.

def process_element(index,elements):
    """ RECIBE: el índice de un elemento y la lista en la que se encuentra. 
        DEUELVE: La suma de sus vecinos SIN INCLUIR EL ELEMENTO y el número de vecinos que tiene el elemento """
    # Obtengo la lista de vecinos + elemento
    indices = get_neighbour_indices(index,elements)
    values = get_neighbour_values(indices,elements)
    # Calculo su suma
    sum = reduce(lambda x,y: x + y,values)
    # Devuelvo el valor final
    return sum,len(values)


# 4.- Implemento una función que transforma todos los elementos de una lista o fila horizontal

def process_list(elements):
    """ RECIBE: una lista de números 
        DEVUELVE: Una nueva lista en la que cada elemento sea la suma de los vecinos horizontales de cada elemento
            y también devuelve una lista en la que cada valor es el numero de vecinos de cada elemento """
    # Creo una nueva lista vacía donde iré acumulando los valores transformados
    processed_list = []
    num_neighbours = []
    # Hay que tener en cuenta que la lista puede no tener elementos o tener solo uno
    if len(elements) == 0:
        processed_list = [0]
        num_neighbours = [0]
    elif len(elements) == 1:
        processed_list = [0]
        num_neighbours = [0]
    else:
        # Itero por cada elemento de la lista.
        for index, element in enumerate(elements):
            # Proceso el elemento
            new_element = process_element(index, elements)
            # Añado el elemento procesado a la nueva lista
            processed_list.append(new_element[0])
            # añado un vecino al contador
            num_neighbours.append(new_element[1])

    # devuelvo la nueva lista procesada y la lista con el numero de vecinos
    return processed_list,num_neighbours


######################## FUNCIONES CON MATRICES ########################


# 5.- Implemento una función que itera por cada lista de la matriz y devuelve otra MATRIZ CUYAS LISTAS se componen del VALORES PROMEDIO DE LOS VECINOS DE CADA ELEMENTO.
#   SIN INCLUIR AL ELEMENTO!

def get_horizontal_neighbour_sum(matrix):
    """ RECIBE: dos matrices que son lista de listas, la primera es la lista de vecinos horizontales y la segunda el numero de vecinos horizontales PARA CADA ELEMENTO DE LA MATRIZ
        DEVUELVE: dos matrices:
            - una matriz que en cada lista(fila) contiene la suma de los vecinos horizontales de cada elemento de la matriz original. NO INCLUYE AL ELEMENTO
            - una matriz que en cada lista(fila) contiene el número de los vecinos horizontales de cada elemento de la matriz original """
    sum_neighbours=[]
    num_neighbours=[]
    for list in matrix:
        process_result = (process_list(list))
        sum_neighbours.append(process_result[0])
        num_neighbours.append(process_result[1])
    return sum_neighbours,num_neighbours


# 6.- Implemento una función que obtenga la matriz transpuesta de una matriz cualquiera

def get_transposed_matrix(matrix):
    """Devuelve la matriz transpuesta de una matriz cualquiera"""
    transp=[*zip(*matrix)] 
    # zip devuelve tuplas, lo convierto en listas para trabajar todo el ejercicio con listas y no mezclar distintos tipos de datos
    transposed_matrix=[]
    for element in transp:
        transposed_matrix.append(list(element))
    return transposed_matrix
    

# 7.- Implemento una función que transpone la matriz original, itera por cada lista de la matriz transpuesta 
#   y devuelve otra matriz cuyas listas se componen del promedio de los vecinos verticales de cada elemento SIN INCLUIR AL ELEMENTO
#   Para ello, aplico get_horizontal_processed_list a la matriz transpuesta
#   MUY IMPORTANTE: Los vecinos del elemento (n,m) en la matriz original serán los vecinos del elemento (m,n) en la transpuesta.
#   Para tener una lista que devuelva los promedios de los elementos en orden tal y como aparecen en la matriz original, transpongo la matriz transpuesta ya transformada.

def get_vertical_neighbour_sum(matrix):
    """ RECIBE: dos matrices que son lista de listas, la primera es la lista de vecinos horizontales y la segunda el numero de vecinos horizontales 
                PARA CADA ELEMENTO DE LA MATRIZ TRANSPUESTA
        DEVUELVE: dos matrices:
            - una matriz que en cada lista(fila) contiene la suma de los vecinos verticales de cada elemento de la matriz ORIGINAL. NO INCLUYE AL ELEMENTO
            - una matriz que en cada lista(fila) contiene el número de los vecinos verticales de cada elemento de la matriz ORIGINAL """
    transp = get_transposed_matrix(matrix)
    processed_transp = get_horizontal_neighbour_sum(transp)
    transp_sum = processed_transp[0]
    transp_num = processed_transp[1]
    return get_transposed_matrix(transp_sum),get_transposed_matrix(transp_num)


# 8.- Implemento una función que suma dos matrices cualesquiera
#   Se obtiene así una matriz cuyos elementos son la media de esos dos elementos en las matrices de entrada

def sum_matrix(M1, M2):

    dim_m1, dim_n1 = len(M1), len(M1[0]) # número de filas, número de columnas de M1
    dim_m2, dim_n2 = len(M2), len(M2[0]) # número de filas, número de columnas de M2

    if dim_m1 != dim_m2 or dim_n1 != dim_n2: # Para que podamos sumar matrices, tienen que tener las mismas dimensiones
        result = [0] # no debería darse esta caso en este programa porque trabajamos con una única matriz, por lo tanto las dimensiones serán siempre iguales

    # Creo una matriz que usaré como acumulador con las mismas dimensiones que M1 y M2 en la que todos sus elementos sean 0:
    result = [[0 for _ in range(dim_n1)] for _ in range(dim_m1)] 

    # Itero por la matriz, sumo sus elementos uno a uno y acumulo el resultado en result
    for m in range(dim_m1):
        for n in range(dim_n1):
            result[m][n] = M1[m][n] + M2[m][n]

    return result


# 9.- Implemento una función que recibe una matriz y devuelve dos matrices: la primera contiene la suma de vecinos totales para cada elemento de la matriz original,
#       y la otra contiene el numero de vecinos totales de cada elemento de la matriz original

def get_total_neighbours(matrix):
    """ RECIBE: DOS matriz
        DEVUELVE: DOS matrices:
                        - La suma de todos los vecinos de cada elemento de la matriz original
                        - El numero total de vecinos de cada elemento de la matriz original"""
    horizontal_neighbours = get_horizontal_neighbour_sum(matrix)
    vertical_neighbours = get_vertical_neighbour_sum(matrix)
    total_sum_neighbours = sum_matrix(horizontal_neighbours[0], vertical_neighbours[0])
    total_num_neighbours = sum_matrix(horizontal_neighbours[1], vertical_neighbours[1])
    return total_sum_neighbours,total_num_neighbours


# 10.- Implemento una función que sume 1 a cada elemento de una matriz

def sum_one(matrix):
    """ Dada una matriz, le suma uno a cada elemento"""
    new_matrix = []
    for list in matrix:
        new_list = []
        for element in list:
            new_element = element + 1
            new_list.append(new_element)
        new_matrix.append(new_list)
    return new_matrix 


# 11.- Implemento una función que sume cada elemento con todos sus vecinos

def add_element_and_neighbours(matrix):
    """ RECIBE: Una matriz
        HACE: Obtiene dos matrices, la suma de los vecinos y el numero de vecinos de cada elemento
        DEVUELVE: Dos matrices:
                        - Una es la suma de cada elemento con todos sus vecinos
                        - Otra es el numero de vecinos mas uno"""
    sum_num_neighbours = get_total_neighbours(matrix)
    total_sum = sum_matrix(sum_num_neighbours[0],matrix)
    total_num = sum_one(sum_num_neighbours[1])
    return total_sum,total_num


# 12.- Implemento una función que recibe dos matrices y devuelve una nueva matriz en la que cada elemento
#  es el resultado de dividir ese elemento de la primera matriz entre ese elemento de la segunda matriz

def average_matrix(M1, M2):
    """ RECIBE: dos matrices
        DEVUELVE: una matriz en la que cada elemento i,j es el elemento i,j de la primera entre el elemento i,j de la segunda.
                Los elementos de esta matriz resultante se han redondeado a dos cifras decimales
        ATENCiÓN: No se ha tenido en cuenta la posibilidad de que el denominador sea 0 porque en este ejercicio la matriz
        M2 es imposible que contenga un 0 (todos los elementos tienen algún vecino y además sum_one suma 1 por cada elemento) """
    new_matrix = []
    for i,list in enumerate(M1):
        new_list = []
        for j,element in enumerate(list):
            new_element = round(element / M2[i][j],2)
            new_list.append(new_element)
        new_matrix.append(new_list)
    return new_matrix


# 13.- Implemento una función que recibe una matriz, obtiene dos matrices: una con la SUMA de vecinos+elemento
#    y otra con el NUMERO total de vecinos+elemento. Devuelve una matriz que en cada elemento contiene suma/numero

def process_matrix(matrix):
    """ RECIBE: una matriz
        HACE: 
            - Obtiene dos matrices: la suma de los vecinos y el numero de vecinos de cada elemento INCLUYENDO EL ELEMENTO
            - Aplica average matrix a esas dos matrices para obtener el promedio de la suma de todos los vecinos+elemento entre el número de vecinos+elemento
        DEVUELVE: una matriz en la que cada elemento es el promedio de ese elemento con sus vecinos"""
    matrices = add_element_and_neighbours(matrix)
    result = average_matrix(matrices[0], matrices[1])
    return result
