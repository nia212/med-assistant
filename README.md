#  MedChat - AI RAG Medical Personal Assistant

An intelligent, AI-powered medical assistant designed to provide fast and reliable answers to your health-related questions. Built on a **Retrieval-Augmented Generation (RAG)** architecture, it combines the power of **Large Language Models (LLMs)**, **LangChain**, and **Pinecone vector database** to deliver accurate responses grounded in trusted medical knowledge.

> Whether you're looking to understand a diagnosis, explore treatment options, or simply learn more about your health — **MedChat** is your 24/7 personal medical companion.

---

https://github.com/user-attachments/assets/e482354f-f1ef-4438-a0cd-2b2c810e56e8

##  Features

- Real-time chat with AI medical assistant
- LLM-powered responses using GPT
- Vector search with Pinecone
- LangChain for intelligent retrieval chain

---

## Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Backend      | Python, Flask          |
| LLM          | OpenAI GPT             |
| AI Framework | LangChain              |
| Vector Db    | Pinecone               |
| Frontend     | HTML, CSS, Bootstrap 5 |
| Animation    | Lottie, CSS Keyframes  |
| AJAX         | jQuery 3.6             |

---

## Installation

**STEP 1 - Clone the repository**
```bash
https://github.com/nia212/med-assistant.git
cd med-assistant
```

**STEP 2 - Create a conda environment**
```bash
conda create -n medbot python=3.10 -y
conda activate medbot
```

**STEP 3 - Install the requirements**
```bash
pip install -r requirements.txt
```

**STEP 4 - Create a `.env` file in the root directory**
```env
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

**STEP 5 - Store embeddings to Pinecone**
```bash
python store_index.py
```

**STEP 6 - Run the app**
```bash
python app.py
```

**STEP 7 - Open browser**


---

## 💬 Usage

- Type a medical question in the chat input
- Or click a **Common question** from the sidebar
- Bot will respond using GPT + Pinecone vector search

---

> ⚠️ **Disclaimer:** MedChat is for **informational purposes only** and is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider.
