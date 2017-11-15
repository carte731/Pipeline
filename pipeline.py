#!/usr/bin/python
###File conversion V1.0

import os
import sys
import datetime
import time
import subprocess
from subprocess import call 
import logging

def initModLoad():
    subprocess.call("module load bedops_ML/2.4.20")
    subprocess.call("module load bedtools_ML/2.23.0")

def start():
    windowCounter = 0
    fileIO = 0
    leftWindow = 0
    rightWindow = 0
    totalWindowLength = 0
    intputFile = null
    outputFileDir = null
    for x in argv:
        argInput = sys.argv[x]
        path = os.path.isfile(argInput)
        if(path == true):
            if((fileIO == 0) and (argInput.endswith('.vcf')) or (argInput.endswith('.fasta'))):
                intputFile = argInput
                fileIO += 1
            else if(fileIO == 1):
                outputFileDir = argInput
                fileIO += 1
        if((argInput.type(int)) and (windowCounter == 0) and (path != False)):
            leftWindow = argInput
            windowCounter += 1
        if((argInput.type(int)) and (windowCounter == 1) and (path != False)):
            rightWindow = argInput
            totalWindowLength = leftWindow + rightWindow
    if(fileIO < 2):
        outputFileDir = intputFile
    if(fileIO == 0):
        print("\nNo file or working directory specified.\n")
    else if(__name__ == '__main__'):
        main(intputFile, outputFileDir, leftWindow, rightWindow, totalWindowLength)

def fileConvert(inputFile, outputFileDir):
    now = datetime.datetime.now()
    dateTime = (now.strftime("%Y-%m-%d %H:%M:%S"))
    output = False
    if(inputFile.endswith('.vcf')):
        subprocess.call("vcf2bed <" + inputFile + " >" + outputFileDir + "ouput_" + dateTime + ".bed") #calls Bedops and input directory path from args //CHECK IF THEY WANT THE FILE SORTED AND BROKEN APART
        print("\nVCF to BED conversion complete.\n")
        output = True
        return(output)
    else if(inputFile.endswith('.fasta')):
        subprocess.call("") #calls Bedtool and input directory path from args
        print("\nBED to FASTA conversion complete.\n")
        output = True
        return(output)        
    print("\nFile conversion FAILED... Check extension.\n")
    return(output)

def main(intputFile, outputFileDir, leftWindow, rightWindow, totalWindowLength):
    try:
        initModLoad()
        fileConvert(inputFile, outputFileDir)
    except(Exception) as error: #Logs crashes from the program
        now = datetime.datetime.now()
        sslog.write('\n')
        logging.basicConfig(filename=outputFileDir,filemode='a', format='%(msecs)d %(name)s %(levelname)s %(message)s', level=logging.DEBUG)
        logging.info('\n' + "PYTHON ERRORS: " + "\n" + (now.strftime("%Y-%m-%d %H:%M:%S")) + '\n' + '-----------')
        logger = logging.getLogger(__name__)
        logger.error(error, exc_info=True)

start() #Starts program