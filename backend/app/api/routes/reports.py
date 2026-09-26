from fastapi import APIRouter

router = APIRouter(prefix="/threat-intel", tags=["threat-intel"])


@router.get("/{ioc}")
def get_threat_intel(ioc: str):
    if "192.0.2" in ioc or "198.51.100" in ioc:
        return {
            "ioc": ioc,
            "provider": "LOCAL_MOCK",
            "reputation": "SUSPICIOUS",
            "score": 78,
            "summary": "Synthetic malicious reputation lookup for lab demonstration",
        }
    return {"ioc": ioc, "provider": "LOCAL_MOCK", "reputation": "UNKNOWN", "score": 12, "summary": "No strong reputation signal"}


@router.post("/check")
def check_threat_intel(payload: dict):
    value = payload.get("value", "")
    return get_threat_intel(value)
