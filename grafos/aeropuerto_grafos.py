def lista_vuelos():
    try:
        # Cargar los datos de vuelos_limpios
        vuelos = []
        with open('vuelos_limpios.csv', 'r', encoding='utf-8') as f:
            for linea in f:
                vuelos.append([x for x in linea.strip().split(';')])
            f.close()

    except FileNotFoundError:
        # Si no se ha encontrado el archivo crearlo
        lista = []
        with open('BAreviews.csv', 'r', encoding='utf-8') as f:
            p = True
            for linea in f:
                if p:
                    p = False
                else:
                    linea = linea.strip().split(',')
                    if linea[4] != 'None':
                        lista.append(linea[4])
            f.close()

        vuelos = []
        for i in lista:
            vuelo = i.split(' to ')
            vuelo[0] = vuelo[0].strip('"')

            if len(vuelo) > 1:
                if vuelo in vuelos:
                    continue
                vuelos.append(vuelo[:2])
                continue
            else:
                vuelo = i.split('-')
                if len(vuelo) > 1:
                    if vuelo in vuelos:
                        continue
                    vuelos.append(vuelo)
                    continue

        for v in range(len(vuelos)):
            el = vuelos[v][1].split(' ')
            if len(el) > 1:
                if el[1] == 'via' or el[1] == 'return':
                    vuelos[v][1] = el[0]
            elif len(el) > 2:
                if el[2] == 'via' or el[2] == 'return':
                    vuelos[v][1] = ''.join(el[:2])
        
        for x in range(len(vuelos)):
            vuelos[x][0] = vuelos[x][0].strip()
            vuelos[x][1] = vuelos[x][1].split('via')[0]
            vuelos[x] = [x.capitalize() for x in vuelos[x]]

        with open('vuelos_limpios.csv', 'w', encoding='utf-8') as f:
            for vuelo in vuelos:
                a = ';'.join(vuelo)+'\n'
                f.write(a)
    return vuelos

def crear_dict(lista):
    index = 0
    dict_vuelos = {}
    for vuelo in lista:
        if vuelo[0] not in dict_vuelos.keys():
            dict_vuelos[vuelo[0]] = index
            index += 1
    return dict_vuelos


def guardar_dict(diccionario):
    with open('diccionario_indices.csv', 'w', encoding='utf-8') as f:
        for key in diccionario.keys():
            a = key + ';' + str(diccionario[key]) + '\n'
            f.write(a)

        f.close()


