#!/usr/bin/python
import os
import portScanner

#Sub domain scanner
def domCh():	
	domain = raw_input("Please input the selected domain\n")
	os.system("dmitry -s %s > subs.txt"%(domain))
	f = open('subs.txt',"r")
	subs = []
	for line in f:
		#print line
		if line.find("HostIP:")!=-1:
			subs.append(line.strip("HostIP:\n"))
	f.close()
	domChoice = raw_input("Choose one:\n 1-Scan a selected port in all of the found subdomains | 2-Scan all the ports in 1 of the displayed domains | Anything else, quit the program\n")
	if domChoice == "1":
		flag = 0
		port = [int(raw_input("which port would you like to scan?\n"))]
		for ip in subs:
			isOpen = []
			portScanner.qScanPortList(ip,port,isOpen)
			if isOpen[0] == port:
				print "for ip:\n port %s is open\n"%(str(port))
				flag = 1
		if flag == 0:
			print "This ip isn't open in any of the ips.\n"
	elif domChoice ==  "2":
		i = 1
		for ip in subs:
			print str(i)+" - %s \n"%(ip)
			i = i + 1
		isOpen = []
		ip = subs[int(raw_input("Input the number of your chosen host.\n"))-1]
		print "Scanning, this may take a while, please wait."
		portScanner.qScanPortList(ip,range(0,65536),isOpen)
		print "ports"+str(isOpen)+"are open"
	else:
		sys.exit()

