
from fastapi import FastAPI
from pydantic import BaseModel
from .services import gemini_service
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query(request: QueryRequest):
    response = await gemini_service.get_gemini_response(request.query)
    return {"response": response}
