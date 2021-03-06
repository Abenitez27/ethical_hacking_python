import portscanner

targets_ip = input('[+] * Enter Target To Scan for Vulnerable Open Ports: ')
port_num = int(input('[+] * Enter Amount Of Ports You Want To Scan(ex: 500 - first 500 ports): '))
vul_file = input('[+] * Enter Path To The File With Vulnerable Softwares: ')
print('\n')


target = portscanner.PortScan(targets_ip, port_num)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!! Vulnerable Banner: "' + banner + '" On Port: '+ str(target.open_ports[count]))
        count += 1