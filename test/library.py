### THIS IS A PYTHON LIBRARY FOR BATCH
from glob import glob
import sys,os,re
from subprocess import call, check_output

EOS = "/afs/cern.ch/project/eos/installation/0.3.84-aquamarine/bin/eos.select"

def PrintLine(list):
        ''' convert list in list of int number, sort and compress consecutive numbers. Then print the result:
        4,5,8,3 -> 3-5,8
        '''
        nums = [ int(s) for s in list ]
        nums.sort()
        compress = []
        last = None
        blockinit = None

        for n in nums:
                #first if it is not consecutive
                if last == None: ## INIT
                        blockinit = n

                elif last != n-1:
                        #close a block and open a new one
                        if last != blockinit:
                                compress.append( str(blockinit) + "-" + str(last) )
                        else:
                                compress.append( str(last) )
                        blockinit = n

                last = n

        #consider also the last number
        #close a block and open a new one
        if last != blockinit:
                compress.append( str(blockinit) + "-" + str(last) )
        else:
                compress.append( str(last) )

        return ",".join(compress)

def PrintSummary(dir, doPrint=True):
        ''' Print summary informations for dir. uses the .run .done .fail files.
	'''
	if dir[-1] == '/' : dir = dir[:-1]
        run  = glob(dir + "/*run")
        fail = glob(dir + "/*fail")
        done = glob(dir + "/*done")
	pend = glob(dir + "/*pend") 
	#pend = int(check_output( "bjobs -w | grep '%s' | grep PEND | wc -l "%dir, shell=True))

        ## bash color string
        red="\033[01;31m"
        green = "\033[01;32m"
        yellow = "\033[01;33m"
        cyan = "\033[01;36m"
        white = "\033[00m"

        run = [ re.sub('\.run','' , re.sub('.*/sub_','', r) ) for r in run ]
        fail = [ re.sub('\.fail','' , re.sub('.*/sub_','', r) ) for r in fail ]
        done = [ re.sub('\.done','' , re.sub('.*/sub_','', r) ) for r in done ]
        pend = [ re.sub('\.pend','' , re.sub('.*/sub_','', r) ) for r in pend ]

        tot = len(run) + len(fail) + len(done) + len(pend)

        color = red
        if len(run) > len(fail) and len(run) > len(pend) : color= yellow
        if len(pend) > len(fail) and len(pend) > len(run) : color= cyan
        if len(done) == tot and tot >0 : color = green

        if doPrint:
                print " ----  Directory "+ color+dir+white+" --------"
		print " Pend: " + yellow + "%3d"%len(pend)  + " / " + str(tot) + white + " : " + PrintLine(pend) 
                print " Run : " + yellow + "%3d"%len(run) + " / "  + str(tot) + white + " : " + PrintLine(run)  ### + ",".join(run)  + "|" 
                print " Fail: " + red    + "%3d"%len(fail) + " / " + str(tot) + white + " : " + PrintLine(fail) ### + ",".join(fail) + "|" 
                print " Done: " + green  + "%3d"%len(done) + " / " + str(tot) + white + " : " + PrintLine(done) ### + ",".join(done) + "|" 
                print " -------------------------------------"

        return ( done, run, fail)

def chunks(l, n):
    """ Yield successive n-sized chunks from l.
    """
    for i in xrange(0, len(l), n):
        yield l[i:i+n]

def chunksNum( l, tot):
    """ Yield successive n-sized chunks form l, in total number tot"""
    if len(l) % tot == 0:
        ChunkSize = len(l) / tot
    else:
        ChunkSize = (len(l) / tot) + 1
    return chunks(l,ChunkSize)


def CheckDir(dir):
	''' Return 0 if directory exists and is not empty. If it is empty delete it'''
	cmd = "[ -d "+ dir+" ]"
	status = call( cmd , shell=True)
	if status == 0:
        	print "Directory",dir,"already exists"
        	cmd =  "rmdir " + dir
        	status = call(cmd, shell = True)
		if status !=0 : return status;
		cmd = "[ -d "+ dir+" ]"
		status = call( cmd , shell=True)
	return status

