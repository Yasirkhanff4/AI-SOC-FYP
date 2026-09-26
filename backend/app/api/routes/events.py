from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary")
def dashboard_summary():
    return {
        "total_alerts": 128,
        "critical_alerts": 9,
        "high_alerts": 21,
        "medium_alerts": 46,
        "low_alerts": 52,
        "open_incidents": 7,
        "resolved_incidents": 28,
        "active_threats": 3,
        "events_per_day": 1842,
    }


@router.get("/timeline")
def dashboard_timeline():
    return {"timeline": [{"time": "09:00", "events": 120}, {"time": "10:00", "events": 190}, {"time": "11:00", "events": 210}]}


@router.get("/top-attacks")
def top_attacks():
    return {"data": [{"name": "Brute Force", "value": 34}, {"name": "Port Scan", "value": 19}, {"name": "Suspicious Auth", "value": 15}]}


@router.get("/top-ips")
def top_ips():
    return {"data": [{"ip": "192.0.2.10", "count": 42}, {"ip": "198.51.100.7", "count": 16}, {"ip": "203.0.113.9", "count": 11}]}
