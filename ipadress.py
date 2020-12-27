"""
App that prints the Hostname, Local and Public IP-addresses.
"""
import socket
from requests import get


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP


hostname = socket.gethostname()
# local_ip = socket.gethostbyname(hostname)
local_ip = get_ip()
public_ip = get("https://api.ipify.org").text

print(f"Hostname: {hostname}")
print(f"Local IP: {local_ip}")
print(f"Public IP: {public_ip}")