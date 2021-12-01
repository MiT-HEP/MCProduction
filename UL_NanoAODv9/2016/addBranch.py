from __future__ import print_function
import sys,os
import numpy as np
from subprocess import call, check_output

from optparse import OptionParser
parser=OptionParser()
parser.add_option("-f","--file",dest="files",type="string",help="Input file (nanoAOD). Specials: JSON num, PARENT (use the list below instead of figuring out with das)",default=[],action='append')
parser.add_option("-p","--parents",dest="parents",type="string",help="Parent files (force, default figure it out)",default=[],action='append')
parser.add_option("-u","--output",dest="output",type="string",help="Output file to update (nanoAOD) [%default]",default="nano.root")
parser.add_option("-a","--add",dest="names",type="string",help="add weight name,pos",default=[],action='append')
parser.add_option("","--minME",type="string",help="figure out names from min and max",default=None)
parser.add_option("","--maxME",type="string",help="figure out names from min and max",default=None)
parser.add_option("-x","--xrdcp",dest="xrdcp",action="store_true",help="Use first xrdcp",default=False)
parser.add_option("","--persistent_temp",dest="persistent_temp",help="Persistent temp directory",default=None)
parser.add_option("-v","--verbose",dest="verbose",type="int",help="Verbose [%default]",default=1)
opts, args=parser.parse_args()

## re-handle file in json format. These are the original nanoAOD, will use edm/das tools to convert it to miniAOD
if opts.files[0] == 'JSON':
    jobNum = int(opts.files[1])
    #job_input_file_list_12
    import json
    with open('job_input_file_list_%d.txt'%jobNum) as fin:
        data=json.load(fin)
        opts.files=[f if 'root://' in f else 'root://xrootd-cms.infn.it//' + f for f in data]
    print ("JSON 'job_input_file_list_%d.txt' changed file list to: "%jobNum,','.join(opts.files))

# import root in batch mode
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

## c++ data formats
from array import array

# load FWLite C++ libraries
ROOT.gSystem.Load("libFWCoreFWLite.so");
ROOT.gSystem.Load("libDataFormatsFWLite.so");
ROOT.FWLiteEnabler.enable()

# load FWlite python libraries
from DataFormats.FWLite import Handle, Events

names=[ (n,int(p)) for n,p in opts.names ] # output branch names, weight position
descr=None
weights={} #->run,lumi,evt  -> [values]

if opts.minME and len(names)>0: raise ValueError("Cannot specify minME and names simultaneously")

if opts.xrdcp:
    tmp=check_output(["mktemp","-d"]).replace('\n','') if opts.persistent_temp == None else opts.persistent_temp
    print ("temporary directory is",tmp)

for ifile,fnamenano in enumerate(opts.files):
    if fnamenano =='PARENT':
        parents=opts.parents
    else:
        fname_logical=fnamenano[fnamenano.find('/store'):]  
        #find parent
        cmd="dasgoclient -query 'parent file=%s'"%fname_logical
        print ("-> Parents fetch with command: "+ cmd)
        out=check_output(cmd,shell=True)

        #print ("DEBUG","CMD",cmd)
        #print ("DEBUG","out",out)

        parents = [ 'root://xrootd-cms.infn.it//' + x for x in out.split() if '/store/' in x ]
    print ("-> Runnig on ",fnamenano,"parents",','.join(parents))
    for ifile2,fname in enumerate(parents):
        if opts.xrdcp:
            need_transfer=True
            if opts.persistent_temp != None and os.path.isfile( tmp+"/"+fname.split('/')[-1] ) : need_transfer=False
            ## copy and swap fname
            cmd=['xrdcp',fname,tmp+"/"+fname.split('/')[-1] ]
            st=call(cmd) if need_transfer else 0
            if st !=0:  
                print ("DEBUG","CMD",' '.join(cmd))
                print ("DEBUG","status",st)
                raise RuntimeError("Unable to transfer file "+fname+" with xrdcp" )
            # now use local version
            fname=tmp+"/"+fname.split('/')[-1]
        print ("->Opening file",fname,"parent",ifile2,"/",len(parents), "of", fnamenano, ifile,"/",len(opts.files))
        events = Events(fname)
        lhe,lheLabel = Handle("LHEEventProduct"),"externalLHEProducer"

        for iev,event in enumerate(events):
            if event.eventAuxiliary().event() % 1000 ==1:
                print ("-> Event %d: run %6d, lumi %4d, event %12d" % (iev,event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event()))
            event.getByLabel(lheLabel, lhe)

            hepeup = lhe.product().hepeup()
            w=lhe.product().weights()[0].wgt

            if len(names) == 0: ## figure them out here
                foundMin=False
                foundMax=False
                for p in range(0,len(lhe.product().weights())):
                    if opts.minME in lhe.product().weights()[p].id: foundMin=True
                    if foundMin and not foundMax: names.append( (lhe.product().weights()[p].id, p) )
                    if opts.maxME in lhe.product().weights()[p].id: foundMax=True
                print ("names is now:", names)

            weights[ (event.eventAuxiliary().run(), event.eventAuxiliary().luminosityBlock(),event.eventAuxiliary().event() ) ] = [ lhe.product().weights()[p].wgt for n,p in names]
            if not descr: descr = [ lhe.product().weights()[p].id for n,p in names ] 
        if opts.xrdcp: #clean
            cmd=['rm','-v',fname]
            try:
                st=call(cmd)
            except OSError: 
                pass

print (">>","Opening",opts.output,"for R/W")
# Open Output in R/W and add a new branch
fout=ROOT.TFile.Open(opts.output,"UPDATE")
tree = fout.Get("Events")
values = []
branches=[]
for i,(n,p) in enumerate(names):
    values.append( array('d',[0.]) )
    b=tree.Branch(n,values[i],n+"/D")
    if descr: b.SetTitle(descr[i])
    branches.append(b)

## loop over entries
for i in range(0,tree.GetEntries()):
    tree.GetEntry(i)
    w = (tree.run, tree.luminosityBlock, tree.event)
    for i,(n,p) in enumerate(names):
        values[i][0] = weights[w][i] #if w in weights else -99. ### Raise Exception
        branches[i].Fill()
tree.Write("",ROOT.TObject.kOverwrite);

print (">>","Events tree Written")
print (">>","Computing Sums (Runs)")
# save sums
branches2=[]
values_sums=[] 
run_tree = fout.Get("Runs")
for i,(n,p) in enumerate(names):
    values_sums.append( array('d',[0.]))
    b=run_tree.Branch("sum_"+n,values_sums[i],"sum_"+n+"/D")
    values_sums[i][0] = np.sum([weights[w][i] for w in weights])
    if descr: b.SetTitle("sum of weights")
    b.Fill()
    branches2.append(b)
run_tree.Write("",ROOT.TObject.kOverwrite);

## close
fout.Close()
print (">>","Done. Exiting")
