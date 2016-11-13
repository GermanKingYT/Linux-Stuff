#!/usr/bin/env python

import getopt
import sys
import os

def usage():
	print """Usage: check_error_log -p path"""
	sys.exit(3)


def readfile(filename):
	if os.path.exists(filename):
		content = open(filename, "r").readlines()
		return int(content[0])
	else:
		return ""



def writefile(filename, data):
	file_obj = open(filename, 'w')
	file_obj.write("%s" % data)	


try:
    opts, args = getopt.getopt(sys.argv[1:],
        "p:", "path="
        )
except getopt.GetoptError:
    usage()
    sys.exit(2)

logfile = ""
savefile = "/tmp/check_error_log.dat"

for opt, arg in opts:
    if opt in ('-p', '--path'):
    	if not os.path.exists(arg):
			print "Log file not found\n"
			usage()
			sys.exit(2)
        else:
			logfile = arg        
    else:
        usage()
        sys.exit(2)    


f = open(logfile)
p = readfile(savefile)
if p == "":
	p = 0
f.seek(p)
latest_data = f.read()
p = f.tell()
if latest_data:
	print latest_data   
	writefile(savefile, p)
	sys.exit(2)
else:
	print "OK"
	sys.exit(0)
