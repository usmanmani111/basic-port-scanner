#!/usr/bin/env python3
"""Basic Port Scanner — student learning project (Python stdlib only).

Scans YOUR OWN computer (localhost / 127.0.0.1) only.
Never scan a computer, server or network you do not own or do not
have explicit permission to test — that is the responsible rule
behind penetration testing.

Run it:
    python3 port_scanner.py
    python3 port_scanner.py --ports 22,80,443,8000,8080

What it teaches: TCP connect scans, sockets, timeouts, and how a
common service (SSH 22, HTTP 80, HTTPS 443) shows up as "open".
Try it while a local server is running (e.g. `python3 -m http.server`)
and watch port 8000 flip from closed to open.
"""
import argparse
import socket

# Common ports and the service usually behind them.
COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS",
    3306: "MySQL", 5432: "PostgreSQL", 8000: "HTTP-alt", 8080: "HTTP-proxy",
}

ALLOWED_HOSTS = {"127.0.0.1", "localhost", "::1"}


def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    """Return True if a TCP connection to host:port succeeds."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Basic Port Scanner (localhost only)")
    parser.add_argument("--host", default="127.0.0.1",
                        help="host to scan (only localhost / 127.0.0.1 allowed)")
    parser.add_argument("--ports", default=",".join(str(p) for p in COMMON_PORTS),
                        help="comma-separated ports, e.g. 22,80,443")
    args = parser.parse_args()

    if args.host not in ALLOWED_HOSTS:
        print(f"Refused: this starter only scans your own computer ({args.host} not allowed).")
        print("Only scan systems you own or have permission to test.")
        raise SystemExit(1)

    ports = [int(p.strip()) for p in args.ports.split(",") if p.strip()]
    print(f"Scanning {args.host} — {len(ports)} ports...\n")
    open_ports = []
    for port in ports:
        service = COMMON_PORTS.get(port, "unknown")
        if scan_port(args.host, port):
            print(f"  [OPEN]   {port:<6} {service}")
            open_ports.append(port)
        else:
            print(f"  [closed] {port:<6} {service}")
    print(f"\nDone. {len(open_ports)} open port(s): {open_ports or 'none'}")


if __name__ == "__main__":
    main()
