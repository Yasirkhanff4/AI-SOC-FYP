from fastapi import APIRouter

router = APIRouter(prefix="/reports", tags=["reports"])


@router.post("/incident/{incident_id}")
def generate_report(incident_id: int):
    return {"message": f"Report generated for incident {incident_id}", "status": "success", "file": f"reports/incident_{incident_id}.pdf"}


@router.get("/{report_id}")
def get_report(report_id: str):
    return {"id": report_id, "status": "available", "type": "incident_report"}
