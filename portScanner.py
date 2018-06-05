#!/usr/bin/python
# --------------------------------------------------------------#
#PortScanner
# --------------------------------------------------------------#
import socket
import sys
import threading
import bannerGrab

#range(0,65536)
# --------------------------------------------------------------#
#Creates a list of ips for scanning from a start IP and end IP range.
# --------------------------------------------------------------#
def mkIpList(ip1, ip2):
	ipOne = ip1.split('.')
	ipTwo = ip2.split('.')
	ipList = []
	for p1 in range(int(ipOne[0]),int(ipTwo[0])+1):
		for p2 in range(int(ipOne[1]),int(ipTwo[1])+1):
			for p3 in range(int(ipOne[2]),int(ipTwo[2])+1):
				for p4 in range(int(ipOne[3]),int(ipTwo[3])+1):
					ipList.append(str(p1)+"."+str(p2)+"."+str(p3)+"."+str(p4))
	return ipList
# --------------------------------------------------------------#
#Scanning through allthe selected ips and ports via 1-8 threads. Later found out there is a possible max threads command
# --------------------------------------------------------------#
def scan(ip1,ip2,portList):
	ipList = mkIpList(ip1,ip2)
	openPorts = []
	t = []
	subPortList = []
	for ip in ipList:
		print "scanning ip:\n%s\nThis may take a while, Please wait."%(ip)
		if len(portList) <= 100:
			scanPortList(ip,portList)
		elif len(portList) <=1000:	
			mv = len(portList)%3
			subPortList.append(portList[0:(len(portList)-mv)/3])
			subPortList.append(portList[(len(portList)-mv)/3:(len(portList)-mv)/3*2])
			subPortList.append(portList[(len(portList)-mv)/3*2:len(portList)])
			for i in range(3):
				t.append(threading.Thread(target=scanPortList, args = [ip,subPortList[i],openPorts]))
			for x in t:
				x.start()
			for x in t:
				x.join()
		elif len(portList) > 1000:
			mv = len(portList)%8
			subPortList.append(portList[0:(len(portList)-mv)/8])
			subPortList.append(portList[(len(portList)-mv)/8:(len(portList)-mv)/8*2])
			subPortList.append(portList[(len(portList)-mv)/8*2:(len(portList)-mv)/8*3])
			subPortList.append(portList[(len(portList)-mv)/8*3:(len(portList)-mv)/8*4])
			subPortList.append(portList[(len(portList)-mv)/8*4:(len(portList)-mv)/8*5])
			subPortList.append(portList[(len(portList)-mv)/8*5:(len(portList)-mv)/8*6])
			subPortList.append(portList[(len(portList)-mv)/8*6:(len(portList)-mv)/8*7])
			subPortList.append(portList[(len(portList)-mv)/8*7:len(portList)])
			for i in range(8):
				t.append(threading.Thread(target=scanPortList, args = [ip,subPortList[i],openPorts]))
			for x in t:
				x.start()
			for x in t:
				x.join()
		openPorts.sort()
		print ip + ":" 
		print openPorts
# --------------------------------------------------------------#
#Scans the selected ports for a specific ip.
# --------------------------------------------------------------#
def scanPortList(ip, portList, openPorts):
	for port in portList:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.5)
			result = sock.connect_ex((ip,port))
			if result == 0:
				#print "port{}:	Open".format(port)
				if [21,22,23,25,80,110].find(port) != -1:
					bannerGrab.banGrab(sock)
				openPorts.append(port)
			sock.close()
		except KeyboardInterrupt:
			print "You presses Ctrl+C"
			sys,exit()
		except socket.gaierror:
			print "hostname sucks"
			sys.exit()
		except socket.error:
			print "couldn't connect"
			sys.exit()
# --------------------------------------------------------------#
#Specialport scan used to access the portscan outside the full run (Like in the added tool)
# --------------------------------------------------------------#
def qScanPortList(ip,portList,openPorts):
	subPortList = []
	t = []
	mv = len(portList)%8
	subPortList.append(portList[0:(len(portList)-mv)/8])
	subPortList.append(portList[(len(portList)-mv)/8:(len(portList)-mv)/8*2])
	subPortList.append(portList[(len(portList)-mv)/8*2:(len(portList)-mv)/8*3])
	subPortList.append(portList[(len(portList)-mv)/8*3:(len(portList)-mv)/8*4])
	subPortList.append(portList[(len(portList)-mv)/8*4:(len(portList)-mv)/8*5])
	subPortList.append(portList[(len(portList)-mv)/8*5:(len(portList)-mv)/8*6])
	subPortList.append(portList[(len(portList)-mv)/8*6:(len(portList)-mv)/8*7])
	subPortList.append(portList[(len(portList)-mv)/8*7:len(portList)])
	for i in range(8):
		t.append(threading.Thread(target=scanPortList, args = [ip,subPortList[i],openPorts]))
	for x in t:
		x.start()
	for x in t:
		x.join()
	
