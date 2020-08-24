# -*- coding: utf-8 -*-

# '''run "python ETLCTL.py D:\Projects\untitled\flag db_UPS_200310 D:\Projects\untitled\log log.txt 2 6100" for testing'''

import sys, os
import time
from etlmodules.logger import Logger, log

start_time = time.time()

logger = Logger('main').getlog()
print(logger)
def ETLN2(FLAGDIR, DBFLAG, LOGDIR, LOGFILE, PROCNUM, BANK):
    pass


if __name__ == "__main__":
    ETLN2(sys.argv[1].strip(), sys.argv[2].strip(), sys.argv[3].strip(), sys.argv[4].strip(), sys.argv[5].strip(), sys.argv[6].strip(), )