#!/usr/bin/env python

import subprocess
import optparse
#python3 mac_changer.py --interface


parser = optparse.OptionParser() # OptionParser - starts with uppercase means it is a class. its function is to handle user input using arguments

parser.add_option("-i", "--interface", dest="interface", help="Interface to changes its MAC address") 
#-i specify interface, dest is the value of interface is stored, help is when user needs help it will display the text
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address") 

(options, arguments) = parser.parse_args() #allows user to entery and learn what it contains. this also returns the output with a given variable. returns 2 sets or information =  values and arguments. options and arguments are just variables


interface = options.interface #first user input
new_mac = options.new_mac #second input


print("[+] Changing MAC address for " + interface + " to " + new_mac)


subprocess.call(["ifconfig", interface, "down"]) 
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) #LIST inside brackets everytime it sees a space it closes the element, whats inside the quotation is part of the command 
subprocess.call(["ifconfig", interface, "up"])


#subprocess.call("ifconfig " + interface + "", shell=True) #prints ifconfig of the interface
