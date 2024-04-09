import re

def regista_percentagens(palavras, total_palavras):
    percentagens = {}
    for palavra, ocorr in palavras.items():
        if palavra not in percentagens:
            percentagens[palavra] = ocorr / total_palavras
    return percentagens

def regista_percentagens_esperadas():
    percentagens_esperadas = {}

    with open("./words-top.txt", 'r') as file:
        lines = file.readlines()
    
    ocorrencias = []
    for line in lines:
        numero = re.findall(r'\b\d+\b', line)
        ocorrencias.extend(numero)
    total = sum(int(numero) for numero in ocorrencias)

    pattern = r'(.+)\s+(\d+)\s+.+'
        
    for line in lines:
        match = re.match(pattern,line)
        palavra = match.group(1)
        nr_ocorr = int(match.group(2))
        if palavra not in percentagens_esperadas.keys():
            percentagens_esperadas[palavra] = nr_ocorr / total 
    
    return percentagens_esperadas

def lista_percentagens(palavras, total_palavras):
    percentagens_esperadas = regista_percentagens_esperadas()
    percentagens = regista_percentagens(palavras, total_palavras)
    string = "=== Palavra: Percentagem Esperada (%) -> Percentagem Real (%) ===\n"
    for palavra in palavras:
        if palavra in percentagens_esperadas:
            string += palavra + ": " + str(percentagens_esperadas[palavra]) + " --> " + str(percentagens[palavra]) + "\n"
        else:
            string += ''
    print(string)