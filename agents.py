import threading
import time
import numpy as np
from data_fetcher import fetch_all_data
from processor import process_data, model
from vector_db import VectorDB

# Global vector database instance
vector_db = None

def data_collector_agent(interval=300, query="diabetes"):
    """
    Periodically collects healthcare data from PubMed, patient records, and drug database,
    then updates the vector database.
    """
    global vector_db
    while True:
        print("Data Collector: Fetching new healthcare data...")
        data = fetch_all_data(query)
        if data:
            processed = process_data(data)
            embeddings = np.array([entry['embedding'] for entry in processed])
            metadata = [{"title": entry['title'], "description": entry['description']} for entry in processed]
            if vector_db is None:
                vector_db = VectorDB()
            vector_db.add(embeddings, metadata)
            print("Data Collector: Added", len(processed), "entries to the vector DB.")
        else:
            print("Data Collector: No data fetched.")
        time.sleep(interval)

def advisory_agent(query):
    """
    Retrieves relevant documents from the vector database and generates a healthcare advisory.
    """
    global vector_db
    if vector_db is None:
        print("Advisory Agent: No data available yet. Please wait for data collection.")
        return "No data available yet. Please try again later."
    query_embedding = model.encode([query])
    retrieved_docs = vector_db.search(query_embedding, top_k=5)
    from advisory import generate_advisory  # Delayed import to avoid circular dependencies
    advisory_text = generate_advisory(query, retrieved_docs)
    return advisory_text

def start_agents():
    """
    Starts the data collector agent in a background thread.
    """
    collector_thread = threading.Thread(target=data_collector_agent, daemon=True)
    collector_thread.start()
