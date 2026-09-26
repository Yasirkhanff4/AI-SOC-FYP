# Chapter 3 — Methodology

## 3.1 Development Method

The project uses iterative Agile development. Each increment has a defined objective, implementation tasks, tests, and a demonstrable outcome.

## 3.2 Iterations

1. Architecture and requirements
2. Database and authentication
3. Event ingestion and detection
4. ML training and evaluation
5. AI analyst, MITRE, and threat intelligence
6. Incident response and reports
7. Frontend, deployment, and defense preparation

## 3.3 Requirements Engineering

Functional requirements cover authentication, RBAC, ingestion, normalization, detection, risk scoring, enrichment, AI analysis, MITRE mapping, incident response, reports, audit logging, analytics, and search. Non-functional requirements cover security, maintainability, usability, performance, reliability, and auditability.

## 3.4 Experimental Design

The ML experiment uses generated synthetic records split into training and test partitions. The baseline and advanced models must be trained with a fixed random seed and evaluated on a held-out test set. The final report must record dataset-generation parameters, feature definitions, class distribution, software versions, and measured runtime.

## 3.5 Threat Model

Assets include credentials, event data, alert data, incident evidence, API keys, and reports. Threats include unauthorized API access, token theft, injection, sensitive-data exposure, manipulated events, and unsupported AI output. Controls include password hashing, JWT expiration, RBAC, validation, parameterized ORM queries, environment secrets, audit logs, and analyst approval.

## 3.6 Safety Model

Synthetic events and simulated response actions are used for demonstrations. Actions such as blocking an IP or isolating a host are recommendations or simulations only. The platform must not execute destructive actions against real systems.

## 3.7 Acceptance Traceability

Each objective should be linked to a route, service, UI workflow, and test. The team should maintain a traceability table in the final report showing requirement ID, implementation location, test case, and evidence screenshot.
