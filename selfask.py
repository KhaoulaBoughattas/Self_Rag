# selfask.py

from generator import generate_response

def self_ask(question: str, previous_answer: str = "") -> str:
    """
    Reformule la question pour la rendre plus précise,
    en tenant compte de la réponse précédente.
    """
    if not previous_answer:
        # Première formulation simple
        return question.strip()

    prompt = f"""
    Reformule la question suivante pour qu'elle soit plus claire et mieux ciblée en tenant compte de la réponse précédente :

    Question originale : {question}
    Réponse précédente : {previous_answer}

    Nouvelle question :
    """

    reformulated = generate_response(prompt, [])
    return reformulated.strip()
