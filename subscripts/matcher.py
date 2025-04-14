from collections import defaultdict

def normalize_text(text):
    return text.lower() if isinstance(text, str) else ""

def match_drugs_to_publications(drugs, pubmed, clinical_trials):
    drug_mentions = defaultdict(lambda: {
        "drug": "",
        "mentions": {
            "pubmed": [],
            "clinical_trials": [],
            "journals": []
        }
    })

    for _, row in drugs.iterrows():
        drug = row['drug']
        atccode = row['atccode']
        drug_lower = normalize_text(drug)

        # PubMed
        for _, pub in pubmed.iterrows():
            if drug_lower in normalize_text(pub['title']):
                drug_mentions[atccode]['drug'] = drug
                drug_mentions[atccode]['mentions']['pubmed'].append({
                    "id": pub['id'],
                    "title": pub['title'],
                    "journal": pub['journal'],
                    "date": pub['date']
                })
                drug_mentions[atccode]['mentions']['journals'].append({
                    "journal": pub['journal'], "date": pub['date']
                })

        # Clinical Trials
        for _, trial in clinical_trials.iterrows():
            if drug_lower in normalize_text(trial['scientific_title']):
                drug_mentions[atccode]['drug'] = drug
                drug_mentions[atccode]['mentions']['clinical_trials'].append({
                    "id": trial['id'],
                    "title": trial['scientific_title'],
                    "journal": trial['journal'],
                    "date": trial['date']
                })
                drug_mentions[atccode]['mentions']['journals'].append({
                    "journal": trial['journal'], "date": trial['date']
                })

    return drug_mentions