# filecheck_pkg/console.py

from filecheck_pkg.argmanage.clickconsole import *
from filecheck_pkg.screenit.headerfooter import *


def main():
    """ Launch the filecheck_pkg """
    #Header
    console_header()

    #Arg call
    click_console()

    #Footer
    console_footer()

if __name__ == "__main__":
    main()
