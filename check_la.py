#!/usr/bin/env python

import os
import sys
import getopt

def usage():
    print """Usage: check_getloadavg [-h|--help] [-m|--mode 1|2|3] \
    [-w|--warning level] [-c|--critical level]"

Mode: 1 - last minute ; 2 - last 5 minutes ; 3 - last 15 minutes"
Warning level defaults to 2.0
Critical level defaults to 5.0"""
    sys.exit(3)

try:
    options, args = getopt.getopt(sys.argv[1:],
        "hm:w:c:",
        "--help --mode= --warning= --critical=",
        )
except getopt.GetoptError:
    usage()
    sys.exit(3)

argMode = "1"
argWarning = 2.0
argCritical = 5.0

for name, value in options:
    if name in ("-h", "--help"):
        usage()
    if name in ("-m", "--mode"):
        if value not in ("1", "2", "3"):
            usage()
        argMode = value
    if name in ("-w", "--warning"):
        try:
            argWarning = 0.0 + value
        except Exception:
            print "Unable to convert to floating point value\n"
            usage()
    if name in ("-c", "--critical"):
        try:
            argCritical = 0.0 + value
        except Exception:
            print "Unable to convert to floating point value\n"
            usage()

try:
    (d1, d2, d3) = os.getloadavg()
except Exception:
    print "GETLOADAVG UNKNOWN: Error while getting load average"
    sys.exit(3)

if argMode == "1":
    d = d1
elif argMode == "2":
    d = d2
elif argMode == "3":
    d = d3

if d >= argCritical:
    print "CRITICAL: Load average is %.2f, %.2f, %.2f" % (d1, d2, d3)
    sys.exit(2)
elif d >= argWarning:
    print "WARNING: Load average is %.2f, %.2f, %.2f" % (d1, d2, d3)
    sys.exit(1)
else:
    print "OK: Load average is %.2f, %.2f, %.2f" % (d1, d2, d3)
    sys.exit(0)
