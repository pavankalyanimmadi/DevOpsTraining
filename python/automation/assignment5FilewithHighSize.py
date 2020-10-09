'''
Created on Oct 9, 2020

@author: immadi pavan kalyan

'''

import os;

print("enter directory path ")
sourcePath=input();
sourcePath+="\\"
fileList=os.listdir(sourcePath);

print(fileList)

for i in fileList:
    SizeOfFile=os.path.getsize(sourcePath+i)/1048576;
    if SizeOfFile > 100:
        print( sourcePath+i+ " --- "+str(os.path.getsize(sourcePath+i)/1048576) + "Mb");
