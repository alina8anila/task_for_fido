# task_for_fido_2

pip3 install weaviate-client;
pip3 install fastapi
pip3 install uvicorn
pip3 install python-dotenv
source .venv/bin/activate 

uvicorn task2:app --reload --port 8003

must be ".ebv" file with:
WEAVIATE_URL=
WEAVIATE_API_KEY=
OHERE_APIKEY=

git add README.md
