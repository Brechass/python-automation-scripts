# scripts/check_open_ports.py

import socket
from tqdm import tqdm

def scan_ports(ip, start_port, end_port):
    open_ports = []

    print(f"\nEscaneando puertos de {ip} ({start_port}-{end_port})...\n")

    for port in tqdm(range(start_port, end_port + 1), desc="Escaneando", unit="puerto"):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        s.close()

    return open_ports

if __name__ == "__main__":
    ip = input("Introduce la IP que quieres escanear: ")
    start = int(input("Puerto inicial: "))
    end = int(input("Puerto final: "))

    ports = scan_ports(ip, start, end)

    print("\nEscaneo completado.\n")

    if ports:
        print("Puertos abiertos:")
        for port in ports:
            print(f"  - {port}")
    else:
        print("No se encontraron puertos abiertos.")
