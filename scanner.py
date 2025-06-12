import sys
import socket
from datetime import datetime

if len(sys.argv)==2 :
    target = socket.gethostbyname(sys.argv[1])
else :
    print("Invalid amount of arguments")
    print("Syntax:python3 scanner.py <ip>")

print("\n" + "="*60)
print("|{:^58}|".format("PORT SCANNER"))
print("="*60)
print("|{:^58}|".format(f"Scanning Target: {target}"))
print("|{:^58}|".format(f"Time Started   : {datetime.now()}"))
print("="*60 + "\n")

try:
    for port in range(50,80):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        if result==0:
            print(f"[+] Port {port} is open.")
        s.close()

except KeyboardInterrupt:
    print("Exiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
