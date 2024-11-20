# millas:float = float(input('cuantas millas? '))
# km:float = millas * 1.609
# print(f'{millas} millas son {km}km')
#
# profuncidad:float = float(input('cuantos metros de profuncidad tiene? '))
# anchura:float = float(input('cuantos metros de anchura tiene? '))
# largo:float = float(input('cuantos metros de largura tiene? '))
#
# litros = (profuncidad*anchura*largo)*1000
# print(litros)
# coste:float = 14.78
# pagado:float = 20
# vueltas:float = pagado-coste
# print(vueltas)
#
#
#
# if vueltas >= 2:
#    print(f'{vueltas//2} monedas de 2 euros')
#    vueltas -= 2*(vueltas//2)
# if vueltas >= 1:
#    print(f'{vueltas//1} monedas de 1 euros')
#    vueltas -= 1*(vueltas//1)
# if vueltas >= 0.5:
#    print(f'{vueltas//0.5} monedas de 0.5 euros')
#    vueltas -= 0.5*(vueltas//0.5)
# if vueltas >= 0.2:
#    print(f'{vueltas//0.2} monedas de 0.2 euros')
#    vueltas -= 0.2*(vueltas//0.2)
# if vueltas >= 0.1:
#    print(f'{vueltas//0.1} monedas de 0.1 euros')
#    vueltas -= 0.1*(vueltas//0.1)
# if vueltas >= 0.05:
#    print(f'{vueltas//0.05} monedas de 0.05 euros')
#    vueltas -= 0.05*(vueltas//0.05)
# if vueltas >= 0.02:
#    print(f'{vueltas//0.02} monedas de 0.02 euros')
#    vueltas -= 0.02*(vueltas//0.02)
# if vueltas >= 0.01:
#    print(f'{vueltas//0.01} monedas de 0.01 euros')
# vueltas -= 0.01*(vueltas//0.01)
#
#
# peso:float = float(input('Cual es tu peso: '))
# altura:float = float(input('Cual es tu altura(en metros): '))
#
# imc:float = peso / (altura**2)
#
# if imc > 30:
#    print("Obesidad")
# elif imc >= 25:
#    print("Sobrepeso")
# elif imc >= 18.5:
#    print("Peso normal")
# else:
#    print("Bajo peso")


# frase:float = input('Cual es tu frase: ')
# primera_palabra = ''
#
# for x in frase:
#     if x == ' ':
#         break
#     primera_palabra += x
#
# print(primera_palabra)
#
# ultima_palabra_reves = ''
#
# for y in range(len(frase)-1, 0, -1):
#     if frase[y] == ' ':
#         break
#     ultima_palabra_reves += frase[y]
#
# ultima_palabra = ''
# for z in range(len(ultima_palabra_reves)-1, -1, -1):
#     ultima_palabra += ultima_palabra_reves[z]
#
# print(ultima_palabra)

#print("""
#¿Cual es la capital de España?
#1) Madrid
#2) Paris
#3) Helsinki
#""")
#while True:
#    respuesta: int = int(input('Respuesta: '))
#    if respuesta == 1:
#        print('Correcto')
#        break
#    elif 4 < respuesta < 0:
#        print('Out of range')
#    else:
#        print('Te has equivocado')
#        break
#
#print("""
#¿Quien tiene mas balones de oro?
#1) Cristiano
#2) Messi
#3) Modric
#""")
#
#while True:
#    respuesta2: int = int(input('Respuesta: '))
#    if respuesta == 2:
#        print('Correcto')
#        break
#    elif 4 < respuesta < 0:
#        print('Out of range')
#    else:
#        print('Te has equivocado')
#        break
#
#
#banco_preg = [['Preg1']]
#
#
#nota: int  = int(input('Cual es tu calificacion'))
#
#if nota < 5:
#    print('Tu calificaion es un SUSPENSO')
#elif nota < 6:
#    print('Tu calificaion es un SUFICIENTE')
#elif nota < 7:
#    print('Tu calificaion es un BIEN')
#elif nota < 9:
#    print('Tu calificaion es un NOTABLE')
#else:
#    print('Tu calificaion es EXECELENTE')
#
#
#
#def estrellas(num):
#    for x in range(num):
#        print('*', end='')


a = [1, 2, 3]


def dosYCuatr(a:list):
    print(a)

dosYCuatr(a)

cuatro = False

for i in a:
    if i == 4:
        cuatro = True


def valorMax(lista):
    max = lista[0]
    for i in range(1, len(lista)):
        if lista[i] > max1:
            max1 = lista[i]

    return max

def diferencia(lista1, lista2):
    max1 = valorMax(lista1)
    max2 = valorMax(lista2)

    resultado = max1 - max2

    return resultado    