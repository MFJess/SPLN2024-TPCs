import spacy
from collections import defaultdict, Counter
import argparse

# Carrega o modelo de linguagem
nlp = spacy.load("en_core_web_sm")

def analyze_entities(text):
    doc = nlp(text)
    
    entity_relations = defaultdict(Counter)

    entities = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    
    if len(entities) > 1:
        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                entity_relations[entities[i]][entities[j]] += 1
                entity_relations[entities[j]][entities[i]] += 1
    
    return entity_relations

def main():
    parser = argparse.ArgumentParser(description="Analyze entities in a text file.")
    parser.add_argument("file_path", type=str, help="Path to the text file to be analyzed.")
    args = parser.parse_args()

    with open(args.file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    relations = analyze_entities(text)
    
    print("\nRelations:")
    for entity, counter in relations.items():
        print(f"\nEntity: {entity}")
        print("  Relations:")
        for related_entity, count in counter.items():
            print(f"   - {related_entity}: {count} x")

main()
