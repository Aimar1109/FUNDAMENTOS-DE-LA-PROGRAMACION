import random


def creador_municipios():
    municipios = []
    for i in range(5):
        municipio = {'nombre':f'municipio-{i}',
                     'codigo_postal':48000+random.randint(0,999),
                     'habitantes':random.randint(2*(10**6), 3*(10**6)),
                     'hogares':random.randint(1*(10**4), 5*(10**4)),
                     'consumo': random.randint(7*(10**3), 3*(10**4))
                     }
        municipios.append(municipio)
    
    municipios_ordenados = []
    while len(municipios) > 0:
        min = municipios[0]
        for municipio in municipios:
            if municipio['codigo_postal'] < min['codigo_postal']:
                min = municipio
        municipios_ordenados.append(min)
        municipios.remove(min)
    return municipios_ordenados


def consumo_media_hab(municipio):
    return municipio['consumo'] / municipio['habitantes']


def crearMensaje(municipio):
    return f'{municipio['hogares']} hogares han consumido un total de {municipio['consumo']}m3, con una media de {consumo_media_hab(municipio)}m3/habitante'


def agua_disponible(municipios):
    restante = 100000
    for municipio in municipios:
        restante -= municipio['consumo']
    return restante

def indice_municipio(municipios, cd_pst):
    indice = -1
    for i in range(len(municipios)):
        if municipios[i]['codigo_postal'] == cd_pst:
            indice = i
            break
    return indice
print(creador_municipios())