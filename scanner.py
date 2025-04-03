import socket
import argparse

def scan_tcp(ip, port):
    """Escaneia uma porta TCP usando socket."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        s.close()
        return "Aberta"
    except socket.timeout:
        return "Filtrada (sem resposta)"
    except socket.error:
        return "Fechada ou Filtrada"

def scan_udp(ip, port):
    """Escaneia uma porta UDP enviando um pacote vazio."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(1)
    try:
        s.sendto(b'', (ip, port))
        data, _ = s.recvfrom(1024)  # Tenta receber resposta
        s.close()
        return "Aberta"
    except socket.timeout:
        return "Aberta ou Filtrada (sem resposta)"
    except socket.error:
        return "Fechada"

def main():
    parser = argparse.ArgumentParser(
        description="Ferramenta simples para varredura de portas TCP e UDP."
    )
    parser.add_argument("ip", help="Endereço IP a ser escaneado")
    parser.add_argument(
        "-p", "--ports",
        help="Lista de portas separadas por vírgula (ex.: 22,80,443)",
        default="22,53,80,139,445,330"
    )
    args = parser.parse_args()

    ip = args.ip
    try:
        socket.inet_aton(ip)  # Valida o IP
    except socket.error:
        print("Endereço IP inválido.")
        return

    ports = [int(p.strip()) for p in args.ports.split(',')]

    print(f"Varredura de portas TCP em {ip}:")
    for port in ports:
        print(f"  Porta TCP {port}: {scan_tcp(ip, port)}")

    print(f"\nVarredura de portas UDP em {ip}:")
    for port in ports:
        print(f"  Porta UDP {port}: {scan_udp(ip, port)}")

if __name__ == '__main__':
    main()