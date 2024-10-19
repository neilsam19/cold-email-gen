import chromadb

client = chromadb.Client()

collection = client.create_collection(name="my_collection")


collection.add(
    documents=[
        "This is a document about New York",
        "This is a document about Delhi"
    ],
    ids=["id1", "id2"],
    metadatas = [
        {"url": "https://en.wikipedia.org/wiki/New_York_City"},
        {"url":"https://en.wikipedia.org/wiki/New_Delhi"}
    ]
)


results = collection.query(
    query_texts=["This is a document about Pennsylvania Station"], # Chroma will embed this for you
    n_results=2 # how many results to return
)
print(results)

#results are:
'''
{'ids': [['id1', 'id2']], 
 'embeddings': None, 
 'documents': 
 [['This is a document about pineapple', 'This is a document about oranges']], 
 'uris': None, 
 'data': None, 
 'metadatas': [[None, None]], 
 'distances': [[1.0404009819030762, 1.2430799007415771]], 
 'included': [<IncludeEnum.distances: 'distances'>, <IncludeEnum.documents: 'documents'>, <IncludeEnum.metadatas: 'metadatas'>]}
'''

