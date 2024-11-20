import numpy as np

#parking = []
#
#for i in range(5):
#    fila = []
#    for j in range(5):
#        fila.append(False)
#    parking.append(fila)
#
#parking[1][1] = True
#for x in parking:
#    print(x)
#
#
#def matriz(num:int) -> list[list]:
#    lista:list = []
#    for i in range(1, num+1):
#        fila = []
#        for x in range(num):
#            fila.append(i)
#        lista.append(fila)
#    return lista
#
#matrix = matriz(5)
#
#def suma_matriz(matriz:list[list]) -> int:
#    resultado:int = 0
#    for y in matriz:
#        for x in y:
#            resultado += x
#    return resultado
#
#print(suma_matriz(matrix))
#
#def matriz_columnas(num:int) -> list[list]:
#    matriz:list[list] = []
#    for y in range(1, num+1):
#        fila:list = []
#        for x in range(1, num+1):
#            fila.append(x)
#        matriz.append(fila)
#    return matriz
#
#print(matriz_columnas(4))

#def indentidad(num:int) -> list[list]:
#    matriz:list[list] = []
#    for i in range(num):
#        fila:list = []
#        for x in range (num):
#            if i == x:
#                fila.append(1)
#            else:
#                fila.append(0)
#        matriz.append(fila)
#    return matriz
#
#m1 = indentidad(10)
#m2 = indentidad(10)
#
#def suma_matrices(matriz1:list[list], matriz2:list[list]) -> list[list]:
#    matriz_suma:list[list] = []
#    for y in range(len(matriz1)):
#        fila:list = []
#        for x in range(len(matriz1[0])):
#            fila.append(matriz1[y][x] + matriz2[y][x])
#        matriz_suma.append(fila)
#
#    return matriz_suma
#
#m3 = suma_matrices(m1, m2)
#
#for y in m3:
#    print(y)
#
#
#def limpia_matriz(matriz:list[list])->list[list]:
#    
#    filasBorrar = []
#    columnasBorrar = []
#
#    for y in range(len(matriz)):
#        filaZero = True
#        for x in range(len(matriz[y])):
#            if matriz[y][x] != 0:
#                filaZero = False
#                break
#        if filaZero:
#            filasBorrar.append(y)
#
#
#    for y in range(len(matriz)):
#        columna = []
#        for x in range(len(matriz[y])):
#            columna.append(matriz[x][y])
#
#        columnaZero = True
#        for x in range(len(columna)):
#            if columna[x] != 0:
#                columnaZero = False
#                break
#        if columnaZero:
#            columnasBorrar.append(y)
#
#    matriz_limpia = []
#    for y in range(len(matriz)):
#        if y not in filasBorrar:
#            fila = []
#            for x in range(len(matriz[y])):
#                if x not in columnasBorrar:
#                    fila.append(matriz[y][x])
#            matriz_limpia.append(fila)
#    return matriz_limpia
#
#
#
#m = limpia_matriz([
#                [0, 0, 3, 0, 0], 
#                [0, 0, 0 ,0 ,0], 
#                [0, 6, 1, 0, 0], 
#                [0, 0, 0, 0, 0],
#                [0, 0, 0, 0, 1]])
#
#for x in m:
#    print(x)
#def letrasONo(frase:str) -> list[int]:
#    lista:list = []
#    for x in range(len(frase)):
#        if frase[x].isalpha():
#            lista.append(1)
#        else:
#            lista.append(0)
#    return(lista)
#
#
#print(letrasONo("abcd 12 ABC"))

#def sumaCobro(facturas:dict) -> float:
#    suma:float = 0
#    for x in facturas.values():
#        suma += x
#    return suma



#def traductor(frase:str) -> str:
#    palabras = {"hello": "hola", "how": "como", "are": "estar", "you": "tu", "me": "yo"}
#    frase_ingles:list = frase.split(" ")
#    frase_cast:list = []
#    for i in range((len(frase_ingles))):
#        frase_cast.append(palabras[frase_ingles[i]])
#    frase_str = ""
#    for x in frase_cast:
#        frase_str += (x + " ")
#    return frase_str
#
#print(traductor("hello how are you"))


