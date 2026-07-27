import os

def ping_host(host):
    # Vulnerable: user-controlled input is inserted into a shell command
    command = f"ping -c 1 {host}"
    return os.system(command)

host = input("Enter hostname: ")
ping_host(host)
