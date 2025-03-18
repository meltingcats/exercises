#!/usr/bin/env python

import subprocess

#this program prevents user from entering extra commands on the input. it is the secure version
#https://docs.python.org/3/library/subprocess.html
#subprocess.run(["ls", "-l"])  # doesn't capture output
#replacing the shell=True

interface = input("interface > ")
new_mac = input("new MAC > ")


print("[+] Changing MAC address for " + interface + " to " + new_mac)


subprocess.call(["ifconfig", interface, "down"]) 
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) #LIST inside brackets everytime it sees a space it closes the element, whats inside the quotation is part of the command 
subprocess.call(["ifconfig", interface, "up"])


subprocess.call("ifconfig " + interface + "", shell=True) #prints ifconfig of the interface

#print(f"The new mac address of interface {interface} is   {new_mac}")
