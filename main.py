from subscripts.loaders import load_data
from subscripts.matcher import match_drugs_to_publications
from subscripts.builder import build_graph
from subscripts.writer import save_graph_to_json

def main():
    print("Chargement des données...")
    drugs, pubmed_df, clinical_trials_df = load_data('data/drugs.csv',
                                                    'data/pubmed.csv',
                                                    'data/pubmed.json',
                                                    'data/clinical_trials.csv')
    print("Données chargées avec succès !")

    print("Recherche des correspondances drug ↔ publications/essais cliniques/journals...")
    drug_mentions = match_drugs_to_publications(drugs, 
                                                pubmed_df, 
                                                clinical_trials_df)

    print("Construction du graphe...")
    graph = build_graph(drug_mentions)

    print("Sauvegarde du graphe en JSON...")
    save_graph_to_json(graph, 'output/drug_mentions_graph.json')
    print("Graph enregistré avec succès !")


if __name__ == "__main__":
    main()
