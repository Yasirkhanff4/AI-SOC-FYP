from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Alert
from app.services.ai_analysis import analyze_alert
from app.services.detection_engine import generate_alert

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("")
def list_alerts(db: Session = Depends(get_db)):
    alerts = db.query(Alert).all()
    return [{
        "id": alert.id,
        "title": alert.title,
        "severity": alert.severity,
        "status": alert.status,
        "risk_score": alert.risk_score,
        "source_ip": alert.source_ip,
    } for alert in alerts]


@router.get("/{alert_id}")
def get_alert(alert_id: int, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return {
        "id": alert.id,
        "title": alert.title,
        "description": alert.description,
        "severity": alert.severity,
        "status": alert.status,
        "risk_score": alert.risk_score,
        "source_ip": alert.source_ip,
        "destination_ip": alert.destination_ip,
        "username": alert.username,
    }


@router.post("")
def create_alert(payload: dict, db: Session = Depends(get_db)):
    generated = generate_alert(payload)
    alert = Alert(**generated)
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return {"message": "Alert created", "id": alert.id, "alert": generated}


@router.patch("/{alert_id}")
def update_alert(alert_id: int, payload: dict, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    for key, value in payload.items():
        if hasattr(alert, key):
            setattr(alert, key, value)
    db.commit()
    return {"message": "Alert updated", "id": alert.id}


@router.post("/{alert_id}/analyze")
def analyze_alert_endpoint(alert_id: int, db: Session = Depends(get_db)):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    result = analyze_alert({
        "alert_id": alert.id,
        "event_type": "authentication_failure",
        "source_ip": alert.source_ip,
        "username": alert.username,
        "host": "LAB-PC-01",
        "detection_rule": "BRUTE_FORCE_001",
    })
    return result


@router.post("/{alert_id}/enrich")
def enrich_alert(alert_id: int):
    return {"message": f"Threat intelligence enrichment requested for alert {alert_id}"}
