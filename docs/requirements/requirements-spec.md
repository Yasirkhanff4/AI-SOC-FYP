# API Contract

## Authentication

### POST /api/auth/login
Request:
```json
{
  "username": "admin",
  "password": "StrongPass123!"
}
```

Response:
```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}
```

### POST /api/auth/register
### POST /api/auth/refresh
### POST /api/auth/logout
### GET /api/auth/me

## Dashboard

### GET /api/dashboard/summary
### GET /api/dashboard/timeline
### GET /api/dashboard/top-attacks
### GET /api/dashboard/top-ips

## Events

### GET /api/events
### GET /api/events/{id}
### POST /api/events

## Alerts

### GET /api/alerts
### GET /api/alerts/{id}
### POST /api/alerts
### PATCH /api/alerts/{id}
### POST /api/alerts/{id}/analyze
### POST /api/alerts/{id}/enrich

## Incidents

### GET /api/incidents
### POST /api/incidents
### GET /api/incidents/{id}
### PATCH /api/incidents/{id}
### POST /api/incidents/{id}/notes
### POST /api/incidents/{id}/actions
### POST /api/incidents/{id}/close

## MITRE

### GET /api/mitre/techniques
### GET /api/mitre/{technique_id}

## Threat Intelligence

### GET /api/threat-intel/{ioc}
### POST /api/threat-intel/check

## AI

### POST /api/ai/analyze-alert
### POST /api/ai/investigate
### POST /api/ai/explain
### POST /api/ai/recommend-response

## Reports

### POST /api/reports/incident/{id}
### GET /api/reports/{id}

## Security Expectations

- JWT auth
- Role-based access control
- strict input validation
- logging for audit purposes
- no secret leakage in API responses
