import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter IP to scan: ")
port = int(input("Enter port to check: "))
hostname = socket.gethostbyaddr(host)
def portscanner(port_scn):
    if s.connect_ex((host, port_scn)):
        print(f"Port {port_scn} is closed for host {host}")
    else:
        print(f"Port {port_scn} is open for host {host}")
        print(hostname)

portscanner(port)