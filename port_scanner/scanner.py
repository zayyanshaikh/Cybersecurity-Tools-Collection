"""Simple multi-threaded TCP port scanner (educational use only)."""
import argparse
import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(host: str, port: int, timeout: float) -> bool:
    """Return True if the TCP port is open."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except (socket.timeout, ConnectionRefusedError, OSError):
        return False


def main() -> None:
    parser = argparse.ArgumentParser(description="TCP port scanner")
    parser.add_argument("host", help="Target host (only scan what you own or are authorized to test)")
    parser.add_argument("-s", "--start", type=int, default=1, help="Start port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="End port")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Timeout in seconds")
    args = parser.parse_args()

    try:
        ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        print(f"Cannot resolve host: {args.host}")
        return

    ports = range(args.start, args.end + 1)
    print(f"Scanning {args.host} ({ip}) ports {args.start}-{args.end}...")

    with ThreadPoolExecutor(max_workers=100) as pool:
        results = pool.map(lambda p: (p, scan_port(ip, p, args.timeout)), ports)
        open_ports = [p for p, is_open in results if is_open]

    if open_ports:
        for p in open_ports:
            print(f"Port {p} is open")
    else:
        print("No open ports found.")


if __name__ == "__main__":
    main()