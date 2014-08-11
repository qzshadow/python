# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 12:26:19 2014

@author: ZhouQin
"""

import sys
import os
import chardet

def getFilesInDir(rootDir):
    listDirs = os.walk(rootDir)
    fileList = []
    for root, dirs, files in listDirs:
        for f in files:
            fileList.append(f)
    return fileList

def FilterFile(fileList,extList):
    files = []
    for file in fileList:
        if os.path.splitext(file)[1] in extList:
            files.append(file)
    return files
    

def removeTempFiles(extList,rootDir):
#    os.system('cd %s' % rootDir)
#    for ext in extList:
#        os.system('rm *.%s' % ext)
    files = getFilesInDir(rootDir)
    tempFile = FilterFile(files,extList)
    for file in tempFile:
        os.system('rm %s%s' % (rootDir,file))
    return 0
      
#TODO chardet module didnot support windows platforms
def getEncode(fileList,rootDir):
    fileEncode = {}
    for file in fileList:
        fileEncode[file] = chardet.detect(\
        open('%s%s' % (rootDir,file),'r').read())
    return fileEncode
    
    
def main():
    files = getFilesInDir('F:\\workspace\\temp')
#    print files
    files2 = FilterFile(files,['.m','.txt'])
#    removeTempFiles(['.m~','.asv'],'F:/workspace/temp/')
    print getEncode(files2,'F:/workspace/temp')
    
if __name__ == '__main__':
    main()