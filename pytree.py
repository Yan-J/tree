#!/usr/bin/env python3
import subprocess
import sys
import os
import string

def printDir(path, layer, file_cnt, dir_cnt):
    if (path[-1]!= '/'):
        path = path + '/'
    curList = sorted(os.listdir(path))
    cnt = []
    for i in curList:
        if (i[0]!='.'):
            if (i == curList[-1]):
                f_name = '└── ' + i
            else:
                f_name = '├── ' + i
            for l in range(0, layer):
                f_name = '    ' + f_name
            print(f_name)
            curPath = path + i
            if (os.path.isdir(curPath)):
                curPath = curPath + '/'
                dir_cnt = dir_cnt + 1
                cnt1 = printDir(curPath, layer+1, file_cnt, dir_cnt)
                file_cnt = cnt1[1]
                dir_cnt = cnt1[0]
            elif (os.path.isfile(curPath)):
                file_cnt = file_cnt + 1
        else:
            pass
    cnt.append(dir_cnt)
    cnt.append(file_cnt)
    return cnt
if (len(sys.argv) == 1):
    path = '.'
elif (len(sys.argv) == 2):
    path = sys.argv[1]
print(path)
cnt = printDir(path, 0, 0, 0)
print(str(cnt[0]) + ' directories', str(cnt[1]) + ' files')
if __name__ == '__main__':
    # just for demo
    subprocess.run(['tree'] + sys.argv[1:])
