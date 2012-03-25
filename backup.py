#!/usr/bin/env python3

# This script is created by YoungUk Kim
# License: GNU GPL v3.0
# v.2012.03.25

import sys

if __name__ != '__main__' or len(sys.argv) != 2:
    print('Invalid run')
    sys.exit()

from subprocess import Popen
from os import waitpid
from os.path import normpath, exists, dirname

dest = normpath(sys.argv[1])

if not exists(dirname(dest)):
    print('Not exists destination')
    sys.exit()

srcList = [
        # Directory List
    ]

print('=== Backup Start ===')

for src in srcList:
    print('=== Start {} to {} ==='.format(src, dest))
    waitpid(Popen('rsync -az {} {}'.format(src, dest), shell=True).pid, 0)
    print('=== Finish {} to {} ==='.format(src, dest))

print('=== Backup finished ===')
