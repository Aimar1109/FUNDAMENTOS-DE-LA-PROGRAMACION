
# Nombre:
# Apellido:
# DNI:

from datetime import datetime

# Funciones auxiliares
def format_hora(hora):
    return datetime.strptime(hora, "%H:%M")

# Lista de diccionarios para pasajeros
pasajero1 = {"nombre": "Ana Torres", "identificacion": "ID1001", "asiento": "10A"}
pasajero2 = {"nombre": "Carlos Gómez", "identificacion": "ID1002", "asiento": "10B"}
pasajero3 = {"nombre": "Luisa Fernández", "identificacion": "ID1003", "asiento": "11A"}
pasajero4 = {"nombre": "Miguel Ángel Ruiz", "identificacion": "ID1004", "asiento": "11B"}

# Diccionario para cada vuelo
vuelo1 = {
    "numero_vuelo": "AA123",
    "origen": "Madrid",
    "destino": "París",
    "salida": "09:00",
    "llegada": "11:30",
    "pasajeros": [pasajero1, pasajero2]
}

vuelo2 = {
    "numero_vuelo": "BB456",
    "origen": "Bogotá",
    "destino": "Miami",
    "salida": "14:00",
    "llegada": "18:00",
    "pasajeros": [pasajero3]
}

vuelo3 = {
    "numero_vuelo": "CC789",
    "origen": "Buenos Aires",
    "destino": "Santiago",
    "salida": "07:00",
    "llegada": "09:00",
    "pasajeros": [pasajero4]
}

vuelo4 = {
    "numero_vuelo": "DD101",
    "origen": "París",
    "destino": "Londres",
    "salida": "12:30",
    "llegada": "13:30",
    "pasajeros": []
}

vuelo5 = {
    "numero_vuelo": "EE202",
    "origen": "Miami",
    "destino": "Nueva York",
    "salida": "19:30",
    "llegada": "21:30",
    "pasajeros": []
}

vuelo6 = {
    "numero_vuelo": "FF102",
    "origen": "Londres",
    "destino": "Bilbao",
    "salida": "22:00",
    "llegada": "23:30",
    "pasajeros": []
}

vuelo7 = {
    "numero_vuelo": "FF102",
    "origen": "Bilbao",
    "destino": "Hawai",
    "salida": "22:00",
    "llegada": "23:30",
    "pasajeros": []
}

vuelo8 = {
    "numero_vuelo": "FF102",
    "origen": "Hawai",
    "destino": "Salamanca",
    "salida": "22:00",
    "llegada": "23:30",
    "pasajeros": []
}

vuelo9 = {
    "numero_vuelo": "FF102",
    "origen": "Hawai",
    "destino": "Sevilla",
    "salida": "22:00",
    "llegada": "23:30",
    "pasajeros": []
}

vuelo10 = {
    "numero_vuelo": "FF102",
    "origen": "Bilbao",
    "destino": "Salamanca",
    "salida": "22:00",
    "llegada": "23:30",
    "pasajeros": []
}

vuelo11 = {
    "numero_vuelo": "FF102",
    "origen": "París",
    "destino": "Albacete",
    "salida": "22:00",
    "llegada": "23:30",
    "pasajeros": []
}

vuelo12= {
    "numero_vuelo": "FF102",
    "origen": "Madrid",
    "destino": "Tenesse",
    "salida": "22:00",
    "llegada": "23:30",
    "pasajeros": []
}


# Lista de vuelos
vuelos = [vuelo1, vuelo9, vuelo10, vuelo2, vuelo3, vuelo4, vuelo5, vuelo6, vuelo7,  vuelo8, vuelo11, vuelo12]


# Ejercicio 1
def calcular_capacidad_aeropuerto(vuelos:list) -> float:
    max:int = 100
    pasajeros:int = 0
    for vuelo in vuelos:
        pasajeros += len(vuelo['pasajeros'])
    return pasajeros / max

# print(calcular_capacidad_aeropuerto(vuelos))

# Ejercicio 2
nuevo_pasajero = {"nombre": "Sofía Martín", "identificacion": "ID1010","asiento": "12C"}


