
# This module contains compatibility fixes for ubuntu 18.04
# - generally this means quick fixes to account for that distro having python version 3.6

import sys
if sys.version_info[0] < 3:
    raise Exception("Python 3 only")

from datetime import date

def date_from_iso_string(string):
    if sys.version_info.minor < 7:
        intlist = [ int(e) for e in string.split("-")]
        return date(*intlist)
    else:
        return date.fromisoformat(string)

