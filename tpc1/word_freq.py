#!/usr/bin/env python3
'''
NAME
   word_freq - Calculates the word frequency in a text

SYNOPSIS
   word_freq [options] input_files
   options: 
        -m 20 : Shows the 20th most frequent words
        -n : Order alfabetically
   
Description'''

from jjcli import * 
from collections import Counter
import sys
import re

cl=clfilter("nm:", doc=__doc__)
print(cl.opt)
def tokaniza(texto):
    palavras = re.findall(r'\w+(?:\-\w+)?|[.,?!;:—]+', texto)
    return palavras

def imprime(lista):
    for palavra, n_ocorr in lista:
        print(f"{palavra} --> {n_ocorr}")
        
for txt in cl.text(): 
    lista_palavras = tokaniza(txt)
    ocorr = Counter(lista_palavras)
    
    if "-n" in cl.opt and "-m" in cl.opt:
        imprime(sorted(ocorr.most_common(int(cl.opt.get("-m")))))
    
    elif "-m" in cl.opt:
        imprime(ocorr.most_common(int(cl.opt.get("-m"))))

    elif "-n" in cl.opt:
        imprime(sorted(ocorr.items()))
    
    else:
        imprime(ocorr.items())



