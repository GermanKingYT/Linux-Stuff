#! /usr/bin/python
import subprocess
import argparse
import sys

UNKNOWN = 3
OK = 0
WARNING = 1
CRITICAL = 2

def get_arguments():
    parser = argparse.ArgumentParser(description='Get total processes in system')
    parser.add_argument("--warning", "-w", type=int, default=False, help="Warning processes count", required=True)
    parser.add_argument("--critical", "-c", type=int, default=False, help="Critical processes count", required=True)
    args = parser.parse_args()
    args = vars(args)
    return args


def get_process_count():	
	return int(subprocess.check_output('ps ax | wc -l',shell=True))


args = get_arguments()
process_count = get_process_count()

if process_count >= args['critical']:
    print "CRITICAL: " + str(process_count) + ' processes'
    sys.exit(2)

if process_count >= args['warning'] and process_count < args['critical']:
    print "WARNING: " + str(process_count) + ' processes'
    sys.exit(1)
else:
    print "OK: " + str(process_count) + ' processes'
    sys.exit(0)