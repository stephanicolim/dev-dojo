import ollama
import chromadb
from config import settings
import os

def get_embedding(text: str) -> list[float]:
    response = ollama.embed(model=settings.EMBED_MODEL, input=text)
    return response["embeddings"][0]

def initialise_docs_collection(reinitialise: bool=False) -> chromadb.types.Collection:
    client = chromadb.PersistentClient(path=settings.CHROMA_PATH)
    collection = client.get_or_create_collection(name=settings.DOCS_CATEGORY_NAME)
    if reinitialise and settings.DOCS_CATEGORY_NAME in client.list_collections():
        client.delete_collection(name=settings.DOCS_CATEGORY_NAME)
    
    if collection.count() == 0:
        print("Index documents into collection")
        for filename in sorted(os.listdir(settings.DOCS_DIR)):
            filepath = os.path.join(settings.DOCS_DIR, filename)
            if ".txt" in filename:
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                
                if content:
                    embedding = get_embedding(content)
                    collection.add(
                        ids=[filename],
                        embeddings=[embedding],
                        documents=[content]
                    )
    print(f"Indexed docs {collection.count()} for {collection}")
    return collection

def query(collection: chromadb.api.models.Collection, question: str) -> dict:
    question_embedding = get_embedding(question)
    result = collection.query(query_embeddings=[question_embedding], n_results=1)
    
    prompt = f"""
    Answer the question based on the given context. 
    If answer is not in context then reply with "I could not find any input regarding that"
    # Context:
    {" ".join(result["documents"][0])}
    # Question: 
    {question}
    """
    
    response = ollama.chat(
        model=settings.CHAT_MODEL, 
        messages=[{"role":"user", "content": prompt}]
    )
    
    return {"response": response.message.content,
            "doc_file": result["ids"][0]
    }
    
    
    