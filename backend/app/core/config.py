from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI-SOC",
    version="0.1.0",
    description="AI-powered Security Operations Center for final-year cybersecurity project",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "ai-soc-backend"}

@app.get("/")
def root():
    return {
        "project": "AI-SOC",
        "status": "initialized",
        "message": "SOC backend started successfully"
    }