def leer_dict():
    dict_v = {}
    with open('diccionario_indices.csv', 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea.strip().split(';')
            dict_v[linea[0]] = int(linea[1])
        f.close()
    return dict_v


def crear_matriz(lista, diccionario):
    matriz = []
    for l in diccionario:
        linea = []
        for c in diccionario:
            linea.append(0)
            for vuelo in lista:
                if l == vuelo[0] and c == vuelo[1]:
                    linea.pop()
                    linea.append(1)
                    break
            
        matriz.append(linea)
    return matriz


def guardar_matriz(matriz):
    with open('matriz_vuelos.csv', 'w', encoding='utf-8') as f:
        for linea in matriz:
            a = ';'.join([str(x) for x in linea])
            f.write(a+'\n')

        f.close()


def leer_matriz():
    with open('matriz_vuelos.csv', 'r', encoding='utf-8') as f:
        matriz = []
        for linea in f:
            linea = [int(x) for x in linea.strip().split(';')]
            matriz.append(linea)

        f.close()
    return matriz


def algoritmo_busqueda_vuelos_profunda(matriz, dict_indices, origen, destino, vuelo_act=None, trayectoria=None):
    # Algortimo busqueda profunda

    # Variables locales
    dict_origen = {}
    if vuelo_act == None:
        trayectoria = []

    # Destino encontrado
    if vuelo_act and vuelo_act[1] == destino:
        return trayectoria

    # Buscar indice de origen mediante busqueda recursiva
    dict_origen[origen] = dict_indices[origen]
    for destino_id in range(len(matriz[dict_origen[origen]])):
        rp = False
        if matriz[dict_origen[origen]][destino_id] == 1:
            vuelo = [origen, [d for d in dict_indices if dict_indices[d] == destino_id][0]]
            for t in trayectoria:
                if t[0] == vuelo[1]:
                    rp = True
                    break
            if rp:
                continue
            trayectoria.append(vuelo)
            return algoritmo_busqueda_vuelos_profunda(matriz, dict_indices, vuelo[1], destino, vuelo, trayectoria)
    trayectoria = trayectoria[:-1]
    if len(trayectoria) == 0:
        return 'No se ha encontrado'
    return algoritmo_busqueda_vuelos_profunda(matriz, dict_indices, trayectoria[-1][1], destino, trayectoria[-1], trayectoria)


def algoritmo_busqueda_vuelos_bfs(matriz, dict_indices, origen, destino):
    # Busqueda de vuelos por bfs, recorriendo primero todas las posibilidades dentro de un capa
    # Para ello uso un diccionario con el aeropuerto de clave y una lista con la capa y su aeropuerto padre

    # Varibles locales
    posibilities = {}
    dict_destino = {destino: dict_indices[destino]}
    encontrado = False
    capa = 0
    posibilities[origen] = [capa, None]

    # Busqueda en cada capa va añadiendo las siguientes posibilidades a un nuevo diccionario y una vez recorrido todo los destino pasa a la siguiente capa
    while not encontrado:
        new_posibilities = {}
        for pos in posibilities:
            if posibilities[pos][0] == capa:
                for destino_id in range(len(matriz[dict_indices[pos]])):
                    if destino_id == dict_destino[destino] and  matriz[dict_indices[pos]][destino_id] == 1:
                        posibilities[destino] = [capa+1, pos]
                        encontrado, padre = destino, pos
                        break
                    elif matriz[dict_indices[pos]][destino_id] == 1:
                        new_posibilities[[x for x in dict_indices if dict_indices[x] == destino_id][0]] = [capa+1, pos]
            if encontrado:
                break
        # Añdair las nuevas posibilidades porque si voy añadiendolas directamente me jode el for porque esta editando las posibilidades
        if len(new_posibilities) > 0:
            for new_pos in new_posibilities:
                if new_pos in posibilities.keys():
                    continue
                posibilities[new_pos] = new_posibilities[new_pos]
            capa += 1
        else:
            return 'No se ha encontrado'
    
    # Una vez encontrado el destino empezar a ir para atras haciendo uso de aeropuerto padre y la capa
    trayectoria = [[encontrado, padre]]
    capa_tra = posibilities[encontrado][0]-1
    while capa_tra >= 0:
        for pos in posibilities:
            if pos == origen and capa_tra == posibilities[pos][0] == capa_tra:
                trayectoria.append([pos, posibilities[pos][1]])
                capa_tra -= 1
                break
            if posibilities[pos][0] == capa_tra and pos == trayectoria[-1][1]:
                trayectoria.append([pos, posibilities[pos][1]])
                capa_tra -= 1
            
    return trayectoria


# Main
if __name__ == "__main__":
    try:
        dict_vuelos = leer_dict()
    except FileNotFoundError:
        vuelos = lista_vuelos()
        dict_vuelos = crear_dict(vuelos)
        guardar_dict(dict_vuelos)

    try:
        matriz_vuelos = leer_matriz()
    except FileNotFoundError:
        vuelos = lista_vuelos()
        matriz_vuelos = crear_matriz(vuelos, dict_vuelos)
        guardar_matriz(matriz_vuelos)

    try:
        print(algoritmo_busqueda_vuelos_profunda(matriz_vuelos, dict_vuelos, 'Barbados', 'Amman jordan'))
    except RecursionError:
        print('No se a podido encontrar')
    #for i in dict_vuelos:
    #    if i != 'Barbados':
    #        print(algoritmo_busqueda_vuelos_bfs(matriz_vuelos, dict_vuelos, 'Barbados', i))

    print(algoritmo_busqueda_vuelos_bfs(matriz_vuelos, dict_vuelos, 'Barbados', 'Amman jordan'))

# PROBLEMAS:
# El diccionario de indices solo tiene de indices aeropuertos con salidas y no contempla aeropuertos que no tienen
# salidas y solo tienen entradas
#
# 
# 