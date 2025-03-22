# PubMed API configuration
PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
PUBMED_DB = "pubmed"
PUBMED_RETMAX = 5  # Number of articles to retrieve

# Dummy patient records file (create this JSON file with sample patient data)
PATIENT_RECORDS_FILE = "dummy_patient_records.json"

# Dummy drug database file (create this JSON file with sample drug info)
DRUG_DB_FILE = "dummy_drug_database.json"

# Pinecone configuration
PINECONE_API_KEY = "your_pinecone_api_key_here"  # Replace with your Pinecone API key
PINECONE_ENV = "us-west1-gcp"  # Replace with your Pinecone environment
PINECONE_INDEX_NAME = "healthassist-index"
VECTOR_DIMENSION = 384  # Using all-MiniLM-L6-v2 embeddings (384 dimensions)

# OpenAI API Key
OPENAI_API_KEY = "your_openai_api_key_here"  # Replace with your OpenAI API key

# Sentence Transformer model for generating embeddings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
