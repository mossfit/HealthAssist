import pinecone
import numpy as np
from config import PINECONE_API_KEY, PINECONE_ENV, PINECONE_INDEX_NAME, VECTOR_DIMENSION

# Initialize Pinecone
pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)

def create_index_if_not_exists():
    if PINECONE_INDEX_NAME not in pinecone.list_indexes():
        pinecone.create_index(PINECONE_INDEX_NAME, dimension=VECTOR_DIMENSION)
create_index_if_not_exists()

class VectorDB:
    def __init__(self):
        self.index = pinecone.Index(PINECONE_INDEX_NAME)
        # Local metadata storage for demonstration purposes
        self.metadata = []

    def add(self, embeddings, metadata):
        """
        embeddings: numpy array (n_samples, VECTOR_DIMENSION)
        metadata: list of dicts (e.g., title and description)
        """
        ids = [str(i + len(self.metadata)) for i in range(len(metadata))]
        self.metadata.extend(metadata)
        vectors = [(id_, emb.tolist(), meta) for id_, emb, meta in zip(ids, embeddings, metadata)]
        self.index.upsert(vectors=vectors)

    def search(self, query_embedding, top_k=5):
        query_embedding = query_embedding.tolist()
        results = self.index.query(vector=query_embedding, top_k=top_k, include_metadata=True)
        output = []
        for match in results['matches']:
            meta = match.get("metadata", {})
            meta['score'] = match.get("score", None)
            output.append(meta)
        return output

if __name__ == "__main__":
    import numpy as np
    dummy_embeddings = np.random.rand(2, VECTOR_DIMENSION).astype(np.float32)
    metadata = [
        {"title": "Dummy 1", "description": "Dummy description 1"},
        {"title": "Dummy 2", "description": "Dummy description 2"}
    ]
    db = VectorDB()
    db.add(dummy_embeddings, metadata)
    query_embedding = dummy_embeddings[0]
    results = db.search(query_embedding, top_k=2)
    print(results)
