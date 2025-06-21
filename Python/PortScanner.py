#nmap not intrinsically installed with python. Will need to install nmap module with command in terminal "pip install python-nmap".
import nmap

scanner = nmap.PortScanner()

target = input("What is your IP target?")
#We will use Nmap website IP for practice. 45.33.32.156.
#Can change the options depending on what nmap options you need.
options = "-sV -sC"

scanner.scan(target, arguments = options)

#results saved in another file called "ScanResults.txt" for readability
with open("ScanResults.txt", "w") as outputfile:
    #scan for all IPs and writes them to file
    for hosts in scanner.all_hosts():
        outputfile.write(f"Host: {hosts} {scanner[hosts].hostname()}\n")
        outputfile.write(f"State: {scanner[hosts].state()}\n")
        #scan for protocols then writes them to file
        for protocol in scanner[hosts].all_protocols():
            outputfile.write(f"Protocol: {protocol}\n")
            port_info = scanner[hosts][protocol]
            #returns ports and their state to outputfile
            for port, state in port_info.items():
                outputfile.write(f"Port: {port}\t State: {state}\n")