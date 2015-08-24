cmsDriver.py step3 --filein file:step2.root  \
	--fileout file:step3.root --mc \
	--eventcontent MINIAODSIM  \
	--runUnscheduled --datatier MINIAODSIM  \
	--conditions MCRUN2_74_V9  \
	--step PAT \
	--python_filename step3.py  \
	--customise Configuration/DataProcessing/Utils.addMonitoring \
	-n -1
