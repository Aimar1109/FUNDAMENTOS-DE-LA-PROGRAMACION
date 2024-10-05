def contar_segundos(hora, minutos, segundos):
    return hora*60*60 + minutos*60 + segundos


def separar_mayores(lista, numero):
    return [ x for x in lista if x>numero]


def login(intentos):
    user = "user1"
    contra = "pass1"
    num = 0
    while num < intentos:
        user_input = input("Introduce el usuario:")
        contra_input = input("Introduce la contraseña:")
        if user_input == user and contra_input == contra:
            return True
        else:
            print("Datos incorrectos")
    print("Te has quedado sin intentos!")


def ganador(lista):
    tiempos = [contar_segundos(x[1][0], x[1][1], x[1][2]) for x in lista]
    tiempos_or = tiempos.copy()
    tiempos_or.sort()
    contador = 0
    p_ganador  = 0
    comparador = tiempos_or[0]
    while contador < len(tiempos):
        if comparador == tiempos[contador]:
            p_ganador = contador
        contador += 1
    return lista[p_ganador]

lista = [["Piloto1",[1,22,10]], 
         ["Piloto2",[1,20,13]], 
         ["Piloto3",[1,19,18]]]

print(ganador(lista))