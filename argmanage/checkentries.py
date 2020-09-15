# filecheck_pkg/argmanage/checkentries.py

import os
import sys
from pathlib import Path


def isitdir(directory):
    if (os.path.isdir(directory)) == True:
        return  True
    else:
        return False

def createdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print("Please check your path")

def check_file_integrity(indir, outdir):
    """ Parse file in dir and check integrity """
    dic_files={}
    dic_param={}
    dic_integ={}
    for f in os.listdir(indir):
        if os.path.isfile(f)==True:
            print(f)
            dic_files[f]=dict_param
        else: 
            print (str(f) + "is a dir" )
    print(dic_files)