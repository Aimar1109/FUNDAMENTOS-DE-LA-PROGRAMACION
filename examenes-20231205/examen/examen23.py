import csv

users = []
lista_palabras = []

username = {}
post = {}


def datos_prueba(users):
    pass


def cargar_palabras(palabras):
    with open('hinojosa.csv', mode='r') as file:
        csv_reader = csv.reader(file, delimiter=';')
        for fila in csv_reader:
            print(fila)
            palabras.append([fila[0], round(float(fila[1]), 2)])
    return palabras


lista_palabras = cargar_palabras(lista_palabras)

print(lista_palabras)
