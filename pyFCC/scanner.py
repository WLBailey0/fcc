#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome, this is an nmap automation tool")
print("<-------------------------------------->")

ip_addr = input("Enter IP address to scan: ")

print("You entered ", ip_addr)

type(ip_addr)

resp = input("""\n Ender type of scan to run \n
             1) SYN ACK\n
             2) UDP SCAN\n
             3) Comprehensive SCAN\n
             >>>>> """)
# print("You entered ", ip_addr)

if resp == '1':
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-4000', '-v -sS', sudo = True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("Protocol: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-4000', '-v -sU', sudo = True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("Protocol: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
if resp == '3':
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-6000', '-v -sS -sV -sC -A -O', sudo = True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("Protocol: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
