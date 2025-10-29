import weaviate
import os
from weaviate.util import generate_uuid5
from weaviate.classes.config import Configure, Property, DataType
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status 

load_dotenv()

headers = {"X-Cohere-Api-Key": os.getenv("COHERE_APIKEY")}
client = weaviate.connect_to_weaviate_cloud(
    cluster_url=os.getenv("WEAVIATE_URL"),
    auth_credentials=os.getenv("WEAVIATE_API_KEY"),
    headers=headers
)

client.collections.delete("Notes") #not sure
client.collections.create(
    name="Notes",
    properties=[Property(name="text", data_type=DataType.TEXT)],
    vector_config=Configure.Vectors.text2vec_cohere(model="embed-v4.0"), # Define the vectorizer module
    generative_config=Configure.Generative.cohere(model="command-a-03-2025") # Define the generative module
)

notes = client.collections.use("Notes")
app = FastAPI()

@app.post("/notes") 
async def new_note(note : str):
    with notes.batch.fixed_size(batch_size=200) as batch:
        new={ "text": note}
        id=generate_uuid5(note)
        batch.add_object(properties=new, uuid=id)
    return {"ID": id, "text" : note}

@app.get("/notes/{id}")
async def get_id(id: str):
    ans = notes.query.fetch_object_by_id(uuid=id)
    if ans is None or ans.properties is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return {"id": id, "note": ans.properties}

@app.get("/search")
async def get_near(q : str):
    ans=notes.query.near_text(query=q, limit=3)
    res=[]
    for i in ans.objects: res.append(i.properties)
    return {f"near {q}": res}

print(client.is_ready()) # just have to cout True
#client.close() 