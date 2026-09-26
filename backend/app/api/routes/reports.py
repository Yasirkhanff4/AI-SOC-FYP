from fastapi import APIRouter

from app.services.ai_analysis import analyze_alert, investigate_alert

router = APIRouter(prefix="/ai", tags=["ai"])


@router.post("/analyze-alert")
def analyze_alert_endpoint(payload: dict):
    return analyze_alert(payload)


@router.post("/investigate")
def investigate_endpoint(payload: dict):
    return investigate_alert(payload)


@router.post("/explain")
def explain_endpoint(payload: dict):
    return {"summary": "This event was flagged due to repeated failed authentication and anomalous access patterns.", "confidence": 0.82}


@router.post("/recommend-response")
def response_endpoint(payload: dict):
    return {
        "recommended_actions": [
            "Validate affected user account",
            "Check source IP reputation",
            "Review authentication logs",
            "Consider temporary restriction based on organizational policy",
        ]
    }
