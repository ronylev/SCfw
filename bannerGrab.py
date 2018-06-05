#!/usr/bin/python
import os
import socket
#[21,22,23,25,80,110]
#Banner grabbing upgrade. Had problems testing it.
def banGrab(s):
		banner = s.recv(1024)
		print ip + ':' + banner
	
