# filecheck_pkg/argmanage/checkentries.py

import os
import sys
from pathlib import Path
from filehash import FileHash
import datetime



def isitdir(directory):
    if (os.path.isdir(directory)) == True:
        return  True
    else:
        print("Please check your path")
        return False

def createdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("Your path dosen t exist , it will be created")
    else:
        print("OK: Your is correct.")



def check_file_integrity(indir, outdir):
    """ Parse file in dir and check integrity """
    dic_files={}
    dic_param={}
    dic_integ={}
    
    for f in os.listdir(indir):
        path= os.path.join(indir, f)
        #if os.path.isdir(path)==True:
        #    print (str(f) + "is a dir" )
        #elif os.path.isfile(path): 
        if os.path.isfile(path): 
            #dic_param['size']=Path(path).stat().st_size
            dic_param['size']=os.path.getsize(path)

            md5hasher = FileHash('md5')
            dic_param['md5']= md5hasher.hash_file(path)

            dic_files[f]=dic_param
            #print( f + " : It is a normal file") 
            
            #Reinitialize dict
            dic_param={}

        #else: 
        #    print(f + "It is a special file (socket, FIFO, device file)" )
    #print (dic_files)
    return dic_files


def report_edition(outdir,username,dic_files):
    NOW_DATE = str(datetime.datetime.now()).split(".")
    NOW =  NOW_DATE[0].replace(":","")
    
    report_path= outdir.rstrip("/") + "/FilesIntegrityReport"  + "_" + str(NOW).replace(" ","_")+".txt"
    print("Your report is here: " + report_path)
    
    with open(report_path, 'a') as f:
        f.write("UserName : " + username +"\n")
        f.write("FILENAME\tSIZE\tMD5HASH\n")
        for key,values in dic_files.items():
            linetoedit = key + "\t" + str(values['size']) + "\t" + str(values['md5']) + "\n"
            f.write(linetoedit)