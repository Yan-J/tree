#!/usr/bin/env python3
import subprocess
import sys
import os
import string
import re

def printDir(path, file_cnt, dir_cnt,indent=''):
    if (path[-1] != '/'):
        path = path + '/'
    curList = os.listdir(path)
    curList = [item for item in curList if item[0] != '.']#remove hidden files
    curList = sorted(curList, key=str.lower)
    cnt = []
    for i in curList:
        curPath = path + i
        if (os.path.isdir(curPath) and i == curList[-1]):
            curPath = curPath + '/'
            dir_cnt = dir_cnt + 1
            print(indent + '└── ' + str(i))
            indent1 = indent + '    '
            cnt1 = printDir(curPath, file_cnt, dir_cnt, indent1)
            file_cnt = cnt1[1]
            dir_cnt = cnt1[0]
        elif (os.path.isdir(curPath) and i != curList[-1]):
            curPath = curPath + '/'
            dir_cnt = dir_cnt + 1
            print(indent + '├── ' + str(i))
            indent1 = indent + '│   '
            cnt1 = printDir(curPath, file_cnt, dir_cnt, indent1)
            file_cnt = cnt1[1]
            dir_cnt = cnt1[0]
        elif (os.path.isfile(curPath) and i == curList[-1]):
            print(indent + '└── ' + str(i))
            file_cnt = file_cnt + 1
        elif (os.path.isfile(curPath) and i != curList[-1]):
            print(indent + '├── ' + str(i))
            file_cnt = file_cnt + 1    
    cnt.append(dir_cnt)
    cnt.append(file_cnt)
    return cnt

if __name__ == '__main__':
    if (len(sys.argv) == 1):
        path = '.'
    elif (len(sys.argv) == 2):
        path = sys.argv[1]
    print(path)
    cnt = printDir(path, 0, 0, '')
    print()
    print(str(cnt[0]) + ' directories', str(cnt[1]) + ' files')
