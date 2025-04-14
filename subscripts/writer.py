import json

# Enregistrement du graphe dans un fichier JSON
def save_graph_to_json(graph, path):
    with open(path, 'w') as f:
        json.dump(graph, f, indent=4, default=str)