# Azure AI Resume ↔ Job Match (POC)

A production-lean **proof of concept** showing how to:
- Parse resumes and job descriptions
- Create embeddings and store vectors in **Azure Cognitive Search**
- Retrieve top matches and generate **explainable fit** using **Azure OpenAI**
- Display results in a minimal **Streamlit** UI

> This repo is intentionally lightweight so you can extend quickly.

## ⚙️ Architecture (POC)
```
[Streamlit UI] -> [Azure Storage: resumes/jobs]
    -> [AI Document Intelligence] -> parsed JSON
    -> [AI Language] (optional) -> job skills/phrases
    -> [Azure OpenAI Embeddings] -> vectors
    -> [Azure Cognitive Search] (vector index)
    -> [Azure OpenAI GPT] (fit summary + reasons)
```

## 📦 Project Structure
```
azure-ai-resume-match/
├─ app/
│  └─ streamlit_app.py
├─ src/
│  ├─ azure_clients.py
│  ├─ ingest_resume.py
│  ├─ ingest_job.py
│  ├─ search_match.py
│  └─ prompts.py
├─ infra/
│  └─ main.bicep
├─ data/
│  └─ sample/
│     ├─ job_sample.txt
│     └─ resume_sample.txt
├─ .gitignore
├─ LICENSE
├─ requirements.txt
└─ README.md
```

## 🔐 Environment Variables
Create a `.env` in the project root (or export these in your environment):
```
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_KEY=...
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-large
AZURE_OPENAI_CHAT_DEPLOYMENT=gpt-4o

AZURE_SEARCH_ENDPOINT=...
AZURE_SEARCH_KEY=...
AZURE_SEARCH_INDEX=talent-match-index

AZURE_STORAGE_CONNECTION_STRING=...
AZURE_DOC_INTELLIGENCE_ENDPOINT=...
AZURE_DOC_INTELLIGENCE_KEY=...
```

## 🚀 Quickstart (Local)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# run the demo UI
streamlit run app/streamlit_app.py
```

## 🧱 Deploy Infra (optional)
Use the bicep in `infra/main.bicep` as a starting point to provision Search, Storage, and OpenAI resources.

## 🧪 Demo Flow
1. Drop a job description (TXT) and a few resumes (PDF/DOCX) into the app.
2. The app embeds the job, queries the vector index for top-K resumes.
3. It blends vector score + skill overlap + experience alignment.
4. It calls GPT once per candidate to produce an **explainable JSON** (strengths, gaps, summary).
5. Results render as cards you can export or copy.

## 📝 Notes
- This is a POC: add proper Key Vault, VNET, RBAC, and PII handling for prod.
- Replace sample code with your actual parsing/ingestion to Azure services.
