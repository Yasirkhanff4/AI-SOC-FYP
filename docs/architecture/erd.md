# Database ERD Overview

## Core Tables

### Users
- id
- username
- email
- password_hash
- role
- is_active
- created_at

### Hosts
- id
- hostname
- ip_address
- operating_system
- agent_id
- status
- last_seen

### Events
- id
- timestamp
- source
- host_id
- event_type
- raw_log
- normalized_data
- created_at

### Alerts
- id
- event_id
- rule_id
- title
- description
- severity
- risk_score
- status
- source_ip
- destination_ip
- username
- confidence
- created_at
- updated_at

### Detection Rules
- id
- name
- description
- rule_type
- severity
- enabled
- created_at

### IOCs
- id
- alert_id
- type
- value
- reputation
- confidence
- source

### Threat Intelligence
- id
- ioc_id
- provider
- reputation
- score
- raw_response
- checked_at

### MITRE Mappings
- id
- alert_id
- tactic
- technique_id
- technique_name
- confidence
- evidence

### Incidents
- id
- incident_number
- title
- description
- severity
- status
- assigned_to
- created_at
- updated_at
- closed_at

### Incident Alerts
- incident_id
- alert_id

### Incident Notes
- id
- incident_id
- user_id
- note
- created_at

### Response Actions
- id
- incident_id
- action
- status
- executed_by
- created_at

### AI Analyses
- id
- alert_id
- summary
- severity_reason
- attack_type
- recommendations
- confidence
- provider
- created_at

### Audit Logs
- id
- user_id
- action
- resource
- resource_id
- timestamp
- metadata

## ERD Relationship Notes

- one host has many events
- one event may trigger one or more alerts
- one alert may contain many IOCs
- one alert may have many MITRE mappings
- one incident relates to many alerts
- each incident has multiple notes and response actions
- each important action is logged in audit logs

## Example Relationship Diagram

```text
users 1---* audit_logs
hosts 1---* events
events 1---* alerts
alerts 1---* iocs
alerts 1---* mitre_mappings
alerts 1---* ai_analyses
incidents 1---* incident_alerts *---1 alerts
incidents 1---* incident_notes
incidents 1---* response_actions
```
