def simulate_response(ip, severity):
    if severity in ["High", "Critical"]:
        return f"Simulated Action: Blocking IP {ip}"
    return "Monitoring activity"
