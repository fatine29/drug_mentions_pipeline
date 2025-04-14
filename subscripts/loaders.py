import pandas as pd

# Chargement des données
def load_data(path_drugs, path_pubmed_csv, path_pubmed_json, path_clinical_trials):
    drugs = pd.read_csv(path_drugs)
    pubmed_csv = pd.read_csv(path_pubmed_csv)
    pubmed_json = pd.read_json(path_pubmed_json)
    clinical_trials = pd.read_csv(path_clinical_trials)
    pubmed = pd.concat([pubmed_csv, pubmed_json], ignore_index=True).drop_duplicates()
    return drugs, pubmed, clinical_trials