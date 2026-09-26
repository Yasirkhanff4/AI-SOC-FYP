from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Event

router = APIRouter(prefix="/events", tags=["events"])


@router.get("")
def list_events(db: Session = Depends(get_db)):
    events = db.query(Event).all()
    return [{
        "id": event.id,
        "timestamp": event.timestamp.isoformat() if event.timestamp else None,
        "source": event.source,
        "event_type": event.event_type,
        "host_id": event.host_id,
    } for event in events]


@router.get("/{event_id}")
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return {
        "id": event.id,
        "timestamp": event.timestamp.isoformat() if event.timestamp else None,
        "source": event.source,
        "event_type": event.event_type,
        "raw_log": event.raw_log,
        "normalized_data": event.normalized_data,
    }


@router.post("")
def create_event(payload: dict, db: Session = Depends(get_db)):
    event = Event(
        timestamp=payload.get("timestamp"),
        source=payload.get("source", "synthetic"),
        host_id=payload.get("host_id"),
        event_type=payload.get("event_type", "authentication_failure"),
        raw_log=payload.get("raw_log", "synthetic log"),
        normalized_data=payload.get("normalized_data", {}),
    )
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"message": "Event created", "id": event.id}
