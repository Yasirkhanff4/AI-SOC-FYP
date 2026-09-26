def threat_lookup(value: str) -> dict:
    if "192.0.2" in value or "198.51.100" in value:
        return {
            "ioc": value,
            "reputation": "SUSPICIOUS",
            "score": 82,
            "provider": "LOCAL_MOCK",
        }
    return {
        "ioc": value,
        "reputation": "UNKNOWN",
        "score": 12,
        "provider": "LOCAL_MOCK",
    }