def MkDir(dir):
	## creating a working directory
	cmd = ["mkdir","-p", dir]
	call(cmd)

def GetEosFileList(eos):
	cmd = EOS+ " find -f " + eos
	print "Going to call cmd:",cmd
	outputList = check_output(cmd,shell=True)
	fileList0 = outputList.split() ## change lines into list
	fileList = [ '"' + re.sub("/eos/cms","",f) +'"' for f in fileList0 ]
	return fileList

### why not a db class ?
def ReadFromDataBase(dbName,fileList):
	''' Read from Database, and update file list, removing already submitted jobs. Gives the offset with respect to the existing jobs'''
	## jobN file
	database = open(dbName,"a")
	db = {}
	maxn = -1
	fileSubmitted = []
	for line in database:	
		l = line.split('#')[0]
		if len(l) <2 : continue
		n = int(l.split()[0])
		f = l.split()[1]
		if n not in db: db[n] = []
		db[n].append(f)
		if n>maxn: maxn = n;
		fileSubmitted.append(f)
	fileList_tmp = [ f for f in fileList if f not in fileSubmitted ]
	fileList = fileList_tmp[:]
	maxn += 1
	database.close()
	return (maxn, fileList)
	
def WriteIntoDatabase(dbName, idx, f):
	db =open(dbName,"a");
	db.write("%d %s\n"%(idx, f))
	db.close();

###################### SH WRITING ###############
### Why not write a class ?
def OpenSh( dir, idx):
	shName = dir + "/sub_%d.sh"%idx
	sh = open( shName,"w") 
	sh.write("#!/bin/bash\n")
	call("chmod u+x "+ shName , shell=True)
	sh.write("cd %s\n"%os.environ['PWD'])
	sh.write("eval `scramv1 runtime -sh`\n") #cmsenv
	return (shName,sh)

def BeginJobStatusFiles( sh, dir,idx):
	call("touch "+os.environ['PWD']+"/"+dir+"/sub_"+str(idx) + ".pend\n",shell=True);
	sh.write("touch "+os.environ['PWD']+"/"+dir+"/sub_"+str(idx) + ".run\n")
	sh.write("rm "+os.environ['PWD']+"/"+dir+"/sub_"+str(idx) + ".done\n")
	sh.write("rm "+os.environ['PWD']+"/"+dir+"/sub_"+str(idx) + ".fail\n")
	sh.write("rm "+os.environ['PWD']+"/"+dir+"/sub_"+str(idx) + ".pend\n")
	return

def CdWorkDir(sh):
	sh.write('[ "${WORKDIR}" == "" ] && export WORKDIR=/tmp/$USER/ \n') ## make the script work on interactive lxplus
	sh.write('cd $WORKDIR \n' )

def CheckExitStatus(sh, Pipe=False):
	if Pipe:
		sh.write("EXIT=${PIPESTATUS[0]}\n")
	else:
		sh.write("EXIT=$?\n")

def EndJobStatusFiles(sh,dir,idx):
	sh.write("rm "+os.environ['PWD']+"/"+dir+"/sub_"+str(idx) + ".run\n")
	sh.write("[ \"${EXIT}\" == \"0\" ] && touch "+os.environ['PWD']+"/"+dir+"/sub_"+str(idx) + ".done\n")
	sh.write("[ \"${EXIT}\" == \"0\" ] || echo \"exit code : ${EXIT}\"> "+os.environ['PWD']+"/"+dir+"/sub_"+str(idx) + ".fail\n")
	return

def BsubCmd(queue,dir,idx):
	shName = dir + "/sub_%d.sh"%idx
	bsub = "bsub -q " + queue + " -J " + dir + "_"+str(idx) + " -o " + os.environ['PWD']+ "/" + dir+"/sub_"+str(idx) + ".log "
	bsub += os.environ['PWD'] + "/" + shName
	return bsub

### END SH ####
