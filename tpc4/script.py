import re

def read_acronyms():
    acronyms = {}
    with open("pt.txt", 'r') as file:
        for line in file:
            if ':' in line:
                key, value = line.strip().split(':', 1)
                key = key.strip()
                value = value.strip()
                acronyms[key] = value

    with open("eg.txt", 'r') as file:
        for line in file:
            if ':' in line and '(' in line and ')' in line:
                key, rest = line.strip().split(':', 1)
                key = key.strip()
                value = rest[rest.find('(') + 1:rest.find(')')].strip().lower()
                acronyms[key] = value
    
    return acronyms

def replace_acronyms(text, acronyms):
    words = text.split()
    for i, word in enumerate(words):
        if word.upper() in acronyms.keys():
            words[i] = acronyms[word.upper()]
    return ' '.join(words)

def main():
    text = "Hoje não me sinto muito bem tbh."
    acronyms = read_acronyms()
    result = replace_acronyms(text, acronyms)
    print(result)

main()