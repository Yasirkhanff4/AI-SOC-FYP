from fastapi import APIRouter

router = APIRouter(prefix="/mitre", tags=["mitre"])


@router.get("/techniques")
def list_techniques():
    return {
        "techniques": [
            {"id": "T1110", "name": "Brute Force", "tactic": "Credential Access"},
            {"id": "T1046", "name": "Network Service Discovery", "tactic": "Discovery"},
            {"id": "T1078", "name": "Valid Accounts", "tactic": "Defense Evasion"},
        ]
    }


@router.get("/{technique_id}")
def get_technique(technique_id: str):
    mapping = {
        "T1110": {"id": "T1110", "name": "Brute Force", "tactic": "Credential Access"},
        "T1046": {"id": "T1046", "name": "Network Service Discovery", "tactic": "Discovery"},
    }
    return mapping.get(technique_id, {"id": technique_id, "name": "Unknown technique"})
