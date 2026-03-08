import json
from datetime import datetime

def log_incident(attack, mitre, severity, confidence):
    incident = {
        "timestamp": datetime.utcnow().isoformat(),
        "attack": attack,
        "mitre": mitre,
        "severity": severity,
        "confidence": confidence
    }

    with open("incidents.json", "a") as f:
        f.write(json.dumps(incident) + "\n")
