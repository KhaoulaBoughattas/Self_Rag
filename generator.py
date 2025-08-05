import subprocess
from langchain.prompts import PromptTemplate

GENERATION_PROMPT = PromptTemplate.from_template(
    """
    Vous êtes un assistant IA expert. Utilisez le contexte suivant pour répondre à la question de façon précise et complète.
    Contexte :
    {context}

    Question : {question}

    Réponse :
    """
)

def generate_response(question: str, documents: list, model='gemma3:1b'):
    context = "\n".join(documents)
    prompt = GENERATION_PROMPT.format(context=context, question=question)

    try:
        result = subprocess.run(
            ['ollama', 'run', model],
            input=prompt,
            text=True,
            capture_output=True,
            encoding='utf-8',
            timeout=60
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            # Enlever le prompt au début si l'output contient le prompt complet
            if output.startswith(prompt):
                output = output[len(prompt):].strip()
            return output
        else:
            return f"Erreur lors de la génération : {result.stderr.strip()}"
    except Exception as e:
        return f"Exception lors de la génération : {e}"

def reformulate_query(original_question: str, previous_answer: str, model='gemma3:1b'):
    prompt = f"""
Reformule la question suivante pour qu'elle soit plus claire et mieux ciblée en tenant compte de la réponse précédente :

Question originale : {original_question}
Réponse précédente : {previous_answer}

Nouvelle question :
"""
    try:
        result = subprocess.run(
            ['ollama', 'run', model],
            input=prompt,
            text=True,
            capture_output=True,
            encoding='utf-8',
            timeout=30
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            if output.startswith(prompt):
                output = output[len(prompt):].strip()
            return output
        else:
            return f"Erreur lors de la reformulation : {result.stderr.strip()}"
    except Exception as e:
        return f"Exception lors de la reformulation : {e}"
