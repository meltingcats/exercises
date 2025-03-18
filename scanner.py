#!/bin/python3


import sys
import socket
from datetime import datetime

#this program doesn't have DNS so inputting string gets an error. always put an IP address instead

#define our target


if len(sys.argv) == 2:  #argv is like the $ in bash
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPV4
else:
	print("Invalid amout of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#python3 scanner.py <ip> #to see if port is open in a machine. argument 1 is scanner.py argument 2 is ip


#Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " +str(datetime.now()))
print("-" * 50)


try:
	for port in range(100,500):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #setting timer to 1 second if it doesnt connect so it will not attempt any longer
		result = s.connect_ex((target,port)) #returns an error indicator. if result port is open result is 0, if not open it returns error and trigget to 1
		#print("Checking port {}".format(port)) #printing every port checking
		if result == 0:
			print("Port {} is open".format(port))
		s.close() 
		
		
except KeyboardInterrupt: #like in linux, ctrl c to terminate
	print("\nExiting program.")
	sys.exit()

except socket.gaierror: #no hostname resolution exit the program
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error: #cant connect to IP address, exit
	print("Couldn't connec to server.")
	sys.exit()


		
