from pydantic import BaseModel, Field
from typing import Optional


class AlertBase(BaseModel):
    title: str
    description: str
    severity: str = "MEDIUM"
    source_ip: Optional[str] = None
    destination_ip: Optional[str] = None
    username: Optional[str] = None
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)


class AlertCreate(AlertBase):
    pass


class AlertRead(AlertBase):
    id: int
    risk_score: int = 0
    status: str = "NEW"
