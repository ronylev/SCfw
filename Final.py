#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib
import tableUp
import UI
import subDom
#includes countryUpdate(list), ipTable(data, country), ipUpdate(list, country), ownerUpdate(line) and runUi(list)


def run(list):
	tool = raw_input("We have updated the program with a new tool! If you'd like the old country tool press 1, if you'd like the new subdomain tool press 2.")
 	if tool == "1":
		tableUp.countryUpdate(list)
		UI.runUI(list)
	elif tool == "2":
		subDom.domCh()
	else:
		print "choose a proper number."
		run(list)


list = []
run(list)



