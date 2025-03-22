import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_advisory(query, retrieved_docs):
    """
    Generates a detailed healthcare advisory based on the query and retrieved documents.
    """
    context = "\n\n".join(
        [f"Title: {doc.get('title', 'N/A')}\nDescription: {doc.get('description', '')}" for doc in retrieved_docs]
    )
    prompt = (
        f"You are a medical expert assistant. Based on the following information:\n\n"
        f"{context}\n\n"
        f"Provide a detailed and informative answer for the query: '{query}'. "
        "Include any relevant medical advice and reference recent research findings where applicable. "
        "Ensure the response is clear and helpful for healthcare professionals and patients alike."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and knowledgeable healthcare assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message['content']

if __name__ == "__main__":
    sample_docs = [
        {"title": "Study on Diabetes", "description": "Recent findings on the effectiveness of new diabetes treatments."},
        {"title": "Patient Case Study", "description": "A patient with type 2 diabetes showed improvement after medication."}
    ]
    query = "What are the latest treatments for type 2 diabetes?"
    advisory = generate_advisory(query, sample_docs)
    print(advisory)
