def analyze_alert(payload: dict) -> dict:
    alert_id = payload.get("alert_id", "unknown")
    source_ip = payload.get("source_ip", "unknown")
    host = payload.get("host", "unknown")
    username = payload.get("username", "unknown")
    detection_rule = payload.get("detection_rule", "UNKNOWN_RULE")

    return {
        "alert_id": alert_id,
        "summary": f"Repeated authentication failures originated from {source_ip} against host {host} for user {username}. The activity matches a brute-force pattern and should be reviewed by an analyst.",
        "attack_type": "Brute Force",
        "severity_reason": "Multiple failed login attempts within a short time window and suspicious source behavior.",
        "evidence": [
            f"Source IP {source_ip} generated repeated failed logins",
            f"Rule {detection_rule} triggered",
            f"Target user {username} is affected",
        ],
        "mitre": [{"tactic": "Credential Access", "technique_id": "T1110", "technique_name": "Brute Force", "confidence": 0.82}],
        "iocs": [{"type": "ipv4", "value": source_ip, "confidence": 0.8}],
        "recommended_actions": [
            "Validate the affected account",
            "Review authentication logs for related failures",
            "Check source IP reputation and block if policy allows",
            "Confirm whether the activity is malicious or a lab simulation",
        ],
        "confidence": 0.82,
        "uncertainty": ["Data may be synthetic and environment-limited"],
    }


def investigate_alert(payload: dict) -> dict:
    return {
        "answer": "This alert appears consistent with a brute-force or authentication anomaly. The strongest evidence is repeated failed logins from the same source in a short time window.",
        "evidence": ["repeated failures", "single IP pattern", "suspicious login behavior"],
        "inference": "Likely credential attack or abuse pattern",
        "recommendation": "Validate the source, check account lockout history, and review edge-case logs.",
        "uncertainty": ["No real-world internet evidence was used in demo mode"],
    }
