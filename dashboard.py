import streamlit as st
import time
import pandas as pd
import json

from main import run_detection
from traffic_simulator import set_attack_mode, set_intensity

st.set_page_config(layout="wide")

st.title("Autonomous AI Network Defense System v4")

# -------------------------------
# Attack Scenario Selector
# -------------------------------

attack_option = st.selectbox(
    "Select Attack Scenario",
    ["Normal Traffic", "SYN Flood", "Port Scan"]
)

intensity = st.slider("Attack Intensity", 1, 10, 3)

set_attack_mode(attack_option)
set_intensity(intensity)

# -------------------------------
# Auto Simulation Toggle
# -------------------------------

auto_mode = st.checkbox("Enable Auto Simulation Mode")

alert_placeholder = st.empty()

# -------------------------------
# Detection Loop
# -------------------------------

if st.button("Start Simulation") or auto_mode:

    for i in range(20):   # 20 traffic cycles
        result = run_detection()

        if result:
            alert_placeholder.error(f"""
Threat Detected!

Attack: {result['attack']}
MITRE: {result['mitre']}
Severity: {result['severity']}
Confidence: {result['confidence']}%
Response: {result['response']}
""")
        else:
            alert_placeholder.success("No threat detected.")

        time.sleep(0.5)

# -------------------------------
# Incident Timeline
# -------------------------------

def load_incidents():
    try:
        with open("incidents.json") as f:
            return [json.loads(line) for line in f]
    except:
        return []

incidents = load_incidents()

if incidents:
    df = pd.DataFrame(incidents)

    st.subheader("Incident Timeline")
    st.dataframe(df.sort_values("timestamp", ascending=False))

    st.subheader("Confidence Over Time")
    st.line_chart(df.set_index("timestamp")["confidence"])