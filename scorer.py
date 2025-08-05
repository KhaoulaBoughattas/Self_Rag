# scorer.py

from generator import generate_response

def score_candidates(question: str, candidates: list) -> dict:
    """
    Score chaque réponse candidate et retourne la meilleure.
    candidates: list de dict avec clé 'answer'
    """
    best_score = -1
    best_candidate = None

    for cand in candidates:
        prompt = f"""Question : {question}
Réponse : {cand['answer']}
Donne une note sur 10 pour cette réponse selon sa pertinence.
Note :"""

        score_text = generate_response(prompt, [])
        # Extraire un chiffre (note) de la réponse
        digits = "".join(filter(str.isdigit, score_text))
        score = int(digits[:2]) if digits else 0

        if score > best_score:
            best_score = score
            best_candidate = cand

    return best_candidate
