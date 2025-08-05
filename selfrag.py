# selfrag.py

from retriever import retrieve_documents
from selfask import self_ask
from generator import generate_response
from scorer import score_candidates

def self_rag_pipeline(question: str, max_turns: int = 3, top_k: int = 5):
    """
    Pipeline Self-RAG avec reformulation iterative de la question,
    récupération des documents, génération des réponses, et scoring.

    max_turns : nombre max d'itérations self-ask pour reformuler
    top_k : nombre de documents à récupérer
    """

    current_question = question
    previous_answer = ""
    final_answer = None

    for turn in range(max_turns):
        print(f"--- Tour {turn + 1} ---")
        # Reformulation
        refined_question = self_ask(current_question, previous_answer)
        print(f"Question reformulée : {refined_question}")

        # Retrieval
        docs = retrieve_documents(refined_question, k=top_k)

        # Génération de réponses candidates
        candidates = []
        for doc in docs:
            answer_text = generate_response(refined_question, [doc.page_content])
            candidates.append({"answer": answer_text, "source": doc.metadata.get("source", "inconnu")})

        # Scoring des réponses
        best = score_candidates(refined_question, candidates)
        print(f"Meilleure réponse au tour {turn + 1} : {best['answer'][:200]}...")

        # Met à jour la réponse précédente pour la prochaine reformulation
        previous_answer = best['answer']
        current_question = refined_question
        final_answer = best['answer']

    return final_answer
