import csv
import copy

def crear_vuelos_limpios():
    with open('flights.csv', 'r', encoding='utf-8') as f:

        contenido = csv.reader(f)

        columnas = next(contenido)

        indices = [columnas.index('Origin'), columnas.index('Dest'), columnas.index('FlightTimeMin'), columnas.index('AvgTicketPrice')]
        lista =  []
        for row in contenido:
            mins = ''
            for x in row[indices[2]]:
                if x != ',':
                    mins += x
            price = ''
            for p in row[indices[3]]:
                if p != ',':
                    price += p
            lista.append([row[indices[0]], row[indices[1]], str(mins), str(price)[1:]])
        f.close()
    
    with open('clean_flights.csv', 'w', encoding='utf-8') as f:
        for vuelo in lista:
            f.write(';'.join(vuelo)+'\n')
        f.close()
    
    for vuelo in lista:
        vuelo[2] = float(vuelo[2])
        vuelo[3] = float(vuelo[3])

    return lista
    
def leer_vuelos_limpios():
    with open('clean_flights.csv', 'r', encoding='utf-8') as f:
        lista = []
        for linea in f:
            linea = linea.strip().split(';')
            linea[2] = float(linea[2])
            linea[3] = float(linea[3])
            lista.append(linea)
        f.close()
    
    return lista


def crear_dict_guardar(lista, tipo, col):
    dict = {}
    counter = 0
    for vuelo in lista:
        if vuelo[col] not in dict.keys():
            dict[vuelo[col]] = counter
            counter += 1

    with open(f'{tipo}.csv', 'w', encoding='utf-8') as f:
        for key in dict.keys():
            a = key + ';' + str(dict[key]) + '\n'
            f.write(a)
        f.close()

    return dict

