from pydantic import BaseModel, Field
from typing import Optional


class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: str = "MEDIUM"
    category: str = "AUTHENTICATION"
    assigned_to: Optional[str] = None


class IncidentRead(IncidentCreate):
    id: int
    status: str = "NEW"
    incident_number: str = "INC-0001"
