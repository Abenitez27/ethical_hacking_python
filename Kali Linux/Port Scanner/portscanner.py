import socket
from IPy import IP

def scan(target): #Runs the scan_port function on target variable with specified port range
    converted_ip = check_ip(target)
    print('\n' + ' Scanning Target: ' + str(target))
    for port in range(1,int(port_num)):
        scan_port(converted_ip, port)

def check_ip(ip): # Checks input for ip addresses
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip) # Converts domain names into ip addresses

def get_banner(s): #Grabs banners for us
    return s.recv(1024)

def scan_port(ipaddress, port): #Scans ip address for open ports
    try:
        sock = socket.socket()
        sock.settimeout(0.5) #sets a time limit to the connection request and reduces time wasted
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Port {} is open : {}'.format(port,banner.decode().strip('\n')))
        except:
            print('[+] Port {} is open'.format(port))
    except:
        pass

if __name__ == '__main__': # only runs when script is the main program and not imported
    # Take input from user for port range
    port_num = input('Enter the number of ports you would like to scan: ')
    #Takes ip address input from the user
    targets = input('[+] Enter Target/s To Scan(split mulitple targets with a comma): ')
    if ',' in targets: #Checks to see if the user entered mutiple targets
        for ip_add in targets.split(','):
            scan(ip_add.strip(' '))
    else:
        scan(targets)

