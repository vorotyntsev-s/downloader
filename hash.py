import os
import glob
import hashlib


def get_hash():
    file = glob.glob("./*/**", recursive=True)
    for f in file:
        if os.path.isdir(f):
            continue
        else:
            with open(f, 'rb') as getsha256:
                data = getsha256.read()
                gethash = hashlib.sha256(data).hexdigest()
                print(f, gethash)
                revision = open('revision_local.txt', 'a')
                revision.writelines([gethash, '  ', f[1:]])
                revision.write('\n')