def leer_dict(tipo):
    dict = {}
    with open(f'{tipo}.csv', 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip().split(';')
            dict[linea[0]] = int(linea[1])
        f.close()
    return dict

def crear_guardar_matriz(lista, dict_ind, dict_col):
    matriz = []
    for y in dict_ind:
        linea = []
        for x in dict_col:
            linea.append(0)
            for vuelo in lista:
                if y == vuelo[0] and x == vuelo[1]:
                    linea[dict_col[x]] = float(vuelo[2])
        matriz.append(linea)

    with open('matriz_vuelos.csv', 'w', encoding='utf-8') as f:
        for linea in matriz:
            a = ';'.join([str(x) for x in linea])
            f.write(a+'\n')
        f.close()

    return matriz


def leer_matriz():
    with open('matriz_vuelos.csv', 'r', encoding='utf-8') as f:
        matriz = []
        for linea in f:
            linea = [float(x) for x in linea.strip().split(';')]
            matriz.append(linea)

        f.close()
    return matriz


def encontrar_trayectoria(origen, posibilities, encontrado, padre, capa):
    # Funcion para encontrar la ruta una vez encontrado el destino

    # Varibles locales
    trayectoria = [[encontrado, padre]]
    capa_tra = capa
    # Copia de las posibilidades para que poder borrar y hacer la busqueda
    posibilities_t = copy.deepcopy(posibilities)

    # Buscar ruta
    while capa_tra > 0:
        borrar = []
        # Darle la vuelta al diccionario porque el padre tiene que estar al final
        for pos in posibilities_t.keys():
            # Si el padre es el origen hemos finalizado la busqueda de la ruta
            if pos == origen and capa_tra in [x[0] for x in posibilities_t[pos]]:
                trayectoria.append([pos, posibilities_t[pos][1]])
                capa_tra -= 1
                break
            # Si encuentra al padre lo añade a la ruta
            elif  capa_tra in [x[0] for x in posibilities_t[pos]] and pos == trayectoria[-1][-1]:
                
                trayectoria.append([pos, [x[1] for x in posibilities_t[pos] if x[0] == capa_tra][0]])
                capa_tra -= 1

        # Buscar la ultima capa para eliminarlas de las posibilidades
        for pos in  posibilities_t.keys():
            a = posibilities_t[pos]
            for c in posibilities_t[pos]:
                if c[0] > capa_tra:
                    posibilities_t[pos].remove(c)
        
        # Borrar la ultima capa
        for pos in posibilities_t.keys():
            if len(posibilities_t[pos]) == 0:
                borrar.append(pos)
        
        for b in borrar:
            posibilities_t.pop(b)
    
    return trayectoria


def calcular_precio(lista_vuelos, ruta):
    suma = 0
    ruta_p = copy.deepcopy(ruta)
    for r in ruta_p:
        r.reverse()
        for v in lista_vuelos:
            if r[0] == v[0] and r[1] == v[1]:
                suma += v[-1]

    return suma


def algoritmo_busqueda(matriz, dict_ind, dict_col, origen, destino, lista_vuelos):
    # Busqueda de vuelos por bfs, recorriendo primero todas las posibilidades dentro de un capa
    # Para ello uso un diccionario con el aeropuerto de clave y una lista con la capa y su aeropuerto padre

    # Varibles locales
    posibilities = {}
    try:
        dict_destino = {destino: dict_col[destino]}
    except KeyError:
        return []
    rutas = []
    capa = 0
    final = False
    posibilities[origen] = [[capa, None, 0]] # posibilities[origen] = [[capa, None, 0]]


    # Busqueda en cada capa va añadiendo las siguientes posibilidades a un nuevo diccionario y una vez recorrido todo los destino pasa a la siguiente capa
    while not final:
        # Para añadir al final las nuevas posibilidades
        new_posibilities = {}
        # Recorrer las posibilidades por capa
        for pos in posibilities:
            try:                            
                if posibilities[pos][-1][0] == capa:

                    # Para cada aeropuerto de la capa buscar todos los vuelos de salida que tenga
                    for destino_id in range(len(dict_col)):

                        # Si el tiene vuelo al destino
                        if destino_id == dict_destino[destino] and  matriz[dict_ind[pos]][destino_id] > 0:
                            ruta = encontrar_trayectoria(origen, posibilities, destino, pos, capa)
                            rutas.append([ruta, posibilities[pos][-1][-1]+matriz[dict_ind[pos]][destino_id], calcular_precio(lista_vuelos, ruta)])

                        # Si no tiene vuelo al destino pero tiene un vuelo a un nuevo aeropuerto 
                        elif matriz[dict_ind[pos]][destino_id] > 0:
                                
                            # Buscar el nombre del aeropuerto destino
                            aeropuerto_n = [x for x in dict_col if dict_col[x] == destino_id][0]

                            if aeropuerto_n in posibilities.keys() and pos in [x[1] for x in posibilities[aeropuerto_n]]:
                                continue
                            elif aeropuerto_n == pos or aeropuerto_n == origen:
                                continue
                            tiempo = posibilities[pos][-1][-1]+matriz[dict_ind[pos]][destino_id]
                            # Si el aeropuerto de destino no esta ya en aeropuerto
                            if aeropuerto_n in new_posibilities.keys():
                                if tiempo > new_posibilities[aeropuerto_n][0][-1]:
                                    continue
                            new_posibilities[aeropuerto_n] = [[capa+1, pos, tiempo]]
                # if pos == list(posibilities.keys())[-1]:
                #     break
                else:
                    continue
            # Cuando el aeropuerto no tiene vuelos de salida
            except KeyError:
                pass
    
        # Añdair las nuevas posibilidades porque si voy añadiendolas directamente me jode el for porque esta editando las posibilidades
        if len(new_posibilities) > 0:
            for new_pos in new_posibilities:
                if new_pos in posibilities.keys():
                    if new_posibilities[new_pos][0][1] in [x[1] for x in posibilities[new_pos]]:
                        continue
                    posibilities[new_pos].append(new_posibilities[new_pos][0])
                    continue
                posibilities[new_pos] = new_posibilities[new_pos]
            capa += 1
        else:
            final = True
    
    return rutas

def elegir_rutas(rutas):
    # Funcion para elegir la ruta con menos tiempo y la que menos escalas tenga
    ruta_menos_escalas_tiempo = rutas[0]
    ruta_menos_tiempo = rutas[0]
    ruta_barata = rutas[0]
    for ruta in rutas:
        if len(ruta_menos_escalas_tiempo[0]) > len(ruta[0]):
            ruta_menos_escalas_tiempo = ruta
        elif len(ruta_menos_escalas_tiempo[0]) == len(ruta[0]) and ruta_menos_escalas_tiempo[1] > ruta[1]:
            ruta_menos_escalas_tiempo = ruta
        if ruta_menos_tiempo[1] > ruta[1]:
            ruta_menos_tiempo = ruta
        if ruta_barata[-1] > ruta[-1]:
            ruta_barata = ruta
    
    return ruta_menos_escalas_tiempo, ruta_menos_tiempo, ruta_barata


if __name__ == '__main__':
    try:
        vuelos = leer_vuelos_limpios()
    except FileNotFoundError:
        vuelos = crear_vuelos_limpios()
    try:
        dict_indices = leer_dict('dict_indices')
        dict_columnas = leer_dict('dict_columnas')
    except FileNotFoundError:
        dict_indices = crear_dict_guardar(vuelos, 'dict_indices', 0)
        dict_columnas = crear_dict_guardar(vuelos, 'dict_columnas', 1)

    try:
        matriz_vuelos = leer_matriz()
    except FileNotFoundError:
        matriz_vuelos = crear_guardar_matriz(vuelos, dict_indices, dict_columnas)

    
    #rutas_vuelos = algoritmo_busqueda(matriz_vuelos, dict_indices, dict_columnas, 'Sheremetyevo International Airport', 'Winnipeg / James Armstrong Richardson International Airport')

    # PRUEBAS:

    # rutas_vuelos = algoritmo_busqueda(matriz_vuelos, dict_indices, dict_columnas, 'Portland International Jetport Airport', 'San Francisco International Airport')
    # ruta_esc, ruta_tiemp = elegir_rutas(rutas_vuelos)
    # print(ruta_esc)
    # print(ruta_tiemp)

    # Comprobar todas las posibilidades
    c1 = 0
    for i in dict_indices:
        c2 = 0
        if c1 == 5:
            break
        for x in dict_columnas:
            if c2 == 5:
                break
            rutas_vuelos = algoritmo_busqueda(matriz_vuelos, dict_indices, dict_columnas, i, x, vuelos)
            if len(rutas_vuelos) == 1:
                print(rutas_vuelos[0])
            elif len(rutas_vuelos) > 0:
                ruta_m_e, ruta_m_t, ruta_b = elegir_rutas(rutas_vuelos)
                if ruta_m_e == ruta_m_t and ruta_b == ruta_m_e:
                    print(ruta_m_e)
                else:   
                    print(ruta_m_e)
                    print(ruta_m_t)
                    print(ruta_b)
            else:
                print('No se ha encontrado la ruta')
            print('')
            c2 +=1
        c1 += 1


    print(matriz_vuelos[4][79])