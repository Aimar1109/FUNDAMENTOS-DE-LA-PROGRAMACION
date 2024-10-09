import csv

# LEER LA MATRIZ USERFILM
def leer_matriz_csv():
    matriz_user_film = []
    with open('matriz_peliculas.csv')as file:
        csv_reader = csv.reader(file, delimiter=',')

        for fila in csv_reader:
            for x in fila:
                try:
                    fila[fila.index(x)] = float(x)
                except:
                    pass
            matriz_user_film.append(fila)
    return matriz_user_film

# MATRIZ USUARIO FILM
userFilm = leer_matriz_csv()


print(userFilm[0][23])
print(userFilm[60][23])
print(userFilm[485][23])
