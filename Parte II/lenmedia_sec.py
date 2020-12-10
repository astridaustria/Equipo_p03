#!/home/dacosta/anaconda3/bin/python3.8
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 08:59:16 2020

@author: dacosta
"""

##Práctica 02 - Herramientas bioinformáticas en Python
##4/11/2020
##Por Daniel E. Acosta


def len_fasta (fname): #obtiene el promedio de la longitud de las secuencias de un archivo fasta
    f = open (fname, 'r')
    L = []
    n = 0
    p = 0
    c = 0
    for linea in f:
        if (linea [0] != '>' ):
            L +=  linea.strip() 
            p += 1
    for line in L:
        a = len(line)
        n += a
        
    c = n/p
    return c

len_fasta("Mgenitalium_1.fasta") 
len_fasta("Mgenitalium_2.fasta") 
