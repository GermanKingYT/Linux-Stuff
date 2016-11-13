#! /usr/bin/python

import re
import commands
import sys

#################
#Set variables
command = "df /"
critical = 95.0
warning = 75.0
#################

#build regex
dfPattern = re.compile('[0-9]+')

#get disk utilization
diskUtil = commands.getstatusoutput(command)

#split out the util %
diskUtil = diskUtil[1].split()[11]

#look for a match. If no match exit and return an
#UNKNOWN (3) state to Nagios

matchobj = dfPattern.match(diskUtil)
if (matchobj):
    diskUtil = eval(matchobj.group(0))
else:
    print "STATE UNKNOWN"
    sys.exit(3)

#Determine state to pass to Nagios
#CRITICAL = 2
#WARNING = 1
#OK = 0
if diskUtil >= critical:
    print "CRITICAL: '/' is %.2f%% full" % (float(diskUtil))
    sys.exit(2)
elif diskUtil >= warning:
    print "WARNING: '/' is %.2f%% full" % (float(diskUtil))
    sys.exit(1)
else:
    print "OK: '/' is %.2f%% full" % (float(diskUtil))
    sys.exit(0)