import random
import time

# Global control variables (set from dashboard)
attack_mode = "normal"
intensity = 1

def set_attack_mode(mode):
    global attack_mode
    attack_mode = mode

def set_intensity(level):
    global intensity
    intensity = level

def generate_traffic():
    global attack_mode, intensity

    # SYN Flood Simulation
    if attack_mode == "SYN Flood":
        return {
            "timestamp": time.time(),
            "src_ip": "192.168.1.200",
            "dst_port": 80,
            "protocol": "TCP",
            "flag": "SYN"
        }

    # Port Scan Simulation
    if attack_mode == "Port Scan":
        return {
            "timestamp": time.time(),
            "src_ip": "192.168.1.150",
            "dst_port": random.randint(20, 20 + intensity * 10),
            "protocol": "TCP",
            "flag": "SYN"
        }

    # Normal Traffic
    return {
        "timestamp": time.time(),
        "src_ip": f"192.168.1.{random.randint(1,5)}",
        "dst_port": random.choice([80, 443]),
        "protocol": "TCP",
        "flag": "ACK"
    }