# retriever.py

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Paramètres
DATA_PATH = "data/texte_nettoye.txt"  # ✅ Change ici si tu veux utiliser un autre fichier
INDEX_PATH = "vectorstore"
MODEL_NAME = "intfloat/multilingual-e5-base"

# Préparer le modèle d'embedding
embedding_model = HuggingFaceEmbeddings(model_name=MODEL_NAME)

# Vérifie si l'index FAISS existe déjà
if not os.path.exists(INDEX_PATH):
    print("Index FAISS non trouvé, création en cours...")

    # Charger les documents texte
    loader = TextLoader(DATA_PATH, encoding="utf-8")
    docs = loader.load()

    # Diviser le texte en morceaux
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    # Créer et sauvegarder l'index FAISS
    db = FAISS.from_documents(chunks, embedding_model)
    db.save_local(INDEX_PATH)
    print("Index FAISS créé et sauvegardé.")
else:
    print("Index FAISS trouvé, chargement...")
    db = FAISS.load_local(INDEX_PATH, embedding_model, allow_dangerous_deserialization=True)

# Fonction pour récupérer les documents les plus pertinents
def retrieve_documents(query: str, k: int = 5):
    results = db.similarity_search(query, k=k)
    return results
