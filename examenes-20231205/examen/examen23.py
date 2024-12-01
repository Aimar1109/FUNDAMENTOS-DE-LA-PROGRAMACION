import random

users = []
lista_palabras = []

username = {}
post = {}


def datos_prueba(users):
    user1 = {'username': 'ablago',
             'posts' : [
                 {'uid': 134, 'text': 'Feliz 2023', 'hashtags': ['felicidad', 'felicidad', 'alegría']},
                 {'uid': 253, 'text': '¡Feliz año!' , 'hashtags': ['felicidad', 'felicidad']},
                 {'uid': 124, 'text': 'Mal examen de inglés', 'hashtags': ['felicidad', 'felicidad', 'felicidad']}
                ]
            }
    user2 = {'username': 'aimar',
             'posts' : [
                 {'uid': 104, 'text': 'Feliz 2021', 'hashtags': ['feliz', '2021', 'alegría']},
                 {'uid': 233, 'text': '¡Feliz cumpleaños!' , 'hashtags': ['deseos', 'esperanza']},
                 {'uid': 114, 'text': 'Muy bien el examen de mate', 'hashtags': ['mate', 'examen', 'alegría']}
                ]
            }
    users.append(user1)
    users.append(user2)
    return users


def cargar_palabras():
    with open('hinojosa.csv', 'r', encoding='utf-8') as f:
        dict_palabras = {}
        for fila in f:
            fila = fila.strip().split(';')
            dict_palabras[fila[0]] = float(fila[1])
    return dict_palabras


def generador_uid(users):
    unico = False
    while not unico:
        uid = random.randint(111111, 999999)
        nuevo = False
        for user in users:
            for post in user['posts']:
                if uid == post['uid']:
                    nuevo = True
                    break
            if nuevo:
                break
        if nuevo:
            continue
        unico = True
    return uid

def generador_hashtags(dict_palabras):
    unicos = False
    palabras = []
    while not unicos:
        n = random.choice([x for x in dict_palabras.keys()])
        if n not in palabras:
            palabras.append(n)
        if len(palabras) == 3:
            return palabras

def generar_users(users:list, palabras:dict):
    contador = 0
    for us_n in range(1000):
        user = {}
        user['username'] = f'user-{us_n}'
        user['posts'] = []
        for pos in range(20):
            post = {}
            post['uid'] = generador_uid(users)
            post['text'] = f'text-{contador}'
            contador += 1
            post['hashtags'] = generador_hashtags(palabras)
            user['posts'].append(post)
        users.append(user)
    return users

def calcular_media(hashtags, palabras):
    media = 0
    for h in hashtags:
        if h in palabras.keys():
            media += palabras[h]
        else:
            media += 5
    return media / len(hashtags)

def post_menor_puntos(users, palabras):
    menor = [users[0]['posts'][0], calcular_media(users[0]['posts'][0]['hashtags'], palabras)]
    for user in users:
        for pos in user['posts']:
            media = calcular_media(pos['hashtags'], palabras)
            if menor[1] > media:
                menor = [pos, media]

    return menor[0]


def clasificar_user(users, palabras):
    users_clasificados = {'mal': [],
                          'regular': [],
                          'bien' : []
                          }
    
    for user in users:
        media = 0
        for pos in user['posts']:
            media += calcular_media(pos['hashtags'], palabras)
        media = media / len(user['posts'])
        if media < 5:
            users_clasificados['mal'].append(user)
        elif media < 6:
            users_clasificados['regular'].append(user)
        else:
            users_clasificados['bien'].append(user)
    
    return users_clasificados


def guardar_clasificacion(users, users_clasificados):
    with open('clasifica.csv', 'w', encoding='utf-8') as f:
        for user in users:
            if user in users_clasificados['mal']:
                linea = user['username']+';mal;\n'
            elif user in users_clasificados['regular']:
                linea = user['username']+';regular;\n'
            else:
                linea = user['username']+';bien;\n'
            f.write(linea)
        f.close()

if __name__ == '__main__':
    dict_palabras = cargar_palabras()
    list_users = []
    list_users = generar_users(list_users, dict_palabras)
    list_users = datos_prueba(list_users)
    print(post_menor_puntos(list_users, dict_palabras))
    clasificados = clasificar_user(list_users, dict_palabras)
    guardar_clasificacion(list_users, clasificados)