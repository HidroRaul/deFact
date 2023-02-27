'''
Cálculo de los números primos menores de un determinado valor.
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def primos(limSup):

    primos=[1]
    i=2
    while i<=limSup:
        primo=True
        for j in range(1,len(primos),1):
            if i%primos[j]==0:
                primo=False
                break # Sale del bucle for en el momento en el que aparece un divisor
        if primo==True:        
            primos.append(int(i))
        i+=1
    return primos
