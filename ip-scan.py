#!/usr/bin/python
import ipaddress
import threading
import os
import subprocess

net_addr = raw_input ("Nhap network duoi dang CIDR format(192.168.1.0/24): ")
net = unicode(net_addr, "utf-8")
my_net = ipaddress.ip_network(net)
#print(my_net)
list_hosts = list(my_net.hosts())

def check_ping(list_hosts, i):
  reponse = subprocess.call([ 'ping', '-c', '1', str(list_hosts[i]) ],stdout=subprocess.PIPE)
  if reponse == 0:
    print( str(list_hosts[i]) + " " "Online")
  else:
    print( str(list_hosts[i]) + " " "Offline")
#
def main():
  for i in range (len(list_hosts)):
    thread = threading.Thread(target=check_ping, args=(list_hosts, i,  ))
    thread.start()

if __name__ == '__main__':
  main()

