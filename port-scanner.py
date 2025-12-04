import socket
import subprocess
import sys
from datetime import datetime

#Clear the screen
subprocess.call('clear', shell=True)

#Ask user for input
remote_server = input("Please enter an IP address to scan: ")
remote_server_ip = socket.gethostbyname(remote_server)