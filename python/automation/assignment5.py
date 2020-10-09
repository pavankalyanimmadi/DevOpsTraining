'''
Created on Oct 9, 2020

@author: immadi pavan kalyan
'''

import os;
import shutil;
 
print("enter SOURCE directory path from which you want copy files")
sourcePath=input();
sourcePath+="\\"

print("enter DESTINATION folder to which you want copy files");
destinationPath=input();
destinationPath+="\\"

filesList=os.listdir(sourcePath);
count=0;

for i in filesList:
    if i.endswith(".txt") or i.endswith(".jpg") :
        count+=1;
        shutil.copy(sourcePath+i, destinationPath)
        
        
        
print("number of files moved : "+str(count))
        
