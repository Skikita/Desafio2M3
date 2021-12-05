"""
Diseñar un programa que dados una serie de 15 números pueda devolver: 
el mayor, el menor, la suma y el promedio de todos los números
(los 15 números deberán estar ingresados en lista de forma estática)
"""

una_lista_numeros = [100,2,33,4,5,687,7,8,9,10,11,12,130,14,15]

def sumatoria(una_lista_numeros):
    suma = 0
    for numero in una_lista_numeros: 
        suma += numero
    return suma

def promedio(una_lista_numeros):
    return sumatoria(una_lista_numeros)/len(una_lista_numeros)

def menor(una_lista_numeros):
    return min(una_lista_numeros)

def mayor(una_lista_numeros):
    return max(una_lista_numeros)
