
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

from .services import gemini_service




app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.post("/query")
async def query(request: QueryRequest):
    response = await gemini_service.get_gemini_response(request.query)
    return {"response": response}
