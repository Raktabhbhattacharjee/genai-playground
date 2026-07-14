from langchain_community.document_loaders import TextLoader

loader = TextLoader("AI_Introduction.txt")
documents = loader.load()

print(f"Type of Documents: {type(documents)}")
print(f"Type of Document in Documents: {type(documents[0])}")
print(f"Number of Documents: {len(documents)}")

print(f"Actual Data:\n{documents[0].page_content}\n")
print(f"Meta Data:\n{documents[0].metadata}\n")