'''
Created on Oct 9, 2020

@author: immadi pavan kalyan

'''

import os;

print("enter directory path ")
sourcePath=input();
fileList=os.listdir(sourcePath+"\\");

noOfFiles=0;
noOfDirectories=0;

print(fileList);

for i in fileList:
    if os.path.isfile(sourcePath+i):
        sizeOfFile=os.path.getsize(sourcePath+i)/1048576
        sizeOfFile=round(sizeOfFile,2);
        if sizeOfFile > 100:
            print(sourcePath+i +" : "+str(sizeOfFile)+" Mb")
        
    if os.path.isdir(sourcePath+i):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(sourcePath+i):
            for f in filenames:
                fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        
        total_size=total_size/1048576
        if total_size>100:
            total_size=round(total_size,2)           
            print(sourcePath+i + " : "+ str(total_size)+ " Mb");

    

        

    
    