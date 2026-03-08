
def rule_detection(features):
    if features["syn_count"] > 15:
        return "SYN Flood"
    if features["unique_ports"] > 5:
        return "Port Scan"
    return None

def calculate_confidence(rule_attack, anomaly, features):
    score = 0

    if rule_attack:
        score += 50

    if anomaly:
        score += 20

    if features["syn_count"] > 10:
        score += 20

    if features["unique_ports"] > 5:
        score += 20

    return min(score, 100)

def get_severity(confidence):
    if confidence >= 75:
        return "Critical"
    elif confidence >= 50:
        return "High"
    elif confidence >= 30:
        return "Medium"
    return "Low"
