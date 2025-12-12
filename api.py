from fastapi import FastAPI
from backend.rag import rag_agent
from backend.data_models import Prompt

app = FastAPI() 

@app.get("/")
async def hello_message():
    return {"test": "hello there yo"}

@app.post("/rag/query")
async def query_documentation(query: Prompt):
    result = await rag_agent.run(query.prompt)

    return result.output