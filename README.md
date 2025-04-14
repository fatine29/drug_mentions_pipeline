# Drug Mentions Pipeline

## Objectif

Ce projet a pour but de construire une **data pipeline en Python** permettant de :
- Lier des médicaments (`drugs.csv`) à des publications scientifiques (`pubmed.csv`, `pubmed.json`, `clinical_trials.csv`)
- Générer un **graphe JSON** représentant les liaisons entre médicaments, articles et journaux
- Réaliser une **analyse ad-hoc séparée** pour identifier le **journal mentionnant le plus de médicaments différents**

---

## Structure du projet

Voici la structure du dossier à avoir en local pour faire tourner le script

```
data_pipeline_project/
├── data/                    # Données source (dossier non versionné dans Git, à ajouter au dossier)
├── output/                  # JSON généré (également non versionné, à ajouter au dossier)
├── drug_mentions_pipeline   # Dossier cloné
│   ├── subscripts/          # Sous-scripts pour chacune des étapes
│   │   ├── loaders.py       # Fonction pour charger les données
│   │   ├── matcher.py       # Fonction pour identifier lorsqu'un médicament est mentionné dans une publication
│   │   ├── builder.py       # Fonction pour construire le graph
│   │   ├── saver.py         # Fonction pour enregistrer le graph .JSON dans le dossier output
│   ├── main.py              # Script principal
│   ├── ad_hoc_analysis.py   # Analyse ad-hoc séparée
│   ├── requirements.txt     # Dépendances Python environnement virtuel
│   └── README.md                
```

---

## Installation

1. Créer un dossier nommé "data_pipeline_servier_project"

2. Importer dans ce dossier le dossier data contenant toutes les données sources

3. Créer le dossier output

4. Cloner le dépôt :
```bash
git clone https://github.com/ton-utilisateur/drug-mentions-pipeline.git
cd drug-mentions-pipeline
```

5. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate
```

6. Installer les dépendances :
```bash
pip install -r requirements.txt
```

---

## Exécution de la pipeline

Place les fichiers dans le dossier `data/`, puis exécute :

```bash
python main.py
```

Le résultat est généré dans `output/drug_mentions_graph.json`.

---

## Traitement Ad-Hoc (séparé)

Permet de retrouver le **journal qui mentionne le plus de médicaments différents** à partir du fichier JSON généré :

```bash
python ad_hoc_analysis.py
```

Exemple de sortie :
```
Journal avec le plus de médicaments différents : Journal of Medicine (12 drugs)
```

---

## Scalabilité (Big Data)

Pour gérer des volumes massifs (plusieurs To ou millions de fichiers).

**Principaux points :**
- Utiliser Spark ou Dask au lieu de pandas pour effectuer du calcul distribuel des bases de données massives
- Remplacer CSV/JSON par Parquet (nous permet d'avoir les données format colonne)