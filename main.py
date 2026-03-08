# ==============================
# main.py
# Core Detection Engine
# ==============================

from traffic_simulator import generate_traffic
from features import extract_features
from detection import rule_detection, calculate_confidence, get_severity
from ai_engineer import detect_anomaly
from mitre_mapping import get_mitre
from logger import log_incident
from response import simulate_response


def run_detection():
    # Generate simulated traffic
    packet = generate_traffic()

    # Extract behavioral features
    features = extract_features(packet)

    # Run rule-based detection
    rule_attack = rule_detection(features)

    # Run ML anomaly detection
    anomaly = detect_anomaly(features)

    # If nothing suspicious → return
    if not rule_attack and not anomaly:
        return None

    # Calculate confidence
    confidence = calculate_confidence(rule_attack, anomaly, features)
    severity = get_severity(confidence)

    # Smart labeling
    if rule_attack:
        attack_label = rule_attack
        mitre = get_mitre(rule_attack)
    elif anomaly and confidence >= 50:
        attack_label = "Suspicious Activity"
        mitre = "Behavioral Anomaly"
    else:
        return None  # ignore weak anomaly

    # Log structured incident
    log_incident(attack_label, mitre, severity, confidence)

    # Simulated defensive response
    action = simulate_response(packet["src_ip"], severity)

    return {
        "attack": attack_label,
        "mitre": mitre,
        "severity": severity,
        "confidence": confidence,
        "response": action
    }