"""
This script implements a simple TCP port scanner in Python that checks for common open
ports on a specified domain.

Usage:
    python3 port_scanner.py
"""

import socket

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995]
DOMAIN = "www.google.com"


def scan(domain, port):
    try:
        ip = socket.gethostbyname(domain)

        sock = socket.socket()
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            print(f"[+] Port open: {port}")

    except socket.error as e:
        print(f"[-] Error: {e}")


if __name__ == "__main__":
    print(f"[*] Scanning {DOMAIN} for open ports...\n")
    for port in COMMON_PORTS:
        scan(DOMAIN, port)
