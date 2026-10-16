from fastapi import FastAPI
from pydantic import BaseModel
from pservice import chat_service

app=FastAPI()

class Chatrequest(BaseModel):
    session_id:str
    message:str
    
@app.post("/chat")
def chat(data:Chatrequest):
    answer=chat_service(data.session_id,data.message)
    return {"answer":answer}

