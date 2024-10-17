# AIMAR MARDONES

#LIBRERIAS
import math, random


# EJERCICIO 1
def convertir_grados(radianes:int):
    return radianes *(180/math.pi)

print(convertir_grados(1))

print('')

#EJERCICIO 2
def encontrar_pares(lista:list):
    # Lista para guadar solo los numeros pares
    pares:list = []
    # Recorre la lista introducida
    for i in lista:
        # Comprueba si el numero es par y lo añade a una nueva lista
        if (i % 2)==0:
            pares.append(i)
    return pares

print(encontrar_pares([1, 2, 3, 4, 5, 6]))
print(encontrar_pares([11, 13, 14, 16, 17]))

print('')

#EJERCICIO 3
def adivinar_numero():
    # Variable que guardan el numero aleatorio y el numero de intentos
    num_aleatorio:int = random.randint(1, 10)
    num_intentos:int = 4
    print(f'¡Adivina el numero aleatorio del 1-10!\n¡Tienes {num_intentos} intentos!')
    # Bucle que hace que solo tengas cuatro intentos
    for i in range(num_intentos):
        # Manego de datos fuera de el rango y que no sean numeros
        while True:
            try:
                intento:int = int(input('Introduce un número: '))
                if 1 > intento or intento > 10:
                    print('Valor fuera de rango, introduce un numero entre el 1 y el 10.')
                    continue
            except ValueError:
                print('Valor incorrect, introduce un numero entre el 1 y el 10.')
                continue
            break
        # Comprobando si el valor introducido y el numero aleatorio coinciden
        if intento == num_aleatorio:
            print('¡Correcto!')
            print(f'Numero de intentos: {i+1}')
            return True
        print('¡Inténtalo de nuevo!')
        print(f'Numero de intentos: {i+1}')
        
    print(f'Perdiste! El numero era: {num_aleatorio}')
    return False

adivinar_numero()

print('')

#EJERCICIO 4
def calcular_promedio_temperatura(ciudades:list):
    # Lista nueva para guadar los nombres y sus promedios
    promedios:list = []
    # Bucle que recorre la lista de ciudades
    for ciudad in ciudades:
        # Añade un tupla con el primer valor de la lista que es el numbre de la ciudad y luego el prodemio
        promedios.append((ciudad[0], round((sum(ciudad[1])/len(ciudad[1])), 2)))
    return promedios

print(calcular_promedio_temperatura([["Ciudad1", [23, 25, 22]], 
                                     ["Ciudad2", [15, 14, 16]], 
                                     ["Ciudad3", [28, 30, 29]]]))
