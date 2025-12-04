import socket
import subprocess
import sys
from datetime import datetime

def clear_terminal():
    # Clears the terminal screen (Linux/Unix)
    subprocess.call('clear', shell=True)    # shell=True allows 'clear' command to run as if typed directly into the terminal.

def prompt_user():
    return input("Please enter a hostname or IP address to scan: ")

def print_separator():
    print("_" * 60)

def scan_message(remote_server_ip):
    print (f"Please wait, scanning remote host", (remote_server_ip))


def main():

    # Prompt the user to enter the target IP or hostname
    remote_server = input("Please enter a hostname or IP address to scan: ")
    # Resolve the hostname provided by the user to its corresponding IP address.
    # Ensures the scan runs againest a vaild IPv4 address.
    remote_server_ip = socket.gethostbyname(remote_server) 


# Runs the main function
if __name__ == "__main__":
    main()