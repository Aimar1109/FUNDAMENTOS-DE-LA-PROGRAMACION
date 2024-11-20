import random
from typing import List, Dict

# Generador de datos meteorológicos
def generar_datos_meteorologicos(n: int) -> List[Dict[str, int]]:
    """
    Genera una lista de diccionarios con datos meteorológicos aleatorios.

    :param n: Número de registros a generar.
    :return: Lista de diccionarios con datos meteorológicos.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    datos = []
    for _ in range(n):
        registro = {
            "Día": random.choice(dias_semana),
            "Temperatura": random.randint(-10, 40),  # En grados Celsius
            "Humedad": random.randint(0, 100),      # En porcentaje
            "Velocidad del viento": random.randint(0, 120)  # En km/h
        }
        datos.append(registro)
    return datos

# Función para guardar los datos en un fichero TXT
def guardar_datos(datos: List[Dict[str, int]], nombre_fichero: str) -> None:
    """
    Guarda una lista de diccionarios en un fichero TXT.

    :param datos: Lista de diccionarios con datos meteorológicos.
    :param nombre_fichero: Nombre del fichero donde se guardarán los datos.
    """
    # TODO: Implementar guardado manual en fichero
    with open(nombre_fichero, 'w') as f:

        p_linea = ''
        for titulo in datos[0].keys():
            p_linea += str(titulo) + '; '

        f.write(p_linea+'\n')
        for registro in datos:
            f.write(registro['Día']+'; '+str(registro['Temperatura'])+'; '+str( registro['Humedad'])+'; '+str( registro['Velocidad del viento'])+';\n')

# Función para cargar los datos desde un fichero TXT
def cargar_datos(nombre_fichero: str) -> List[Dict[str, int]]:
    """
    Carga datos meteorológicos desde un fichero TXT.

    :param nombre_fichero: Nombre del fichero desde el que se cargarán los datos.
    :return: Lista de diccionarios con los datos cargados.
    """
    # TODO: Implementar carga manual desde fichero

    with open(nombre_fichero, 'r') as f:
        p = True
        datos = []
        for line in f:
            if p:
                p = False
                continue
            r = line.split(';')
            registro = {'Día': r[0], 'Temperatura': int(r[1]), 'Humedad': int(r[2]), 'Velocidad del viento': int(r[3])}
            datos.append(registro)
        return datos

# Operaciones con los datos cargados
def dia_con_temperatura_maxima(datos: List[Dict[str, int]]) -> str:
    """
    Encuentra el día con la temperatura máxima.

    :param datos: Lista de diccionarios con datos meteorológicos.
    :return: Día con la temperatura máxima.
    """
    # TODO: Implementar esta función
    temperatura_maxima = datos[0]
    for registro in datos:
        if registro['Temperatura'] > temperatura_maxima['Temperatura']:
            temperatura_maxima = registro
    return temperatura_maxima['Día']


def dia_mas_caluroso(datos: List[Dict[str, int]]) -> str:
    """
    Calcula cuál es el día más caluroso considerando el promedio diario de temperatura.

    :param datos: Lista de diccionarios con datos meteorológicos.
    :return: El día más caluroso.
    """
    # TODO: Implementar esta función
    dias = {}
    for registro in datos:
        if registro['Día'] in dias:
            dias[registro['Día']]  = (registro['Temperatura'] + dias[registro['Día']])/2
        else:
            dias[registro['Día']] = registro['Temperatura']
    return max(dias, key=dias.get)


def promedio_humedad(datos: List[Dict[str, int]]) -> float:
    """
    Calcula el promedio de la humedad semanal.

    :param datos: Lista de diccionarios con datos meteorológicos.
    :return: Promedio de la humedad.
    """
    # TODO: Implementar esta función
    humedad = 0
    for registro in datos:
        humedad += registro['Humedad']
    return humedad / len(datos)
    
def dias_viento_superior(datos: List[Dict[str, int]], umbral: int) -> int:
    """
    Determina cuántos días tuvieron velocidad del viento superior a un umbral dado.

    :param datos: Lista de diccionarios con datos meteorológicos.
    :param umbral: Valor del umbral de velocidad del viento.
    :return: Número de días con viento superior al umbral.
    """
    # TODO: Implementar esta función
    dias = 0
    for registro in datos:
        if registro['Velocidad del viento'] > umbral:
            dias += 1
    return dias

# Función principal
if __name__ == "__main__":
    # Generar datos (ya resuelto)
    print("Generando datos meteorológicos...")
    datos = generar_datos_meteorologicos(7)
    print("Datos generados:", datos)

    # Guardar los datos en un fichero TXT
    print("\nGuardando datos en 'datos_meteorologicos.txt'...")
    guardar_datos(datos, "datos_meteorologicos.txt")

    # Cargar los datos desde el fichero TXT
    print("\nCargando datos desde 'datos_meteorologicos.txt'...")
    datos_cargados = cargar_datos("datos_meteorologicos.txt")
    print("Datos cargados:", datos_cargados)

    # Realizar operaciones con los datos cargados
    print("\nOperaciones con los datos:")
    print("1. Día con temperatura máxima:", dia_con_temperatura_maxima(datos_cargados))
    print("2. Promedio de la humedad semanal:", promedio_humedad(datos_cargados))
    umbral_viento = 50  # Cambiar este valor si se desea
    print(f"3. Días con velocidad del viento superior a {umbral_viento} km/h:", dias_viento_superior(datos_cargados, umbral_viento))
    print("4. Día más caluroso (promedio diario):", dia_mas_caluroso(datos_cargados))
