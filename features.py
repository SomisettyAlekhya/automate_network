
state_tracker = {}

def extract_features(packet):
    ip = packet["src_ip"]

    if ip not in state_tracker:
        state_tracker[ip] = {"syn_count": 0, "ports": set()}

    if packet["flag"] == "SYN":
        state_tracker[ip]["syn_count"] += 1

    state_tracker[ip]["ports"].add(packet["dst_port"])

    return {
        "src_ip": ip,
        "syn_count": state_tracker[ip]["syn_count"],
        "unique_ports": len(state_tracker[ip]["ports"])
    }
