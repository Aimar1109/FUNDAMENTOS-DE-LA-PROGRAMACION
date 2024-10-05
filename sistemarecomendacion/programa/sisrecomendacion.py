import utilities
import csv

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


def consultaGenero(genero:str, lista_ratings):
    valoracionGenero = []
    genero = genero.capitalize()
    for valoracion in lista_ratings:
        if valoracion['genres'] == genero:
            valoracionGenero.append(valoracion)
    return valoracionGenero

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


def lista_a_csv(lista_clasificada):
    with open('peliculas_clasificadas', mode='w', newline='')as file:
        encabezados = lista_clasificada[0].keys()

        escritor_csv = csv.DictWriter(file, fieldnames=encabezados)
    
        escritor_csv.writeheader()

        escritor_csv.writerows(lista_clasificada)


def recomendacionGeneroRating(genero, ratings):
    lista_genero = consultaGenero(genero, ratings)

#lista_a_csv(clasificacionRating(ratings))

### RATINGS CLASIFICADOS ###
ratings_clasificados = []
with open('peliculas_clasificadas') as file:
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



def algoritmoRecomendacionRating(genero, li_clas):
    li_genre = []
    for peli in li_clas:
        if genero == peli['genre']:
            li_genre.append(peli)
    return sorted(li_genre, key=lambda x: x["rating"], reverse=True)[:5]
    

#print(algoritmoRecomendacionRating('Drama', ratings_clasificados))


def matrizUserPelicula(lista_rating, ratings_clasificados):
    userFilm = []
    userFilm.append([film['title'] for film in ratings_clasificados])
    ratings_promedio = [film['rating'] for film in ratings_clasificados]
    userFilm[0].insert(0, 'X')
    #print(userFilm)

    for user in range(1, lista_rating[-1]['userId']+1):
        lista = [f'user-{user}']
        peliculas_usuario = [film['title'] for film in lista_rating if film["userId"] == user]
        ratings_usuario = [film['rating'] for film in lista_rating if film["userId"] == user]
        #print(peliculas_usuario)
        for film in userFilm[0]:
            if film in peliculas_usuario:
                indice = peliculas_usuario.index(film)
                lista.append(ratings_usuario[indice])
            else:
                lista.append(ratings_promedio[userFilm.index(film)])
        userFilm.append(lista)
    return userFilm


def matriz_a_csv(userFilm):
    with open('matriz_peliculas', mode='w', newline='')as file:
        escritor_csv = csv.writer(file)

    # Escribir todas las filas
        escritor_csv.writerows(userFilm)

matriz_a_csv(matrizUserPelicula(ratings, ratings_clasificados))


def leer_matriz_csv():
    userFilm = []
    with open('matriz_peliculas')as file:
        csv_reader = csv.reader(file, delimiter=',')

        for fila in csv_reader:
            userFilm.append(fila)
    return userFilm

userFilm = leer_matriz_csv()

for fila in userFilm:
    print(fila)
