# Architecture Overview

## High-level Design

The AI-SOC system follows a defensive SOC architecture in which security telemetry is ingested, normalized, correlated, classified, enriched, and investigated through a workflow that ends with incident resolution and reporting.

## System Components

### 1. Data Sources
- Windows hosts running Sysmon and Wazuh agents
- Linux hosts generating auth and audit logs
- Synthetic lab traffic for demonstration

### 2. Log Collection
- Wazuh agents
- Sysmon integration
- Normal Linux log ingestion
- Custom event generators for lab simulations

### 3. Normalization
- Standardized fields
- Event type mapping
- Source IP / destination IP extraction
- Host and user correlation

### 4. Detection Engine
- Rule-based detection
- ML anomaly detection
- Correlation engine

### 5. Alert Engine
- Alert severity assignment
- Risk scoring
- Confidence calculation
- IOC extraction

### 6. Threat Intelligence
- VirusTotal
- AbuseIPDB
- OTX
- Local mock provider fallback

### 7. AI Analyst
- Structured alert investigation
- Summary generation
- MITRE mapping assistance
- Recommended actions
- Evidence/inference separation

### 8. Incident Management
- Alert to incident linkage
- Investigation workflow
- Response actions
- Closure documents

### 9. Dashboard
- SOC overview
- Alert list and detail pages
- Incident page
- MITRE and threat intel views
- Reports and audit trails

## Main Architecture Diagram

```text
Data Sources
   ↓
Log Collection / Wazuh / Sysmon / Linux Logs
   ↓
Normalization Engine
   ↓
Detection + Correlation
   ↓
Alerts + Risk Scores
   ↓
Threat Intel + AI Analyst + MITRE Mapping
   ↓
Incident Management
   ↓
SOC Dashboard + Reports
```

## Proposed Technology Stack

### Frontend
- React
- TypeScript
- Tailwind CSS
- Recharts

### Backend
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL

### AI / ML
- Python
- scikit-learn
- pandas
- numpy
- optional XGBoost or PyTorch

### Security / Lab Tools
- Wazuh
- Sysmon
- Linux audit logs

## Design Principles

- defensive only
- modular architecture
- secure auth and RBAC
- synthetic data labeling
- configurable provider integrations
- fallback demo mode

## Implementation Notes

This repository begins the first implementation phase. The architecture remains compatible with later integrations such as SIEM ingestion, ML model deployment, AI analytics, and report generation.
