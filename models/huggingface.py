import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpointEmbeddings

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="BAAI/bge-small-en-v1.5",
    huggingfacehub_api_token=os.getenv("HF_TOKEN")
)

# 1. Generate the embedding for a sentence
text = "Vector embeddings are just lists of numbers."
vector = embeddings.embed_query(text)

# 2. Inspect the "complex" part
print(f"--- VECTOR INFO ---")
print(f"Type: {type(vector)}")
print(f"Length (Dimensions): {len(vector)}") # Should be 384
print(f"First 10 numbers: {vector[:10]}")    # The actual numerical representation
print(f"-------------------\n")

# 3. Compare two similar sentences to see how the numbers relate
vec1 = embeddings.embed_query("I love coding in Python.")
vec2 = embeddings.embed_query("I enjoy programming with Python.")

# Even though the words change, the numbers will be mathematically "close"
print(f"First 5 of Vec1: {vec1[:5]}")
print(f"First 5 of Vec2: {vec2[:5]}")
