# AI-SOC FYP

AI-SOC is a defensive, modular Security Operations Center platform for a cybersecurity final-year project. It demonstrates the traceable workflow:

```text
Synthetic/Lab Event → Normalization → Detection → Alert → Risk Score
→ AI-assisted Investigation → Threat Intelligence → MITRE ATT&CK
→ Incident → Analyst Notes/Response → PDF Report → Audit Log
```

> **Scope:** authorized defensive laboratory use only. Demo events are synthetic. No malware, exploit payloads, or destructive response automation are included.

## Current implementation

- FastAPI backend with SQLite development fallback and PostgreSQL configuration
- SQLAlchemy relational models for users, hosts, events, alerts, IOCs, incidents, analyses, and audit logs
- bcrypt password hashing and JWT authentication foundation
- role model for `ADMIN`, `SOC_ANALYST`, and `VIEWER`
- event, alert, incident, AI, MITRE, threat-intel, and report API routes
- deterministic demo-mode AI analysis and local threat-intelligence fallback
- React/TypeScript dark SOC dashboard
- ML and FYP documentation structure
- Docker Compose development stack

Some integrations, including external Wazuh deployment and external LLM/provider clients, remain environment-dependent and are explicitly documented as limitations. Do not present unexecuted metrics as results.

## Repository layout

```text
backend/       FastAPI API, SQLAlchemy models, services, tests
frontend/      React + TypeScript dashboard
ml/            synthetic dataset, features, training, inference
docs/          architecture, requirements, and FYP chapters
reports/       generated local PDF reports (ignored except .gitkeep)
scripts/       operational helper scripts
docker-compose.yml
.env.example
```

## Local setup

### Windows PowerShell

```powershell
Copy-Item .env.example .env
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:PYTHONPATH = (Get-Location).Path
pytest -q
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Linux/Kali

```bash
cp .env.example .env
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH="$PWD"
pytest -q
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

In a second terminal:

```bash
cd frontend
npm install
npm run dev
```

- API: http://localhost:8000
- Swagger: http://localhost:8000/docs
- Frontend: http://localhost:5173
- Demo login: `admin` / `StrongPass123!` (change for any non-demo deployment)

## Docker

```bash
cp .env.example .env
docker compose up --build
```

PowerShell uses the same Compose command:

```powershell
Copy-Item .env.example .env
docker compose up --build
```

PostgreSQL is the Compose database. Wazuh is intentionally documented as an external lab dependency rather than a fake Compose service.

## ML experiment

```bash
python ml/data/generate_synthetic_security_data.py
python ml/models/train_model.py
```

The output model and metrics are generated artifacts. Copy measured values into `docs/fyp/chapter-5-testing-and-results.md` only after executing the experiment.

## Documentation

- Architecture: `docs/architecture/architecture.md`
- API contract: `docs/architecture/api-contract.md`
- Requirements: `docs/requirements/requirements-spec.md`
- FYP chapters and defense pack: `docs/fyp/`
- Safe demo sequence: `docs/fyp/demo-runbook.md`

## Security and academic integrity

- Never commit `.env`, API keys, JWT secrets, passwords, generated databases, or reports containing sensitive data.
- Treat AI output as advisory and distinguish evidence, inference, recommendation, and uncertainty.
- Do not claim production accuracy, real-world prevalence, or performance without recorded experiments.
- Use only authorized systems and synthetic or approved lab telemetry.

## Team ownership

1. SIEM, collection, normalization, and rules
2. ML features, training, evaluation, and inference
3. AI analyst, threat intelligence, and MITRE mapping
4. Dashboard, incidents, response workflow, and reports

## License

MIT
