import socket
from IPy import IP

class PortScan():
    banners = []
    open_ports = []
    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num

    def scan(self): #Runs the scan_port function on target variable with specified port range
        for port in range(1,int(self.port_num)):
            self.scan_port(port)

    def check_ip(self): # Checks input for ip addresses
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target) # Converts domain names into ip addresses


    def scan_port(self, port): #Scans ip address for open ports
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5) #sets a time limit to the connection request and reduces time wasted
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                self.banners.append(banner)
            except:
                self.banners.append(' ')
            sock.close()
        except:
            pass
