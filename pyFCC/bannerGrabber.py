import socket

def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    print(s.recv(1024))



def main(): 
    ip = input("Enter IP: ")
    port = str(input("Enter port: "))

    banner(ip, port)

main()