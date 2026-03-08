MITRE_MAP = {
    "SYN Flood": "T1498 - Network Denial of Service",
    "Port Scan": "T1046 - Network Service Discovery"
}

def get_mitre(attack):
    return MITRE_MAP.get(attack, "Unknown")
