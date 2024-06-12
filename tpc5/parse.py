import spacy

# modelo de linguagem
nlp = spacy.load("en_core_web_sm")

# Função para analisar a frase
def analyze_sentence(text):
    doc = nlp(text)
    info = []
    for token in doc:
        token_info = {
            "text": token.text,
            "lemma": token.lemma_,
            "pos": token.pos_,
            "value": token.tag_
        }
        info.append(token_info)
    return info

def main():
    text = input("Introduza o seu texto.")
    result = analyze_sentence(text)
    print("Este é o seu resultado:")
    for token_info in result:
        print(f"Text: {token_info['text']}, Lemma: {token_info['lemma']}, POS: {token_info['pos']}, Value: {token_info['value']}")

main()