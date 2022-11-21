import wget
import os
import hash

url = 'http://192.168.1.51:8081/'

if os.path.isfile('revision_local.txt') != True:
    file2 = open('revision_local.txt', 'w')


def make_dirs():
    wget.download(f'{url}dirs.txt')
    lst = []
    d = open('dirs.txt', 'r')
    for i in d.readlines():
        lst.append(i[0:-1])
    for j in lst[1:]:
        if os.path.isdir(j):
            continue
        else:
            os.makedirs(j)
    os.remove('./dirs.txt')


wget.download(f'{url}/revision_srv.txt')
make_dirs()
import comparison
os.remove('revision_srv.txt')
hash.get_hash()