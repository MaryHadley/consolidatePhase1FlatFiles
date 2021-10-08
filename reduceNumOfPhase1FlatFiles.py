from __future__ import division
import ROOT
import os 
#from __future__ import division

#credit to: https://stackoverflow.com/questions/2130016/splitting-a-list-into-n-parts-of-approximately-equal-length
def chunkify(myList, numChunks):
    numChunks = min (numChunks, len(myList))
    if numChunks == 0:
        print "Why are you trying to make 0 chunks or trying to chunkify an empty list? That doesn't make sense. Exiting..."
        return 
    if len(myList)/numChunks == 1:
        print "Why are you trying to put all the files into one chunk? That doesn't make sense, if you wanted this, you wouldn't need to use this function to accomplish that. Exiting..."
        return 
    chunkSize, remainder = divmod (len(myList), numChunks)
    return (myList[i*chunkSize + min(i, remainder):(i+1)* chunkSize + min(i+1, remainder)] for i in range(numChunks))
    
    


##Proof of Concept, can comment out after testing 
#testList = range(10)
#print testList
#choppedUpList =  list(chunkify(testList,3)) #remember to do "list(chunkify(myList, numChunks))" to get the output as something useful!
#print "choppedUpList is:", choppedUpList


chunksPerDir = 3 #Set this to whatever you think is appropriate based on how many files in the directory 

outDir = 'out_justD_14Nov2020'
#outDir = 'scratch_14Nov2020'
if not os.path.exists(outDir):
    os.makedirs(outDir)

#Remember that SAFEPathToFiles must be written like this: '  root://cmseos.fnal.gov//store/user/mhadley/15June2020_lowpTTauPreprocessedSFlatNtuples/' 
#Those 2 spaces at the front are important!! Well, could be 1 space but I think 2 makes easier reading. Remember also the / at the end and the beginning are important
#Thanks Marguerite and David for reminding me of the SAFE path syntax for LPC EOS

def loopChunkAndHaddFilesInTheDir(pathToDir, SAFEPathToFiles):
    filesInTheDirList = [myF for myF in os.listdir(pathToDir) if os.path.isfile(os.path.join(pathToDir, myF))]
#    print "filesInTheDirList:", filesInTheDirList
    
    choppedUpList = list(chunkify(filesInTheDirList, chunksPerDir))
    print "choppedUpList:", choppedUpList
    
    theSuffix = pathToDir.replace('/', '-')[-48:] 
    print 'theSuffix:', theSuffix
    counter = 0
    for i in choppedUpList:
        print "i is:", i
        haddCommand = 'hadd  '  + outDir + '/bigFile_' + theSuffix + '_'   #might need to check this number
# Note the spaces at the end of the 'hadd   ' string, they are important
#       SAFEpathToFiles = '  /scatch2/'
        counter += 1
        print "counter is:", counter
        haddCommand += str(counter) + '.root'
        print haddCommand
        chunkInChoppedUpListList = list(i)
        print len(chunkInChoppedUpListList)
        if len(chunkInChoppedUpListList) ==1:
             print "There is a chunk that only has one file. This will cause a problem when hadding. Please set another value for chunksPerDir to avoid this. Exiting..."
             return 
        for el in chunkInChoppedUpListList: #el for element 
            print el
            haddCommand += SAFEPathToFiles + el 
        print haddCommand
        os.system(haddCommand)
    return #Careful with this indentation!!!! It needs to be at the same level as the "for i in choppedUpList"!!
#     

#print '/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018D_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018D_11Nov2020/201111_131251/0001'.replace('/', '-')[-48:]
#print '/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018A_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018A_11Nov2020/201111_131207/0000'.replace('/', '-')[-48:]
#theDict = {'/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018A_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018A_11Nov2020/201111_131207/0000': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018A_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018A_11Nov2020/201111_131207/0000/',}
#theDict = {'/uscms_data/d3/mhadley/consolidateFlatPhase1Samples_fromLPCEOS/CMSSW_10_6_2/src/LPCAnalysisUtilities/testDir/': '  /uscms_data/d3/mhadley/consolidateFlatPhase1Samples_fromLPCEOS/CMSSW_10_6_2/src/LPCAnalysisUtilities/testDir/'}

theDict = {#'/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018A_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018A_11Nov2020/201111_131207/0001': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018A_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018A_11Nov2020/201111_131207/0001/',
            #'/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018A_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018A_11Nov2020/201111_131207/0002': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018A_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018A_11Nov2020/201111_131207/0002/',
             
            # '/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018B_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018B_11Nov2020/201111_131222/0000/': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018B_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018B_11Nov2020/201111_131222/0000/',
             
            #  '/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018B_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018B_11Nov2020/201111_131222/0001/': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018B_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018B_11Nov2020/201111_131222/0001/',
              
            #  '/eos/uscms/store/user/mhadley/Zmuon_DataJobs_UL2018_DiMu_UL2018C_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018C_11Nov2020/201111_131236/0000': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_UL2018_DiMu_UL2018C_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018C_11Nov2020/201111_131236/0000/',
              
            # '/eos/uscms/store/user/mhadley/Zmuon_DataJobs_UL2018_DiMu_UL2018C_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018C_11Nov2020/201111_131236/0001': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_UL2018_DiMu_UL2018C_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018C_11Nov2020/201111_131236/0001/',
             
             '/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018D_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018D_11Nov2020/201111_131251/0000': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018D_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018D_11Nov2020/201111_131251/0000/',
             
              '/eos/uscms/store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018D_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018D_11Nov2020/201111_131251/0001': '  root://cmseos.fnal.gov//store/user/mhadley/Zmuon_DataJobs_DiMu_UL2018D_11Nov2020/DoubleMuon/crab_DoubleMuUL_Run2018D_11Nov2020/201111_131251/0001/',
             
             
              }


for key in theDict.keys():
    firstArg = key
    secondArg = theDict[key]
    print "PREPARING to hadd files in %s" %(firstArg)
    loopChunkAndHaddFilesInTheDir(firstArg, secondArg)
    print "DONE hadding files in %s" %(firstArg)
