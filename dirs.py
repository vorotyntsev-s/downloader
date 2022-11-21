import os
import glob

file = glob.glob("./*/**", recursive=True)

for f in file:
    if os.path.isdir(f):
        dirs = open('dirs.txt', 'a')
        dirs.write(f)
        dirs.write('\n')
    else:
        continue
