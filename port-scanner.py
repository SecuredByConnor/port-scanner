import socket
import subprocess
import sys
from datetime import datetime

# Clears the terminal screen (Linux/Unix)
subprocess.call('clear', shell=True)    # shell=True allows 'clear' command to run as if typed directly into the terminal

# Prompt the user to enter the target IP or hostname
remote_server = input("Please enter a hostname or IP address to scan: ")
remote_server_ip = socket.gethostbyname(remote_server)  