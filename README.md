# AI-SOC FYP

AI-Powered Security Operations Center (SOC) for Intelligent Threat Detection, Automated Alert Triage, Threat Intelligence and Incident Response.

This repository contains the starter architecture, requirements specification, database model, API contract, and the first working implementation layers for the final-year cybersecurity project.

## Project Goal

Build a practical SOC platform that covers:
- log collection and normalization
- rule-based security detections
- risk scoring
- AI-assisted investigation
- threat intelligence enrichment
- MITRE ATT&CK mapping
- incident response workflows
- dashboard-based analyst operations
- PDF/report generation
- audit logging

## Repository Structure

```text
ai-soc/
├── backend/
│   ├── app/
│   └── tests/
├── frontend/
│   ├── src/
│   └── public/
├── docs/
│   ├── architecture/
│   ├── requirements/
│   └── project/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── README.md
└── LICENSE
```

## Quick Start

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Docker

```bash
docker compose up --build
```

## Documentation

- Architecture overview: `docs/architecture/architecture.md`
- ERD: `docs/architecture/erd.md`
- API contract: `docs/architecture/api-contract.md`
- Requirements specification: `docs/requirements/requirements-spec.md`
- Phase 1 implementation plan: `docs/project/phase-1-plan.md`

## Team Structure

- Member 1: SIEM, log collection, normalization, rules
- Member 2: ML threat detection and model evaluation
- Member 3: AI analyst, threat intel, MITRE mapping
- Member 4: SOC dashboard, incidents, reports

## Security Notice

This project is intended for authorized lab and defensive cybersecurity environments only. It does not contain malware or offensive tooling. All synthetic demos must remain in isolated educational environments.

## License

MIT
