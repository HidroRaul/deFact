'''
Factores de un número
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import primos #Archivo con la función que calcula los números primos

print("Factores de un entero. Introduce el número entero: ")
numFactor=int(input())

#Variable en la que se van a almacenar los factores. 1 es siempre factor.
factores=[1]

#Números primos menores o iguales que el número a descomponer en factores
primosMenores = primos.primos(numFactor)

while len(primosMenores)>1:
    for i in range(1,len(primosMenores),1):
        #Se comprueba si el primer primo de la lista es factor
        if numFactor%primosMenores[i]==0:
            numFactor=numFactor/primosMenores[i]
            factores.append(primosMenores[i])
            #Se descartan los primos que son menores que el número dividido por los factores
            primosMenores = [x for x in primosMenores if x <= numFactor]
            break

print(factores)
