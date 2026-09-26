from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.ai import router as ai_router
from app.api.routes.alerts import router as alerts_router
from app.api.routes.auth import router as auth_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.events import router as events_router
from app.api.routes.incidents import router as incidents_router
from app.api.routes.mitre import router as mitre_router
from app.api.routes.reports import router as reports_router
from app.api.routes.threat_intel import router as threat_intel_router
from app.database import create_db_and_tables, ensure_default_admin

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


@app.on_event("startup")
def startup_event():
    create_db_and_tables()
    ensure_default_admin()


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "ai-soc-backend"}


@app.get("/")
def root():
    return {
        "project": "AI-SOC",
        "status": "initialized",
        "message": "SOC backend started successfully",
    }


app.include_router(auth_router, prefix="/api")
app.include_router(dashboard_router, prefix="/api")
app.include_router(events_router, prefix="/api")
app.include_router(alerts_router, prefix="/api")
app.include_router(incidents_router, prefix="/api")
app.include_router(mitre_router, prefix="/api")
app.include_router(threat_intel_router, prefix="/api")
app.include_router(ai_router, prefix="/api")
app.include_router(reports_router, prefix="/api")
