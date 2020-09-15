#filecheck_pkg/screenit/headerfooter.py

import click
from . import __version__

from filecheck_pkg.argmanage.checkentries import *



def console_header():
    """ Print header """
    global NAME
    global VERSION
    global AUTHOR
    NAME="filecheck_pkg"
    VERSION="1.1.0"
    AUTHOR="NajlaBH"
    CREATION="12-SEP-20"
    UPDATE="15-SEP-20"
    DESCRIPTION="Python package for file integrity check"
    print("-----------------------------------------------------")
    print("Package Name: " + NAME)
    print("Author: " + AUTHOR)
    print("Creation: " + CREATION)
    print("LastUpdate: "+ UPDATE)
    print("Version: " + VERSION)
    print("Description:" + DESCRIPTION)
    print("-----------------------------------------------------\n")

    return NAME, VERSION



@click.command()
@click.version_option(version=__version__)
@click.option('--username', prompt='Your name', help='The person who launch the pkg.')
@click.option('--indir' , prompt='data source dir', help= 'Directory of files to check')
@click.option('--outdir', prompt='result dir', help='Directory to place the check report')

def console_footer(username,indir,outdir):
    #""" Print footer """

    print("\n************************************************")
    click.echo("Hello " + username + " from NajlaBH !! ")
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
        print("Please check your path")
        sys.exit()
    #Output dir
    print("OutputDir: " + outdir)
    if isitdir(outdir) == False:
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
       
    print("--------------------------------------------------------------------------------------------")
    print("Thank you for using " + NAME +" package " +  VERSION + "\nMore infos : bhndevtools@gmail.com")
    print("--------------------------------------------------------------------------------------------")

