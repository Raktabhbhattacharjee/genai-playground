from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("AI_Introduction.pdf")
documents = loader.load()

print(f"Number of Documents: {len(documents)}")  # one per page
print(documents[0].page_content)
print(documents[0].metadata)  # includes 'page' number + 'source'