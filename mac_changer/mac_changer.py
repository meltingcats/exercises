#!/usr/bin/env python

import subprocess


interface = input("interface > ")
new_mac = input("new MAC > ")


print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)


subprocess.call("ifconfig " + interface + "", shell=True) #prints ifconfig of the interface


print(f"The new mac address of interface {interface} is   {new_mac}")
#8e:0f:24:b5:e1:07 original mac
