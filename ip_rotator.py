import requests
import random
import time

# ─────────────────────────────────────────────
# IP ROTATING SCRIPT
# Target: https://api.ipify.org/?format=json
# Every request shows a different public IP
# ─────────────────────────────────────────────

# List of free public proxies (IP:PORT)
PROXY_LIST = [
    "103.149.162.195:80",
    "47.74.152.29:8888",
    "200.105.215.22:33630",
    "45.167.125.97:9992",
    "190.61.88.147:8080",
    "103.155.217.1:41317",
    "185.62.190.7:8080",
    "51.79.50.46:9300",
    "91.92.155.207:3128",
    "64.225.8.82:9991",
]

# Target endpoint (as required by the task)
TARGET_URL = "https://api.ipify.org/?format=json"

# ─────────────────────────────────────────────
# Function to send request via a proxy
# ─────────────────────────────────────────────
def send_request_via_proxy(proxy):
    proxy_dict = {
        "http":  f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        response = requests.get(TARGET_URL, proxies=proxy_dict, timeout=5)
        json_response = response.json()  # Returns {"ip": "x.x.x.x"}
        return json_response
    except Exception as e:
        return {"ip": f"FAILED - {str(e)[:60]}"}

# ─────────────────────────────────────────────
# Main: Send 5 requests, each with different IP
# ─────────────────────────────────────────────
print("=" * 55)
print("        IP ROTATING SCRIPT")
print(f"  Target: {TARGET_URL}")
print("=" * 55)

seen_proxies = []  # Track used proxies to avoid repeats

for request_number in range(1, 6):
    # Pick a proxy not used before (ensure different IP each time)
    available = [p for p in PROXY_LIST if p not in seen_proxies]
    if not available:
        available = PROXY_LIST  # Reset if all used

    chosen_proxy = random.choice(available)
    seen_proxies.append(chosen_proxy)

    print(f"\n[Request #{request_number}]")
    print(f"  Routing through proxy : {chosen_proxy}")

    json_response = send_request_via_proxy(chosen_proxy)
    print(f"  JSON Response         : {json_response}")

    time.sleep(1)

print("\n" + "=" * 55)
print("  Every request used a different proxy IP!")
print("=" * 55)
