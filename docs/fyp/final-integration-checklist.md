# Final Integration Checklist

## Before demonstration

- [ ] Copy `.env.example` to `.env`; use a unique local `JWT_SECRET`.
- [ ] Confirm no `.env`, credentials, generated reports, databases, or model artifacts are tracked.
- [ ] Run backend tests and frontend build.
- [ ] Start the stack and verify `/health` and `/docs`.
- [ ] Confirm the database is PostgreSQL in Compose or SQLite only for local fallback.
- [ ] Train the ML artifact locally if demonstrating ML inference.
- [ ] Label all synthetic/demo data in the UI and presentation.
- [ ] Verify each API response used in the demo against the current code.

## Acceptance evidence

Record screenshots and command output for login, event ingestion, detection, alert analysis, threat-intel fallback, MITRE lookup, incident lifecycle, PDF generation, audit logging, and dashboard loading. Replace `[TO BE MEASURED]` in Chapter 5 only with recorded values.

## Known limitations to disclose

External Wazuh deployment, provider APIs, LLM providers, and production-grade token revocation depend on additional environment configuration. The current demo workflow is defensive and advisory; it does not automatically block, isolate, disable, or attack systems.
