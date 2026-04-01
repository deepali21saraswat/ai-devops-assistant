from fastapi import FastAPI
from pydantic import BaseModel
from app.ai_client import analyze_log

app = FastAPI()

class LogRequest(BaseModel):
    log: str

@app.get("/")
def home():
    return {"message": "AI DevOps Assistant running-AI Explorer"}

@app.post("/analyze")
def analyze(request: LogRequest):
    result = analyze_log(request.log)
    return {"analysis": result}
