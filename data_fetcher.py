import requests
import json
from config import PUBMED_SEARCH_URL, PUBMED_FETCH_URL, PUBMED_DB, PUBMED_RETMAX, PATIENT_RECORDS_FILE, DRUG_DB_FILE

def fetch_pubmed_data(query):
    """
    Fetches PubMed articles based on a query using ESearch and EFetch.
    (For demonstration, the EFetch response is kept as raw XML.)
    """
    params = {
        "db": PUBMED_DB,
        "term": query,
        "retmax": PUBMED_RETMAX,
        "retmode": "json"
    }
    search_response = requests.get(PUBMED_SEARCH_URL, params=params)
    if search_response.status_code != 200:
        print("Error fetching PubMed search data")
        return []
    search_results = search_response.json()
    id_list = search_results.get("esearchresult", {}).get("idlist", [])
    if not id_list:
        return []
    fetch_params = {
        "db": PUBMED_DB,
        "id": ",".join(id_list),
        "retmode": "xml"
    }
    fetch_response = requests.get(PUBMED_FETCH_URL, params=fetch_params)
    if fetch_response.status_code != 200:
        print("Error fetching PubMed article details")
        return []
    # For simplicity, we return the XML text for each article
    articles = []
    for article_id in id_list:
        articles.append({
            "title": f"PubMed Article {article_id}",
            "description": fetch_response.text
        })
    return articles

def fetch_patient_records():
    """
    Loads dummy patient records from a local JSON file.
    Expected format: a list of dicts with keys 'title' and 'description'.
    """
    try:
        with open(PATIENT_RECORDS_FILE, "r") as f:
            records = json.load(f)
        return records
    except Exception as e:
        print("Error reading patient records:", e)
        return []

def fetch_drug_info(query):
    """
    Loads drug information from a dummy JSON file and filters based on the query.
    """
    try:
        with open(DRUG_DB_FILE, "r") as f:
            drugs = json.load(f)
        filtered = [drug for drug in drugs if query.lower() in drug.get("name", "").lower() or query.lower() in drug.get("description", "").lower()]
        return filtered
    except Exception as e:
        print("Error reading drug database:", e)
        return []

def fetch_all_data(query="diabetes"):
    """
    Fetches data from PubMed, patient records, and the drug database.
    The query parameter is used to search PubMed and filter drug info.
    """
    pubmed_data = fetch_pubmed_data(query)
    patient_records = fetch_patient_records()
    drug_data = fetch_drug_info(query)
    return pubmed_data + patient_records + drug_data

if __name__ == "__main__":
    data = fetch_all_data("diabetes")
    for item in data:
        print(item["title"])
