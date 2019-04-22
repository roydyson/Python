from netmiko import ConnectHandler
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import time
#Import YAML module
import yaml

#Load data from YAML into Python dictionary
config_data = yaml.load(open('./newvlan.yaml'))

#Load Jinja2 template
env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
dsw1_template = env.get_template('newvlan_dsw1.j2')

env = Environment(loader = FileSystemLoader('./'), trim_blocks=True, lstrip_blocks=True)
dsw2_template = env.get_template('newvlan_dsw2.j2')

#Render the template with data and print the output
print(dsw1_template.render(config_data))
dsw1cfg = open( "newvlan_dsw1" + "_.cfg", "w")
dsw1cfg.write(dsw1_template.render(config_data))

print(dsw2_template.render(config_data))
dsw2cfg = open( "newvlan_dsw2" + "_.cfg", "w")
dsw2cfg.write(dsw2_template.render(config_data))



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
    output_dsw1 = net_connect.send_config_set(dsw1_template.render(config_data))
    print(output_dsw1)

for devices_dsw2 in auth_dsw2:
    net_connect = ConnectHandler(**devices_dsw2)
    output_dsw2 = net_connect.send_config_set(dsw2_template.render(config_data))
    print(output_dsw2)
