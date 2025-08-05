# test_retriever.py

from retriever import retrieve_documents

if __name__ == "__main__":
    question = "Comment gérer une attaque de panique ?"
    docs = retrieve_documents(question, k=3)
    for i, doc in enumerate(docs, 1):
        print(f"\n--- Document {i} ---\n{doc.page_content}\n")
