#WHOIS is a tool that looks up the IP address and domain names in a database
import socket

def whois_lookup(domain: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connects to the url and port specified
    s.connect(("whois.iana.org", 43))
    #sends a query to the domain and converts to bytes
    s.send(f"{domain}\r\n".encode())
    
    response = b""
    #loop to receive data until all data is received
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data
    s.close()
    return response.decode()

website = input("What is the web address: \n").strip()
print(whois_lookup(website))