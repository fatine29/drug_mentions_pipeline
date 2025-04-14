import json
from collections import defaultdict

def find_top_journal_from_json(json_path):
    with open(json_path, 'r') as f:
        graph = json.load(f)

    journal_to_drugs = defaultdict(set)

    for atccode, info in graph.items():
        for mention in info['mentions']['journals']:
            journal_to_drugs[mention['journal']].add(atccode)

    top_journal = max(journal_to_drugs.items(), key=lambda x: len(x[1]))
    return top_journal[0], len(top_journal[1])

if __name__ == "__main__":
    path = "output/drug_mentions_graph.json"
    journal, count = find_top_journal_from_json(path)
    print("Traitement ad-hoc terminé.")
    print(f"Journal avec le plus de médicaments différents : {journal} ({count} drugs)")
