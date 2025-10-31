
from app.llm_chain import RAGChain

def main():
    print("\n" + "─" * 80)
    print("  RAG System - Question Answering with Elasticsearch")
    print("─" * 80 + "\n")
    print("Initializing RAG chain...")
    try:
        rag_chain = RAGChain()
        print("✓ Ready\n")
    except Exception as e:
        print(f"✗ Failed to initialize: {e}\n")
        return
    
    print("Type 'exit' or 'quit' to end the session.\n")

    while True:

        question = input("Question: ").strip()
        
        if question.lower() in ["exit", "quit"]:
            print("\n" + "─" * 80)
            print("  Session ended")
            print("─" * 80 + "\n")
            break
            
        if not question:
            print("Please enter a valid question.\n")
            continue
        
        print()
        
        try:
            response = rag_chain.query(question)
            
    
            print("─" * 80)
            try:
                answer = response['response']
                print(f"{answer}")
            except (KeyError, TypeError):
                print(f"{response}")
            print("─" * 80 + "\n")
            
        except Exception as e:
            print("─" * 80)
            print(f"Error: {str(e)}")
            print("─" * 80 + "\n")

if __name__ == "__main__":
    main()