#pedidos = {"Pedido_001": [
#    {"producto": "Camiseta", "cantidad": 2, "precio_unitario": 20.0, "descuento": 10},
#    {"producto": "Pantalón", "cantidad": 1, "precio_unitario": 50.0, "descuento": 0}
#],
#    "Pedido_002": [
#    {"producto": "Sudadera", "cantidad": 1, "precio_unitario": 50.0, "descuento": 10},
#    {"producto": "Pantalón", "cantidad": 1, "precio_unitario": 60.0, "descuento": 0}
#],
#    "Pedido_003": [
#    {"producto": "Zapatillas", "cantidad": 1, "precio_unitario": 100.0, "descuento": 10},
#    {"producto": "Pantalón", "cantidad": 2, "precio_unitario": 50.0, "descuento": 0}
#]
#}
#
#def añadir_pedido(pedidos:dict, codigo_pedido:str) -> dict:
#
#    pedido = []
#
#    respuesta = "s"
#
#    while(respuesta.lower() == "s"):
#        fila = {}
#        
#        # Pedimos los datos del usuario
#        producto = input("Introduce el producto: ")
#        cantidad = int(input("Introduce la cantidad: "))
#        precio_unitario = float(input("Introduce el precio unitario: "))
#        descuento = int(input("Introduce el descuento: "))
#
#        # Guardamos los datos en la fila
#        fila["producto"] = producto
#        fila["cantidad"] = cantidad
#        fila["precio_unitario"] = precio_unitario
#        fila["descuento"] = descuento
#
#        pedido.append(fila)
#
#        respuesta = input("¿Desea seguir introduciendo productos?")
#
#
#    pedidos[codigo_pedido] = pedido
#    
#    return pedidos
#
##print(añadir_pedido(pedidos, "Pedido_004"))
#
#def calcular_total_pedido(pedidos:dict, codigo_pedido:str)-> float:
#    resultado:float = 0.0
#    
#    # Obtener el pedido
#    pedido = pedidos[codigo_pedido]
#
#    # Calcular el precio total
#    precio_final:float = 0.0
#    for producto in pedido:
#        precio_total = producto["cantidad"] * producto["precio_unitario"]
#
#        # Aplicar el descuento
#        precio_total = precio_total - precio_total *(producto["descuento"]/100)
#
#        precio_final += precio_total
#        
#    # Devolver el valor calculado.
#    return precio_final
#
#
#def pedidos_minimos(pedidos:dict, precio_min: float):
#    pedidos_rango:dict = {}
#    for pedido in pedidos:
#        if calcular_total_pedido(pedidos, pedido) >= precio_min:
#            pedidos_rango[pedido] = pedidos[pedido]
#    return pedidos_rango
#
#
##print(pedidos_minimos(pedidos, 100))
#
#def producto_generado(pedidos:dict, n_producto:str):
#    total:float = 0
#    for pedido in pedidos:
#        for producto in pedidos[pedido]:
#            if producto['producto'] == n_producto:
#                precio:float = producto['cantidad']*(producto['precio_unitario']*(1-(producto['descuento']*0.01)))
#                total += precio
#    return total
#
#
#print(producto_generado(pedidos, "Pantalón"))

calificaciones = {
    "Matematicas": [("Juan", 8.5), ("María", 9.0), ("Luis", 7.8)],
    "Fisica": [("Juan", 6.5), ("María", 8.0), ("Luis", 7.0)],
    "Quimica": [("Juan", 7.0), ("María", 9.5), ("Luis", 8.2)]
}


def añadir_calificacion(calificaciones):

    nombre = input("Nombre del estudiante: ")
    asignatura = input("Asignatura: ").capitalize()
    nota = float(input("Nota del estudiante: "))
    if asignatura in calificaciones.keys():
        calificaciones[asignatura].append((nombre, nota))
    else:
        calificaciones[asignatura] = [(nombre, nota)]
    return calificaciones


def media_asignaturas(calificaciones, asignatura) -> float:
    suma:float = 0
    for tu in calificaciones[asignatura]:
        suma += tu[1]
    return suma / len(calificaciones[asignatura])


def mejo_nota(calificaciones, asignatura) -> str:
    mayor:tuple = calificaciones[asignatura][0]
    for tu in calificaciones[asignatura]:
        if tu[1] > mayor[1]:
            mayor = tu
    return mayor[0]


def listar_asignaturas(calificaciones) -> None:
    for asignatura in calificaciones:
        print(asignatura + ":")
        for notas in calificaciones[asignatura]:
            print(notas[0] + " --> " + str(notas[1]))
        print()



def eliminar_calificacion(calificaciones, nombre, asignatura):
    for asignatura in calificaciones:
        for notas in calificaciones[asignatura]:
            if notas[0] == nombre:
                calificaciones[asignatura].remove(notas)
    return calificaciones


def estudiantes_dict(calificaciones):
    estudiantes = {}
    for asignatura in calificaciones:
        for nota in calificaciones[asignatura]:
            if nota[0] not in estudiantes.keys():
                estudiantes[nota[0]] = [(asignatura, nota[1])]
            else:
                estudiantes[nota[0]].append((asignatura, nota[1]))

    return estudiantes

print(estudiantes_dict(calificaciones))