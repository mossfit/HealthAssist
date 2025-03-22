# HealthAssist - AI-Powered Healthcare Assistant :scientist:	

**HealthAssist** is an advanced healthcare assistant designed to assist doctors and patients by retrieving and synthesizing medical data from multiple sources—such as PubMed research articles, patient records, and drug databases. Leveraging Pinecone for vector storage and a LangChain-based RAG pipeline with GPT‑4, HealthAssist delivers accurate, up-to-date medical advisories.

## Features

- **Real-Time Medical Data Retrieval:**
  - **PubMed Integration:** Retrieve recent research articles.
  - **Patient Records:** Access sample patient records.
  - **Drug Database:** Query drug information.
- **Advanced RAG Pipeline:**
  - Combines Pinecone vector search with GPT‑4 to provide comprehensive medical advisories.
- **User-Friendly Interface:**
  - A modern, responsive dashboard built with Flask and Bootstrap.
- **LangChain Integration:**
  - Enables efficient retrieval and synthesis of medical knowledge.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd health_assistant

2. **Install Dependencies:**

```bash
  pip install -r requirements.txt
```
3. **Configuration:**

   - Update the API keys in config.py for Pinecone and OpenAI.

   - Create dummy data files dummy_patient_records.json and dummy_drug_database.json in the project root with sample data.

4. **Run the Application:**

```bash
  python main.py
```

Open your browser and navigate to http://127.0.0.1:5000.

Usage
Medical Advisory:
 - Enter your query (e.g., "latest treatments for diabetes") into the input field to receive a detailed, context-rich advisory.

Dashboard:

 - View recent data entries from PubMed, patient records, and drug databases on the live dashboard.
