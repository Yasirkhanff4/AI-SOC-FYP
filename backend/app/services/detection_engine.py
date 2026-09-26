from typing import Any, Dict


def calculate_risk_score(alert_context: Dict[str, Any]) -> int:
    severity_weight = {"LOW": 15, "MEDIUM": 30, "HIGH": 50, "CRITICAL": 75}
    score = severity_weight.get(alert_context.get("severity", "LOW"), 15)
    score += int((alert_context.get("confidence", 0.5) or 0.5) * 20)
    score += int((alert_context.get("ioc_reputation", 0) or 0) * 10)
    score += int((alert_context.get("correlation_score", 0) or 0) * 10)
    return min(score, 100)


def classify_risk(score: int) -> str:
    if score <= 24:
        return "LOW"
    if score <= 49:
        return "MEDIUM"
    if score <= 74:
        return "HIGH"
    return "CRITICAL"
