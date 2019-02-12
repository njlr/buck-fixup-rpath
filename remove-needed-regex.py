#!/usr/bin/env python

import sys
import re
from subprocess import Popen, PIPE

# 0. Help
if len(sys.argv) < 3:
  print 'Tool to remove needed shared libraries that match a regex. '
  print 'You will need to install patchelf. '
  print 'Usage: ' + sys.argv[0] +' <binary> <regexp>'
  print 'Example: ' + sys.argv[0] +' ./main \'^.*libtest.so$\' '
  sys.exit(1)

def call(prog):
  process = Popen(prog, stdout = PIPE)
  (output, err) = process.communicate()
  exit_code = process.wait()
  assert(exit_code == 0)
  return output

binary = sys.argv[1]
regex = sys.argv[2]

# 1. Extract the needed libraries
output = call([ 'patchelf', '--print-needed', binary ])

needed = [ x.strip() for x in output.splitlines() ]

print('The following libraries are needed: ' + str(needed))

# 2. For each needed that matches the regex, remove it
to_remove = [ x for x in needed if re.match(regex, x) ]

print('The following libraries will be removed: ' + str(to_remove))

for x in to_remove:
  print 'Removing ' + x
  call([ 'patchelf', '--remove-needed', x, binary ])

# 3. Show remaining libraries
output = call([ 'patchelf', '--print-needed', binary ])

print('The following libraries remain needed: ' + str(needed))

print 'Done.'
