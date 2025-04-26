"""
This script creates a simple DNS server in Python that filters domain requests
based on a predefined block list. If a domain is listed in `BLOCK_LIST`, the server
responds with NXDOMAIN (non-existent domain). Otherwise, it forwards the request
to an external DNS resolver (default: 8.8.8.8).

Usage:  
    `python3 dns_filter.py`

Test:
    `dig @127.0.0.1 domain.com`

Make sure to run the script with root privileges to bind to port 53.
"""

from dnslib import DNSRecord
from dnslib.server import DNSServer, BaseResolver

BLOCK_LIST = ["instagram.com", "google.com", "github.com"]
DEFAULT_DNS = "8.8.8.8"


class DNSFilter(BaseResolver):
    def resolve(self, request, handler):
        qname = request.q.qname
        domain = str(qname).rstrip(".").lower()

        print(f"[+] Request for: {domain}")

        if domain in BLOCK_LIST:
            print(f"[-] Blocked: {domain}")
            reply = request.reply()
            reply.header.rcode = 3

            return reply

        try:
            proxy = DNSRecord.question(domain)
            response = proxy.send(DEFAULT_DNS, 53, tcp=False)

            return DNSRecord.parse(response)

        except Exception as e:
            print(f"[-] Request error: {e}")
            reply = request.reply()
            reply.header.rcode = 2

            return reply


if __name__ == "__main__":
    try:
        print("[*] DNS server with filter started!\n")
        server = DNSServer(DNSFilter(), port=53, address="127.0.0.1")
        server.start()
    except KeyboardInterrupt:
        print("\n[*] Stopping DNS server...")
        server.stop()
