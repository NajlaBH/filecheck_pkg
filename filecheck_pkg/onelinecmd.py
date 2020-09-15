# filecheck_pkg/onelinecmd.py

from filecheck_pkg.screenit.headerfooter import *
from filecheck_pkg.argmanage.checkentries import *


import argparse



def launch_it():
    #""" Launch the filecheck_pkg """
    #Header
    headerdata = console_header()
    NAME = headerdata[0]
    VERSION = headerdata[1]

    #Arg call
    parser = argparse.ArgumentParser()
    parser.add_argument("username", type=str, help="Script user.")
    parser.add_argument("indir", type=str, help="input dir with file to check.")
    parser.add_argument("outdir", type=str, help="output dir for report edition.")
    parser.parse_args()
    if (len(sys.argv) < 4):
        print("you have ommitted an argument")
        print ("Please put the right arguments and try again :)")
        sys.exit('Usage: python %s --help' % sys.argv[0])

    elif (len(sys.argv) == 4):
        username = sys.argv[1]
        indir = sys.argv[2]
        outdir = sys.argv[3]

        print("\n************************************************")
        print("Hello " + username + " from NajlaBH !! ")
        print("************************************************")
        
        #Input dir
        print("InputDir : " + indir)
        if isitdir(indir)==True:
            print("OK: Correct Path")
            if len(os.listdir(indir))== 0:
                print("Your directory is empty put some data and try again :) !!")
            else:
                
                print("OK: " + str(len([f for f in os.listdir(indir)if os.path.isfile(os.path.join(indir, f))])) + " files ready for chek ;) !!")

        else:
            #print (indir)
            print("Please check your path")
            sys.exit()
        #Output dir
        print("OutputDir: " + outdir)
        if isitdir(outdir) == False:
            #print(outdir)
            createdir(outdir)
        else:
            print("OK: Correct Path")

        #Project
        print("File integrity checking .....BEGIN")
        dic_files = check_file_integrity(indir, outdir)
        print("File integrity checking .....END")

        print("Report editing .....BEGIN")
        report_edition(outdir,username,dic_files)
        print("Report editing .....END")

        print("************************************************\n")
    
    else:
        print ("Please put the right arguments and try again :)")
        sys.exit('Usage: python %s --help' % sys.argv[0])
    
    #Footer
    print("--------------------------------------------------------------------------------------------")
    print("Thank you for using " + NAME +" package " +  VERSION + "\nMore infos : bhndevtools@gmail.com")
    print("--------------------------------------------------------------------------------------------")



# Launch one line cmd script
launch_it()
