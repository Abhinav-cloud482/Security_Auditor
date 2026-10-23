
import socket
from datetime import datetime

def scan_ports(target, ports):
    print(f"\nPython Security Scanner")
    print(f"Target: {target}")
    print(f"Time: {datetime.now()}")
    print("-" * 40)

    for port in ports:
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        sock.settimeout(0.5)

        try:
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"[OPEN] Port {port}")
        except socket.gaierror:
            print("Could not resolve target hostname.")
            return
        except OSError as error:
            print(f"Scan error: {error}")
            return
        finally:
            sock.close()

    print("\nScan completed.")

if __name__ == "__main__":
    target = input(
        "Enter your own device IP or localhost: "
    ).strip()

    if target.lower() == "localhost":
        target = "127.0.0.1"

    common_ports = [
        22, 53, 80, 135, 139,
        443, 445, 3306, 3389, 8080
    ]

    scan_ports(target, common_ports)
