# consolidatePhase1FlatFiles

Tools to consolidate the many Phase1 flat files that come out of CRAB into a few big files that can be fed to the ntupilizer.

**Instructions**  
Main code is reduceNumOfPhase1FlatFiles.py. In this code, you will need to edit:  

chunksPerDir #Set this to some number you think is appropriate based on the number of files in the crab output directory  

outDir #Define a directory where you want your consolidated files to get written out to  

You will need to add the paths to the files as key value pairs to theDict, where the key is the full path beginning with /eos and the value is the xrd safe way to access files, e.g. theDict = {
'/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018D_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018D_11Nov2020/201111_131251/0000/': '          root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018D_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018D_11Nov2020/201111_131251/0000/'} #Note the extra spaces between ' and root in the value, this is important! Note also the final / in the path names, this is critical!


