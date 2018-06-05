#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib
website = "http://nirsoft.net/countryip"
#---------------------------------------------------------------#
# making a list of allcountries and their links
# --------------------------------------------------------------#
def countryUpdate(list):
	global website
	countryIpUrl = urllib.urlopen(website)
	site = countryIpUrl.read()
	soup = BeautifulSoup(site,'lxml')
	flag = 0
	for link in soup.find_all('a'):
		if link.get_text() == "Afghanistan":
			flag = 1
		if flag:
			if str(link.contents)[1] == 'u':
				list.append((link.contents,link.get('href'),[]))

# --------------------------------------------------------------#
#getting the ips for a chosen country
# --------------------------------------------------------------#
def ipTable(list,data, country):
	url = urllib.urlopen(website+"/"+list[country][1])
	site = url.read()
	soup = BeautifulSoup(site,'lxml')
	table = soup.find('table',attrs = {'':''})
	table_body = table.find('table')
	rows  = table.find_all('tr')
	flag1 = -3
	for row in rows:
		if flag1 > 0:	
			cols = row.find_all('td')
			cols = [ele.text.strip() for ele in cols]
			data.append([ele for ele in cols if ele])
		if flag1 == 0:
			flag1 = flag1 + 1
		if row.get_text().find('Major IP Address Blocks For') != -1:
			flag1 = flag1 + 1
# --------------------------------------------------------------#
#chosing a country for an ip update
# --------------------------------------------------------------#
def ipUpdate(list, country):
	coNum = 0
	for line in list:
		if line[0] == country:
			ipTable(list,line[2], coNum)
			break
		coNum = coNum + 1
# --------------------------------------------------------------#
#updating missing owners in the ip table
# --------------------------------------------------------------#
def ownerUpdate(line):
	try:
		own = line[4]
	except:
		url = urllib.urlopen("https://www.whois.com/whois/"+str(line[0]))
		site = url.read()
		spSite = site.split()
		flag = 0
		owner = ""
		for word in spSite:
			if flag:
				if word.find(":") == -1:
					owner = owner + word + " "
				else:
					break
			if word == "descr:" or word == "owner:":
				flag = 1
		line.append(owner.encode("UTF-8"))
