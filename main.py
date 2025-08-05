# main.py

from selfrag import self_rag_pipeline

def main():
    print("Bienvenue dans le système Self-RAG 🤖📚")
    print("Posez une question en lien avec les documents disponibles.")
    print("Tapez 'exit' pour quitter.\n")

    while True:
        user_question = input("❓ Votre question : ")
        if user_question.lower() in ["exit", "quit", "q"]:
            print(" Au revoir !")
            break

        print("\n Traitement en cours...\n")
        final_answer = self_rag_pipeline(user_question)

        print("\n Réponse finale :\n")
        print(final_answer)
        print("\n" + "=" * 60 + "\n")

if __name__ == "__main__":
    main() 