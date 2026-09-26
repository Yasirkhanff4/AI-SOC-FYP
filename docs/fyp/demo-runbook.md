# Safe Demo Runbook

## Preparation

1. Copy `.env.example` to `.env` and keep demo mode enabled.
2. Start PostgreSQL/backend/frontend using the documented commands.
3. Verify `/health` and open Swagger at `/docs`.
4. Confirm that all records shown as synthetic are labeled as such.

## Demo 1 — Brute Force

1. Log in as the demo analyst.
2. Submit an authentication event with `failed_attempts=8`, `time_window_minutes=5`, and source `192.0.2.10`.
3. Create or trigger the corresponding alert.
4. Show the risk score and severity.
5. Run AI analysis and point out evidence, inference, recommendation, and uncertainty.
6. Show T1110 mapping.
7. Create an incident and add an investigation note.

## Demo 2 — Port Scan Pattern

Submit a synthetic event with `ports_touched=25`. Explain that this is a lab pattern and not an instruction to scan real systems. Show the T1046 mapping and recommended investigation.

## Demo 3 — Threat Intelligence Fallback

Look up `192.0.2.10`. Explain that the response is local mock intelligence and not evidence from the public internet.

## Demo 4 — ML Prediction

Train the model using the documented script, submit a normal feature vector, then submit a suspicious feature vector. Show the prediction and confidence as an experimental signal.

## Demo 5 — Full Incident

Create incident → add note → add simulated response action → move through statuses → close after analyst confirmation → generate PDF report → show audit entry.

## Recovery Plan

If an external API, Wazuh agent, or LLM is unavailable, use demo mode and explicitly state the fallback. If the dashboard fails, use Swagger to demonstrate the same backend workflow. Never improvise real offensive activity during the defense.
