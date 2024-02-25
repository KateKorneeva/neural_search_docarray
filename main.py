from docarray import Document, DocumentArray
doc = Document(uri="https://www.gutenberg.org/files/1342/1342-0.txt").load_uri_to_text()

# break large text into smaller chunks
docs = DocumentArray(Document(text = s.strip()) for s in doc.text.split('\n') if s.strip())

# apply feature hashing to embed the DocumentArray
docs.apply(lambda doc: doc.embed_feature_hashing())

# query sentence 
query = (Document(text="chronological order names").embed_feature_hashing().match(docs, limit=5, exclude_self=True, 
metric="jaccard", use_scipy=True))

# print the results
print(query.matches[:, ('text', 'scores__jaccard')])