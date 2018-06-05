#!/usr/bin/python
# --------------------------------------------------------------#
#UI
# --------------------------------------------------------------#
import tableUp
import portScanner
# --------------------------------------------------------------#
#Prints a list of all the countries in the site.
# --------------------------------------------------------------#
def printCount(list):
	contList = ""
	countNum = 0
	flag = 0
	for line in list:
		contList = contList + "[" + str(countNum) + "]" + strU(line[0]) +  "	"
		flag = flag +1
		countNum = countNum + 1
		if flag == 3:
			contList = contList+"\n"
			flag = 0
	print contList
# --------------------------------------------------------------#
# Returns True or False on a choice.
# --------------------------------------------------------------#
def ynRes(list, choice):
	yn = raw_input("Is this your choice?\n"+"(y = yes, anything else = No)\n")
	if str(yn).lower() == "y":				
		return 1
	else:
		return 0
# --------------------------------------------------------------#
# Returns the Number of the chosen country, returns -1 if country isn't found
# --------------------------------------------------------------#
def countryChoice(list, choice):
	if choice == '1':
		printCount(list)
		whLoop = 1
		while whLoop:		
			countNum = raw_input("Which number is the country you'd like?\n")
			try:
				print strU(list[int(countNum)][0])+"\n"	
				if ynRes(list,countNum):
					whLoop = 0
			except:
				print "Not suitble."
	else:
		countNum = 0
		for line in list:
			if str(line[0]).lower().find(choice.lower()) != -1: 
				break
			countNum = countNum + 1
		try:
			print strU(list[int(countNum)][0])+"\n"
			if ynRes(list,countNum):
				return countNum
		except:
			print "Could not find country, please try again"
			return -1
	return int(countNum)

# --------------------------------------------------------------#
# A Run command for the portscanner UI
# --------------------------------------------------------------#
def ipUI(list, countryNum):
	tableUp.ipUpdate(list, list[countryNum][0])
	print "Welcome to the port scanning and IP listing screen for  " + strU(list[countryNum][0]) + "\n"
	num = 0
	whBool = 1
	full5 = raw_input("Choose if you'd like a full list of IPs or only of the top 5 of the list, keep in mind a full list would take longer to load.\n 1 = Full, Anything else = Partial\n")
	for line in list[countryNum][2]:
		num = num +1
		tableUp.ownerUpdate(line)
		print str(num)+" | "+str(line[0])+" | "+str(line[1])+" | "+str(line[4])+'\n'
		if str(full5) != "1":
			if num == 5:
				break
	while whBool:
		userCh = raw_input("Please choose one of the following options:\n 1-Scan a presented range | 2-Scan a few presented ranges | 3-Scan a specific IP address | 4-Scan a specific IP range\n")
		if str(userCh) == "1":
			nCh = raw_input("Pick the number of the one of the ranges above\n")
			chIP = [strU(list[countryNum][2][int(nCh)-1][0]),strU(list[countryNum][2][int(nCh)-1][1])] 
			portUI(chIP[0],chIP[1])
			whBool = 0
		if str(userCh) == "2":
			while nCh != -1:
				nCh = raw_input("Input the numbers of the chosen ranges with Enter in between, input -1 to end the list\n")
				chIP.append([strU(list[countryNum][2][int(nCh)-1][0]),strU(list[countryNum][2][int(nCh)-1][1])])
			for ipRange in chIP:
				portUI(ipRange[0],ipRange[1])
			whBool = 0
		if str(userCh) == "3":
			nCh = raw_input("Type in the specific IP\n")
			portUI(nCh,nCh)
			whBool = 0
		if str(userCh) == "4":
			nCh = [raw_input("Input starting IP\n"),raw_input("Input end IP\n")] 
			portUI(nCh[0],nCh[1])			
			whBool = 0
		if whBool == 1:
			print "You've not chosed a proper response, try again"

# --------------------------------------------------------------#
# A run command for the  port UI
# --------------------------------------------------------------#
def portUI(ip1,ip2):
	whBool = 1
	print "For the IP range "+str(ip1)+"-"+str(ip2)+"\n"
	while whBool:
		userCh = raw_input("Please choose one of the following options:\n 1-Scan a specific port | 2-Scan a few ports | 3-Scan all the ports\n")
		if str(userCh) == "1":
			port = raw_input("Pick the number of the port you'd like to scan\n")
			portScanner.scan(ip1,ip2,[int(port)])
			whBool = 0
		elif str(userCh) == "2":
			port = 0
			ports = []
			while port != "-1":
				port = raw_input("Input the numbers of the chosen ports with Enter in between, input -1 to end the list\n")
				if port != "-1":				
					ports.append(int(port))
			portScanner.scan(ip1,ip2,ports)
			whBool = 0
		elif str(userCh) == "3":
			ports = range(0,65536)
			portScanner.scan(ip1,ip2,ports)
			whBool = 0
		elif whBool == 1:
			print "You've not chosed a proper response, try again\n"
	

# --------------------------------------------------------------#
#stupid way to fix the format, this is a bandaidfix thought of too late into the work
# --------------------------------------------------------------#
def strU(str1):
	return str(str1).strip("[u'").strip("']")


# --------------------------------------------------------------#
# A run command for the UI
# --------------------------------------------------------------#
def runUI(list):
	print "Hello and welcome to the least user friendly country based port scanner in existence."
	name = raw_input("What's your name bugger?\n")
	print "Hello there " + name
	countryNum = -1
	while countryNum == -1:
		choice = raw_input("Now you can either search a country, and then you are just welcome to type it's name in, or if you'd rather see the whole list - type in the number '1'\n")
		countryNum = countryChoice(list,choice)
	ipUI(list, countryNum)

