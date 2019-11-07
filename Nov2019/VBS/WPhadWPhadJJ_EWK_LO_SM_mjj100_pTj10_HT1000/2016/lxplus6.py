#!/usr/bin/env python

#import os,sys
from subprocess import call, check_output
import re
import threading
import time

from optparse import OptionParser, OptionGroup

usage = "usage: %prog [options] exe1 exe2 ..."
parser=OptionParser(usage=usage)
parser.add_option("-c","--ncore" ,dest='ncore',type='int',help="Number of core per server [Default=%default]",default=1)
parser.add_option("-n","--nserver" ,dest='nserver',type='int',help="Number of server to use [Default=%default]",default=10)
parser.add_option("-r","--regexp" ,dest='regexp',type='string',help="Regular expression to apply to the exe, comma separated, if not null [Default=%default]",default='')
parser.add_option("-x","--exe",dest="exe",type='string',help='executable. args will be the arguments [%default]',default='')
(opts,args)=parser.parse_args()


def scout():
	''' scout lxplus servers '''
	servers={}
	host = "host lxplus6.cern.ch | grep 'has address' | cut -d' ' -f 4 | while read ip ; do host $ip | sed 's/.*pointer //' | sed 's/\.$//'; done "
	hosts = check_output(host, shell=True)
	for l in hosts.split():
		servers[ l ] = 0
	return servers
def PrintServers(servers):
	print "I found the following lxplus:"
	for s in servers:
		print "\t*",s
	print "You want to run on", opts.nserver, "servers and I found ", len(servers)

def MergeDict(dict1,dict2):
	for key in dict2:
		if key not in dict1: dict1[key] = dict2[key]

servers=scout()

PrintServers(servers)
raw_input("Is ok?")

def call_exe(exe,server):
	if opts.regexp != "" :exe = re.sub(opts.regexp.split(',')[0], opts.regexp.split(',')[1],exe)
	if opts.exe != "": 
	    cmd = "ssh " + server + ' bash -l -c ' + opts.exe  + ' ' + exe 
	    print " -> Calling " + opts.exe + ' ' + exe + " on [" +server+"]"
	else:
	    cmd = "ssh " + server + ' bash -l -c "' + exe + ' "'
	    print " -> Calling "+ exe + " on [" +server+"]"
	#call(exe,shell=True)
	call(cmd,shell=True)
	print " -> Done "+exe
	servers[server] -= 1  ## not completely thread safe if multicore


threads=[]

for exe in args:
	server = ""
	## don't send too many job to a single lxplus
	while server == "":
		while threading.activeCount() >= opts.nserver*opts.ncore: 
			print "sleep ...",
			time.sleep(3)
			print "wake up"
		for s in servers: 
			if  servers[s] < opts.ncore : 
				server = s
				servers[s] = 1
				break

	t = threading.Thread(target=call_exe, args= (exe,server)  )
	t.start()
	threads.append( t )

for t in threads:
	t.join()

print " ************* Done ***************"

