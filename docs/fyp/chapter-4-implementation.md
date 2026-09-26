# Chapter 4 — Implementation

## 4.1 Architecture

The platform is a monorepo with a React/TypeScript frontend, FastAPI backend, SQLAlchemy data layer, PostgreSQL production database, SQLite development fallback, ML package, provider abstractions, and Docker configuration.

## 4.2 Authentication and RBAC

Users authenticate with a password hash rather than plaintext credentials. JWT claims identify the subject and role. The intended roles are ADMIN, SOC_ANALYST, and VIEWER. Authorization checks must be applied to modifying endpoints, not only to the user interface.

## 4.3 Event Pipeline

An event is received from a controlled source or synthetic generator, normalized into common fields, stored, and made available to detection logic. Important fields include timestamp, source, event type, host, raw log, and normalized data.

## 4.4 Detection and Risk Scoring

Rule logic identifies brute-force, port-scan-like, and authentication anomaly patterns. Risk scoring combines severity, confidence, reputation, and correlation signals and normalizes the result to a 0–100 range. Analysts can override workflow status or severity according to policy.

## 4.5 Machine Learning

The ML pipeline generates synthetic records, engineers numeric features, trains models, evaluates them, saves the selected artifact, and serves inference through an API. The model is an assisting signal; it is not proof of compromise.

## 4.6 AI Analyst

The AI layer receives a controlled structured context. Its schema contains summary, attack type, severity reason, evidence, MITRE references, IOCs, recommendations, confidence, and uncertainty. Demo mode provides a deterministic local analysis when no external provider is configured.

## 4.7 Threat Intelligence and MITRE

Threat-intelligence providers implement a common interface. Local mock intelligence allows offline demonstrations. MITRE mapping uses a maintained allow-list of supported techniques and records evidence and confidence.

## 4.8 Incident Response

Analysts create incidents, link alerts, add investigation notes, record recommended or simulated response actions, move the incident through its lifecycle, close it with a reason, and generate a PDF report.

## 4.9 Frontend

The dashboard provides login, overview metrics, alert investigation, incident management, MITRE lookup, threat-intelligence lookup, and report access. Loading, empty, and error states should be demonstrated during defense.

## 4.10 Deployment

Docker Compose runs the backend, frontend, and PostgreSQL services. Wazuh remains an external lab integration unless a properly supported deployment is documented. Secrets are supplied through environment configuration and are not committed.
