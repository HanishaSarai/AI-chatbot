from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts =[
    "Hello My name is hansiha",
    "What is generative AI?",
    "What is the capital of France?"
]

vectors = embeddings.embed_documents(texts)
print(vectors)