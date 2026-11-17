import os

from config import settings
import pipeline

def healthcheck():
    if not os.path.exists(settings.DOCS_DIR):
        raise Exception("Document directory not found")   

def main():
    healthcheck()
    doc_collection = pipeline.initialise_docs_collection()
    
    while True:
        print("Hi! I'm here to tell you about your fun memories. Enter \n(1) Exit to end chat \n(2) /reinitilise to restart loading of documents \n(3) Type Your question")
        user_input = input("Go on ask a memory:").strip().lower()
        
        if user_input in {"end", "exit","stop", "1"} :
            print("Ok! Sayonara!")
            break
        
        if user_input in {"/reinitialise", "2"}:
            doc_collection = pipeline.initialise_docs_collection(True)
            continue
        
        result = pipeline.query(doc_collection, user_input)
        response = result["response"]
        reference = result["doc_file"]
        print(response, reference)

if __name__ == "__main__":
    main()