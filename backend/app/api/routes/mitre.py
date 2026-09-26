from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Incident

router = APIRouter(prefix="/incidents", tags=["incidents"])


@router.get("")
def list_incidents(db: Session = Depends(get_db)):
    incidents = db.query(Incident).all()
    return [{
        "id": incident.id,
        "incident_number": incident.incident_number,
        "title": incident.title,
        "severity": incident.severity,
        "status": incident.status,
    } for incident in incidents]


@router.post("")
def create_incident(payload: dict, db: Session = Depends(get_db)):
    incident = Incident(
        incident_number=f"INC-{db.query(Incident).count() + 1:04d}",
        title=payload.get("title", "Synthetic investigation"),
        description=payload.get("description", "No description provided"),
        severity=payload.get("severity", "MEDIUM"),
        status="NEW",
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return {"message": "Incident created", "id": incident.id, "incident_number": incident.incident_number}


@router.get("/{incident_id}")
def get_incident(incident_id: int, db: Session = Depends(get_db)):
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return {
        "id": incident.id,
        "incident_number": incident.incident_number,
        "title": incident.title,
        "description": incident.description,
        "severity": incident.severity,
        "status": incident.status,
    }


@router.patch("/{incident_id}")
def update_incident(incident_id: int, payload: dict, db: Session = Depends(get_db)):
    incident = db.query(Incident).filter(Incident.id == incident_id).first()
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    for key, value in payload.items():
        if hasattr(incident, key):
            setattr(incident, key, value)
    db.commit()
    return {"message": "Incident updated", "id": incident.id}


@router.post("/{incident_id}/notes")
def add_note(incident_id: int, payload: dict):
    return {"message": f"Note added to incident {incident_id}", "note": payload.get("note", "")}


@router.post("/{incident_id}/actions")
def add_action(incident_id: int, payload: dict):
    return {"message": f"Action logged for incident {incident_id}", "action": payload.get("action", "")}


@router.post("/{incident_id}/close")
def close_incident(incident_id: int):
    return {"message": f"Incident {incident_id} closed", "status": "CLOSED"}
