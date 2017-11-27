#!/usr/bin/env python
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

def pythonStarter(intputFile, outputFileDir, totalWindowLength):
    subprocess.call("python3_ML/3.6.1")
    subprocess.call("./pipeline " + intputFile + outputFileDir + totalWindowLength)
    
def pythonVersionCheck(intputFile, outputFileDir, totalWindowLength):
    if(sys.version_info[0] == 3):
        import importlib as lib
        if(lib.find_loader('mutation_motif') is None):
            print("\nPlease install mutation motif module or module load the Morrell Lab version of python 3.6.1.\n")
            # print("With this command and try again: " + "module load python3_ML/3.6.1\n")
            print("loading Morrell Lab version of Python 3.6.1 module...\n")
            pythonStarter(intputFile, outputFileDir, totalWindowLength)
    elif(sys.version_info[0] == 2):
        import pkgutil as lib
        if(lib.find_loader('mutation_motif') is None):
            print("\nPlease install mutation motif module or module load the Morrell Lab version of python 3.6.1.\n")
            # print("With this command and try again: " + "module load python3_ML/3.6.1\n")
            print("loading Morrell Lab version of Python 3.6.1 module...\n")
            pythonStarter(intputFile, outputFileDir, totalWindowLength)

def start():
    fileIO = 0
    totalWindowLength = 0
    intputFile = None
    outputFileDir = None
    for x in range(len(sys.argv[0:])):
        argInput = sys.argv[x]
        path = os.path.isfile(argInput)
        if(path == True):
            if((fileIO == 0) and (argInput.endswith('.vcf')) or (argInput.endswith('.fasta'))):
                intputFile = argInput
                fileIO += 1
            elif(fileIO == 1):
                outputFileDir = argInput
                fileIO += 1
        if((type(argInput) == str) and (path != False)): #clean this up, only have one argument fo rwindow length, choose the lenght on both ends. ALSO CHECK ON HOW TO CHECK IF OBJECT IS A STRING!!!
            totalWindowLength = argInput
    if(fileIO < 2):
        outputFileDir = intputFile
    if(fileIO == 0):
        print("\nNo file or working directory specified.\n")
    elif(__name__ == '__main__'):
        main(intputFile, outputFileDir, totalWindowLength)

def fileConvert(inputFile, outputFileDir):
    now = datetime.datetime.now()
    dateTime = (now.strftime("%Y-%m-%d %H:%M:%S"))
    output = False
    if(inputFile.endswith('.vcf')):
        subprocess.call("vcf2bed <" + inputFile + " >" + outputFileDir + "ouput_" + dateTime + ".bed") #calls Bedops and input directory path from args //CHECK IF THEY WANT THE FILE SORTED AND BROKEN APART
        print("\nVCF to BED conversion complete.\n")
        output = True
        return(output)
    elif(inputFile.endswith('.fasta')):
        subprocess.call("") #calls Bedtool and input directory path from args
        print("\nBED to FASTA conversion complete.\n")
        output = True
        return(output)        
    print("\nFile conversion FAILED... Check extension.\n")
    return(output)

def main(intputFile, outputFileDir, totalWindowLength):
    try:
        pythonVersionCheck(intputFile, outputFileDir, totalWindowLength)
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
