#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate Pleiades JSON
"""

import argparse
import os
import sys
import traceback
import logging as l

from pleiades.serialization import pcsv, pjson

SCRIPT_DESC = 'Generates new-fangled Pleiades JSON from Pleiades CSV dumps'

def main ():

    global args

    if args.verbose:
        l.basicConfig(level=l.DEBUG)
    else:
        l.basicConfig(level=l.WARNING)

    pd = pcsv.PleiadesDump('data/pleiades-places-latest.csv')
    nd = pcsv.PleiadesDump('data/pleiades-names-latest.csv')
    ld = pcsv.PleiadesDump('data/pleiades-locations-latest.csv')
    for datum in pd.data:
        p = pjson.PLACEJSON(datum, nd, ld)
        p.write('data/output/json')





if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description=SCRIPT_DESC, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument ("-v", "--verbose", action="store_true", default=False, help="verbose output")
        args = parser.parse_args()
        main()
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print "ERROR, UNEXPECTED EXCEPTION"
        print str(e)
        traceback.print_exc()
        os._exit(1)
