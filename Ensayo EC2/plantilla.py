# Diccionario precargado con información de partidos
partidos = [
    {"id_partido": "M0001", "cod_jugador": "J101", "puntos": [100, 200, 150]},
    {"id_partido": "M0002", "cod_jugador": "J102", "puntos": [300, 250]},
    {"id_partido": "M0003", "cod_jugador": "J103", "puntos": [400, 350, 300]},
    {"id_partido": "M0004", "cod_jugador": "J104", "puntos": [200]},
    {"id_partido": "M0005", "cod_jugador": "J101", "puntos": [150, 250, 300, 100]},
    {"id_partido": "M0006", "cod_jugador": "J102", "puntos": [100, 150]},
    {"id_partido": "M0007", "cod_jugador": "J103", "puntos": [300, 200, 100]},
    {"id_partido": "M0008", "cod_jugador": "J101", "puntos": [200, 300, 150]},
    {"id_partido": "M0009", "cod_jugador": "J102", "puntos": [150]},
    {"id_partido": "M0010", "cod_jugador": "J104", "puntos": [400, 350]},
]

partidos = []

def cargar_partidos(partidos):
    with open('partidos.csv', 'r', encoding='utf-8') as f:
        for linea in f:
            linea = linea[:-1]
            datos = linea.split(':')
            partidos.append({'id_partido': datos[0],
                             'cod_jugador': datos[1],
                             'puntos': [int(x) for x in datos[2:]]})
    return partidos

partidos = cargar_partidos(partidos)

def promedio_puntos(partidos):
    suma = 0
    for partido in partidos:
        suma += sum(partido['puntos']) / len(partido['puntos'])
    return suma / len(partidos)

print(promedio_puntos(partidos))


def calcular_puntos_totales(jugador, partidos):
    puntos = 0
    for partido in partidos:
        if partido['cod_jugador'] == jugador:
            puntos += sum(partido['puntos'])
    return puntos

print(calcular_puntos_totales('J112', partidos))

def partido_por_jugador(partidos):
    jugadores = {}
    for partido in partidos:
        if partido['cod_jugador'] not in jugadores.keys():
            jugadores[partido['cod_jugador']] = 1
        else:
            jugadores[partido['cod_jugador']] += 1
    return jugadores

jugadores_partidos = partido_por_jugador(partidos)

def jugador_mas_activo(jugadores):
    mas_activo = ['', 0]
    for i in jugadores:
        if jugadores[i] > mas_activo[1]:
            mas_activo = [i, jugadores[i]]
    return mas_activo[0]


def guadar_partidos_jugador(jugador, partidos):
    lista = []
    for partido in partidos:
        linea = []
        if partido['cod_jugador'] == jugador:
            linea.append(partido['id_partido'])
            for i in partido['puntos']:
                linea.append(i)
            lista.append(linea)
    
    with open(f'partidos_{jugador}.csv', 'w', encoding='utf-8') as f:
        for partido in lista:
            frase = ''
            for i in partido:
                frase += str(i)+';'
            f.write(frase[:-1]+'\n')
        f.close()


guadar_partidos_jugador('J101', partidos)