from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import time
#Import YAML module
import yaml



with open('qashow_.cfg', 'r') as f:
    qashow = f.read().rstrip()
print(qashow)

with open('newvlan_dsw1_.cfg', 'r') as f:
    dsw1_cmds = f.read().splitlines()

device_dsw1 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.1.13',
    'username': 'cisco',
    'password': 'cisco',
}

device_dsw2 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.1.14',
    'username': 'cisco',
    'password': 'cisco',
}

auth_dsw1 = [device_dsw1]
auth_dsw2 = [device_dsw2]

for devices_dsw1 in auth_dsw1:
    net_connect = ConnectHandler(**devices_dsw1)
    qa_dsw1 = net_connect.send_command(qashow)
    print(qa_dsw1)
