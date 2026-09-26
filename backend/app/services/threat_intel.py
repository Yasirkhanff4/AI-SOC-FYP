def generate_alert(payload: dict) -> dict:
    event_type = payload.get("event_type", "authentication_failure")
    source_ip = payload.get("source_ip", "192.0.2.10")
    username = payload.get("username", "test-user")
    severity = payload.get("severity", "HIGH")
    confidence = int(payload.get("confidence", 75))

    return {
        "title": f"{event_type.replace('_', ' ').title()} detected",
        "description": f"Suspicious event from {source_ip} involving user {username}.",
        "severity": severity,
        "risk_score": 75,
        "status": "NEW",
        "source_ip": source_ip,
        "destination_ip": payload.get("destination_ip", "10.0.0.5"),
        "username": username,
        "confidence": confidence,
        "event_id": payload.get("event_id"),
        "rule_id": payload.get("rule_id"),
    }
