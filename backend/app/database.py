from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(120), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(30), default="SOC_ANALYST", nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    incidents = relationship("Incident", back_populates="assigned_user")
    notes = relationship("IncidentNote", back_populates="user")
    audit_logs = relationship("AuditLog", back_populates="user")


class Host(Base):
    __tablename__ = "hosts"

    id = Column(Integer, primary_key=True, index=True)
    hostname = Column(String(100), nullable=False)
    ip_address = Column(String(45), nullable=False)
    operating_system = Column(String(50), nullable=True)
    agent_id = Column(String(100), nullable=True)
    status = Column(String(30), default="ACTIVE")
    last_seen = Column(DateTime, nullable=True)

    events = relationship("Event", back_populates="host")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    source = Column(String(100), nullable=False)
    host_id = Column(Integer, ForeignKey("hosts.id"), nullable=True)
    event_type = Column(String(100), nullable=False)
    raw_log = Column(Text, nullable=True)
    normalized_data = Column(JSON, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    host = relationship("Host", back_populates="events")
    alerts = relationship("Alert", back_populates="event")


class DetectionRule(Base):
    __tablename__ = "detection_rules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    rule_type = Column(String(50), nullable=False)
    severity = Column(String(20), default="MEDIUM")
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    alerts = relationship("Alert", back_populates="detection_rule")


class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=True)
    rule_id = Column(Integer, ForeignKey("detection_rules.id"), nullable=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    severity = Column(String(20), default="MEDIUM")
    risk_score = Column(Integer, default=0)
    status = Column(String(30), default="NEW")
    source_ip = Column(String(45), nullable=True)
    destination_ip = Column(String(45), nullable=True)
    username = Column(String(100), nullable=True)
    confidence = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    event = relationship("Event", back_populates="alerts")
    detection_rule = relationship("DetectionRule", back_populates="alerts")
    iocs = relationship("IOC", back_populates="alert")
    threat_intel = relationship("ThreatIntel", back_populates="alert")
    mitre_mappings = relationship("MITREMapping", back_populates="alert")
    ai_analyses = relationship("AIAnalysis", back_populates="alert")
    incident_links = relationship("IncidentAlert", back_populates="alert")


class IOC(Base):
    __tablename__ = "iocs"

    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer, ForeignKey("alerts.id"), nullable=False)
    type = Column(String(50), nullable=False)
    value = Column(String(255), nullable=False)
    reputation = Column(String(50), default="UNKNOWN")
    confidence = Column(Integer, default=0)
    source = Column(String(50), default="LOCAL")

    alert = relationship("Alert", back_populates="iocs")
    intel = relationship("ThreatIntel", back_populates="ioc")


class ThreatIntel(Base):
    __tablename__ = "threat_intelligence"

    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer, ForeignKey("alerts.id"), nullable=True)
    ioc_id = Column(Integer, ForeignKey("iocs.id"), nullable=True)
    provider = Column(String(50), nullable=False)
    reputation = Column(String(50), default="UNKNOWN")
    score = Column(Integer, default=0)
    raw_response = Column(Text, nullable=True)
    checked_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    alert = relationship("Alert", back_populates="threat_intel")
    ioc = relationship("IOC", back_populates="intel")


class MITREMapping(Base):
    __tablename__ = "mitre_mappings"

    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer, ForeignKey("alerts.id"), nullable=False)
    tactic = Column(String(100), nullable=False)
    technique_id = Column(String(50), nullable=False)
    technique_name = Column(String(150), nullable=False)
    confidence = Column(Integer, default=0)
    evidence = Column(Text, nullable=True)

    alert = relationship("Alert", back_populates="mitre_mappings")


class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    incident_number = Column(String(50), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    severity = Column(String(20), default="MEDIUM")
    status = Column(String(30), default="NEW")
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    closed_at = Column(DateTime, nullable=True)

    assigned_user = relationship("User", back_populates="incidents")
    notes = relationship("IncidentNote", back_populates="incident")
    actions = relationship("ResponseAction", back_populates="incident")
    incident_alerts = relationship("IncidentAlert", back_populates="incident")


class IncidentAlert(Base):
    __tablename__ = "incident_alerts"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=False)
    alert_id = Column(Integer, ForeignKey("alerts.id"), nullable=False)

    incident = relationship("Incident", back_populates="incident_alerts")
    alert = relationship("Alert", back_populates="incident_links")


class IncidentNote(Base):
    __tablename__ = "incident_notes"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    note = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    incident = relationship("Incident", back_populates="notes")
    user = relationship("User", back_populates="notes")


class ResponseAction(Base):
    __tablename__ = "response_actions"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(Integer, ForeignKey("incidents.id"), nullable=False)
    action = Column(Text, nullable=False)
    status = Column(String(30), default="RECOMMENDED")
    executed_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    incident = relationship("Incident", back_populates="actions")


class AIAnalysis(Base):
    __tablename__ = "ai_analyses"

    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer, ForeignKey("alerts.id"), nullable=False)
    summary = Column(Text, nullable=False)
    severity_reason = Column(Text, nullable=False)
    attack_type = Column(String(100), nullable=False)
    recommendations = Column(Text, nullable=True)
    confidence = Column(Integer, default=0)
    provider = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    alert = relationship("Alert", back_populates="ai_analyses")


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    action = Column(String(100), nullable=False)
    resource = Column(String(100), nullable=False)
    resource_id = Column(String(100), nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    metadata = Column(JSON, nullable=True)

    user = relationship("User", back_populates="audit_logs")


__all__ = [
    "Base",
    "User",
    "Host",
    "Event",
    "DetectionRule",
    "Alert",
    "IOC",
    "ThreatIntel",
    "MITREMapping",
    "Incident",
    "IncidentAlert",
    "IncidentNote",
    "ResponseAction",
    "AIAnalysis",
    "AuditLog",
]
