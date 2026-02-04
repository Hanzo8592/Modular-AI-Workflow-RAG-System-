
from orchestrator.classify import classify_prompt
from orchestrator.planner import generate_subquestions, clean_subquestions
from rag.retrieval import multi_retrieve
from synthesizer import synthesize_answer

def main():
    print("Enter 'exit' to quit.")
    print("AI system ready. Ask questions.")

    while True:
        query = input("\nYou: ")
        if query.lower() == "exit":
            print("Exiting...")
            break

        orchestration = classify_prompt(query)
        print("\nOrchestrator Output:", orchestration)

        if orchestration.get("needs_retrieval"):
            subqs = generate_subquestions(query)
            subqs = clean_subquestions(subqs)
            evidence = multi_retrieve(subqs)
            answer = synthesize_answer(query, evidence)
        else:
            answer = "Reasoning mode active. No retrieval needed."

        print("\nAI:", answer)

if __name__ == "__main__":
    main()