def agregar_pasajero(vuelos:list[dict], num_vuelo:str, pasajero:dict):
    for vuelo in vuelos:
        if vuelo['numero_vuelo'] == num_vuelo:
            vuelo['pasajeros'].append(pasajero)
            print(f'{pasajero['nombre']} a sido agregado/a al vuelo {vuelo['numero_vuelo']}')
            return vuelos
    print(f'No se ha encontrado el vuelo {num_vuelo}')
    return vuelos

# agregar_pasajero(vuelos, "AA123", nuevo_pasajero)

# agregar_pasajero(vuelos, "AA124", nuevo_pasajero)

# Ejercicio 3

def buscar_vuelo_por_destino(vuelos:list, destino:str):
    lista_vuelos:list = []
    for vuelo in vuelos:
        if vuelo['destino'] == destino:
            lista_vuelos.append(vuelo)
    return lista_vuelos

# Ejercicio 4
def itinerario(vuelo_origen, vuelo_destino, uno):
    tiempo_espera = format_hora(vuelo_destino['salida'])-format_hora(vuelo_origen['llegada'])
    tiempo_total = format_hora(vuelo_destino['llegada'])-format_hora(vuelo_origen['salida'])
    
    if uno:
        print (f'Itinerario: {vuelo_origen['numero_vuelo']} -> {vuelo_destino['numero_vuelo']}')
        print(f'Tiempo espera: {tiempo_espera}')
        print(f'Tiempo total del viaje: {tiempo_total}')

    return tiempo_espera, tiempo_total

def calcular_itinerarios_sencillo(vuelos:list, origen:str, destino:str):
    vuelo_origen:dict = {}
    vuelo_destino:dict = {}
    for vuelo in vuelos:
        if vuelo['origen'] == origen:
            vuelo_origen = vuelo
        elif vuelo['destino'] == destino:
            vuelo_destino = vuelo
    if len(vuelo_origen) == 0 or len(vuelo_destino) == 0:
        print('No exite la siguiente salidos o destinos')
    else:
        if vuelo_origen['destino'] != vuelo_destino['origen']:
            print('No se han encontrado las conexiones')
        else:
            itinerario(vuelo_origen, vuelo_destino, 1)

def calcular_itinerarios_avanzado(vuelos:list, origen:str, destino:str):
    for vuelo in vuelos:
        if vuelo['origen'] == origen:
            vuelo_origen = vuelo
        elif vuelo['destino'] == destino:
            vuelo_destino = vuelo
    if len(vuelo_origen) == 0 or len(vuelo_destino) == 0:
        print('No exite la siguiente salidos o destinos')
    else:
        if vuelo_origen['destino'] == vuelo_destino['origen']:
            itinerario(vuelo_origen, vuelo_destino, 1)
        else:
            for vuelo in vuelos:
                if vuelo_origen['destino'] == vuelo['origen']:
                    if vuelo['destino'] == vuelo_destino['origen']:
                        tiempo_espera2, tiempo_total2 = itinerario(vuelo, vuelo_destino)
                        


def busqueda_recursiva(vuelos, trayecto, origen, destino, vuelo_act=None):

    if vuelo_act and vuelo_act['destino'] == destino:
        destino = vuelo_act['origen']
        return trayecto

    
    for vuelo in vuelos:
        if vuelo['origen'] == origen:
            vuelos.remove(vuelo)
            trayecto.append(vuelo)
            return busqueda_recursiva(vuelos, trayecto, vuelo['destino'], destino, vuelo)
    
    try:
        return busqueda_recursiva(vuelos, trayecto[:-1], trayecto[:-1][-1]['destino'], destino, trayecto[-1])
    except IndexError:
        trayecto = busqueda_recursiva(vuelos, [], 'Madrid', 'Tenesse')
        if trayecto:
            return trayecto
        return 'No se ha encontrado'
        

print(busqueda_recursiva(vuelos, [], 'Madrid', 'Tenesse'))

# calcular_itinerarios_sencillo(vuelos, "Madrid", "Bilbao")
