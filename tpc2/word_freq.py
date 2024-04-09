#!/usr/bin/env python3
'''
NAME
   word_freq - Calculates the word frequency in a text

SYNOPSIS
   word_freq [options] input_files
   options: 
        -m 20 : Shows the 20th most frequent words
        -n : Order alfabetically
        -i : Order ignoring capitalization
        -c : Shows relative percentage difference of the number of times the word appears in the text relative to the average value
   
Description'''

from jjcli import * 
from collections import Counter
import sys
import re
from utils import *

cl=clfilter("cinm:", doc=__doc__)
def tokaniza(texto):
    palavras = re.findall(r'\w+(?:\-\w+)?|[.,?!;:—]+', texto)
    return palavras

def imprime(lista):
    for palavra, n_ocorr in lista:
        print(f"{palavra} --> {n_ocorr}")

for txt in cl.text(): 
    lista_palavras = tokaniza(txt)
    ocorr = Counter(lista_palavras)
    
    lista_palavras_minusculas = set(map(str.lower, lista_palavras))
    ocorr_minusculas = Counter(lista_palavras_minusculas)
    
    if "-n" in cl.opt and "-m" in cl.opt:
        imprime(sorted(ocorr.most_common(int(cl.opt.get("-m")))))
    
    elif "-m" in cl.opt:
        imprime(ocorr.most_common(int(cl.opt.get("-m"))))

    elif "-n" in cl.opt:
        imprime(sorted(ocorr.items()))

    elif "-i" in cl.opt:
        imprime(ocorr_minusculas.items())

    elif "-c" in cl.opt:
        total_palavras = len(lista_palavras)
        lista_percentagens(ocorr,total_palavras)
    
    else:
        imprime(ocorr.items())

def main():
    regista_percentagens_esperadas()
main()