import utilities, csv
import numpy as np

# IMPORT RATINGS_SIMPLICADO TO THE PROGRAM
ratings = []
with open('ratings_simplificado.csv', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=';')
    primera = True
    for fila in csv_reader:
        if not primera:
            ratings.append({filaZero[0]: int(fila[0]),
                            filaZero[1]: int(fila[1]),
                            filaZero[2]: float(fila[2]),
                            filaZero[3]: utilities.timestamp_to_date(int(fila[3])),
                            filaZero[4]: fila[4],
                            filaZero[5]: fila[5]
                            })
        else:
            filaZero = fila
            primera = False


# FUNCIONES DE EJERCICIOS
def consultaEspecifica(valoracionId, lista_ratings):
    return lista_ratings[valoracionId]


def anyadirValoracion(userId, movieId, rating, timestamp, title, genres, lista_ratings):
    lista_ratings.apped({'userId': userId,
                         'movieId': movieId,
                         'rating': rating,
                         'timestamp': timestamp,
                         'title': title,
                         'genres': genres,
                         })
    return lista_ratings


def modificarValoracion(id, campo, lista_ratings):
    pass


def consultaUser(userId, lista_ratings):
    user_ratings = []
    for rating in lista_ratings:
        if rating['userId'] == userId:
            user_ratings.append(rating)
    return user_ratings


def consultaGenero(genero: str, lista_ratings):
    valoracionGenero = []
    genero = genero.capitalize()
    for valoracion in lista_ratings:
        if valoracion['genres'] == genero:
            valoracionGenero.append(valoracion)
    return valoracionGenero


# CLASIFICACION DE LOS RATINGS (min 100v views)
def clasificacionRating(lista_ratings):
    peliculas_clasificacadas = []
    for pelicula in lista_ratings:
        if pelicula['genres'] == '':
            continue
        moveId = pelicula['movieId']
        rating = 0
        contador = 0
        for pelicula_comparar in lista_ratings:
            if moveId == pelicula_comparar['movieId']:
                contador += 1
                rating += pelicula_comparar['rating']
                lista_ratings.remove(pelicula_comparar)
        if contador < 100:
            continue
        rating = rating / contador
        pelicula_añadir = {'moveId': moveId,
                           'title': pelicula['title'],
                           'rating': round(rating, 3),
                           'genre': pelicula['genres'],
                           'views': contador,
                           }
        print(pelicula_añadir)
        peliculas_clasificacadas.append(pelicula_añadir)
    return peliculas_clasificacadas


# CREAR CSV PARA LA CLASIFICACION DE FILMS
def lista_a_csv(lista_clasificada):
    with open('peliculas_clasificadas.csv', mode='w', newline='')as file:
        encabezados = lista_clasificada[0].keys()

        escritor_csv = csv.DictWriter(file, fieldnames=encabezados)

        escritor_csv.writeheader()

        escritor_csv.writerows(lista_clasificada)


# lista_a_csv(clasificacionRating(ratings))


### RATINGS CLASIFICADOS ###
ratings_clasificados = []
with open('peliculas_clasificadas.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    primera = True
    for fila in csv_reader:
        if not primera:
            ratings_clasificados.append({filaZero[0]: int(fila[0]),
                                         filaZero[1]: fila[1],
                                         filaZero[2]: float(fila[2]),
                                         filaZero[3]: fila[3],
                                         filaZero[4]: int(fila[4]),
                                         })
        else:
            filaZero = fila
            primera = False


# ALGORITMO SIMPLE
def algoritmoRecomendacionRating(genero, li_clas):
    li_genre = []
    for peli in li_clas:
        if genero == peli['genre']:
            li_genre.append(peli)
    return sorted(li_genre, key=lambda x: x["rating"], reverse=True)[:5]


# print(algoritmoRecomendacionRating('Drama', ratings_clasificados))


# MATRIZ DE FILMS USERS
def matrizUserPelicula(lista_rating, ratings_clasificados):
    userFilm = []
    userFilm.append([film['title'] for film in ratings_clasificados])
    film_num = len(userFilm[0])
    # ratings_promedio = [film['rating'] for film in ratings_clasificados]
    userFilm[0].insert(0, 'X')
    # print(userFilm)

    for user in range(1, lista_rating[-1]['userId']+1):
        lista = [f'user-{user}']
        peliculas_usuario = [film['title']
                             for film in lista_rating if film["userId"] == user]
        ratings_usuario = [film['rating']
                           for film in lista_rating if film["userId"] == user]
        for film in userFilm[0][1:]:
            if film in peliculas_usuario:
                indice = peliculas_usuario.index(film)
                lista.append(ratings_usuario[indice])
            else:
                lista.append(-1)

        if ((-1)*film_num) == sum(lista[1:]):
            continue
        userFilm.append(lista)
    return userFilm


def promedios(matriz):
    for fila in matriz:
        if fila[0] == 'X':
            continue
        user = fila.pop(0)
        lista_pro = [x for x in fila if x != -1]
        promedio = round((sum(lista_pro)/len(lista_pro)), 0)
        for r in fila:
            if r == -1:
                fila[fila.index(r)] = promedio
        fila.insert(0, user)

    return matriz


# CREANDO CSV
def matriz_a_csv(userFilm, fichero):
    with open(f'{fichero}.csv', mode='w', newline='')as file:
        escritor_csv = csv.writer(file)

    # Escribir todas las filas
        escritor_csv.writerows(userFilm)


# matriz_a_csv((matrizUserPelicula(ratings, ratings_clasificados)), 'matriz_peliculas')


def leer_matriz_csv():
    userFilm = []
    with open('matriz_peliculas.csv')as file:
        csv_reader = csv.reader(file, delimiter=',')

        for fila in csv_reader:
            for x in fila:
                try:      
                    fila[fila.index(x)] = float(x)
                except:
                    pass
            userFilm.append(fila)
    return userFilm


userFilm = leer_matriz_csv()
userFilm_prom = promedios(userFilm)


def similitud(userFilm_prom):
    matriz = [x[1:] for x in userFilm_prom[1:]]
    similitud = []
    for user_y in matriz:
        lista = []
        indice = matriz.index(user_y)
        for user_x in matriz:
            if indice == matriz.index(user_x):
                lista.append(1.0)
            else:
                user_y = np.array(user_y)
                user_x = np.array(user_x)
                producto_escalar = np.dot(user_y, user_x)
                modulos = np.linalg.norm(user_y) * np.linalg.norm(user_x)
                lista.append(float(producto_escalar/modulos))
        similitud.append(lista)
    return similitud


#matriz_a_csv(similitud(userFilm_prom), 'similitud')

matriz_similitud = similitud(userFilm_prom)

def sistemaderecomendacion(idUsuario, matriz_similitud, userFilm):
    usuario_mas_parecido = matriz_similitud[idUsuario].index(max([x for x in matriz_similitud[idUsuario] if x != 1.0]))
    usuario = userFilm[idUsuario+1]
    usuario_mas_parecido = userFilm[usuario_mas_parecido+1]


sistemaderecomendacion(0, matriz_similitud, userFilm)
