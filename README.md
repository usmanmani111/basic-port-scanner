# Basic Port Scanner

A small, safe port scanner written in Python. It checks which common ports are open on your own computer, using a TCP connect scan.

This is a learning project. It is not a professional security tool.

## What it does

- Scans 13 common ports on localhost (127.0.0.1) by default: FTP (21), SSH (22), Telnet (23), SMTP (25), DNS (53), HTTP (80), POP3 (110), IMAP (143), HTTPS (443), MySQL (3306), PostgreSQL (5432), HTTP-alt (8000), HTTP-proxy (8080)
- Prints each port as open or closed, with the service usually behind it
- Accepts a custom port list with `--ports`

## Technologies

- Python 3 (standard library only — no installation, no dependencies, no API key)

## How to run it

```bash
python3 port_scanner.py
```

Scan a custom set of ports:

```bash
python3 port_scanner.py --ports 22,80,443,8000,8080
```

Example output:

```
Scanning 127.0.0.1 — 13 ports...

  [closed] 21     FTP
  [closed] 22     SSH
  [closed] 80     HTTP
  ...

Done. 0 open port(s): none
```

Try it while a local server is running — for example, run `python3 -m http.server` in another terminal — and watch port 8000 flip from closed to open.

## Safety and responsible use

This scanner only scans your own computer. It refuses any other host:

```bash
python3 port_scanner.py --host 8.8.8.8
# Refused: this starter only scans your own computer (8.8.8.8 not allowed).
```

Only scan systems you own or have explicit permission to test. Scanning a computer or network without permission is not ethical hacking.

## What I learned

- TCP connect scans and Python sockets
- Timeouts and handling closed ports
- How common services map to port numbers
- Why a scanner must be limited to systems you are allowed to test

## Future improvements

- Add a service banner check for open ports
- Add a scan summary saved to a file
- Add a simple scan of a custom port range
