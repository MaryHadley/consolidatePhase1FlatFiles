# consolidatePhase1FlatFiles

Tools to consolidate the many Phase1 flat files that come out of CRAB into a few big files that can be fed to the ntupilizer.

**Instructions**  
Main code is reduceNumOfPhase1FlatFiles.py. In this code, you will need to edit:  

chunksPerDir #Set this to some number you think is appropriate based on the number of files in the crab output directory  

outDir #Define a directory where you want your consolidated files to get written out to  

In the loopChunkAndHaddFilesInTheDir function, you will need to edit the number in the [] in theSuffix in order to get a good suffix. How many back you want this number to be depends on how long the name of the file output by Crab is (Would be better to standardize the output name, will try to do so in the future)  




