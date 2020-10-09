'''
Created on Oct 9, 2020

@author: immadi pavan kalyan
'''

import os;
import re;

print("specify path of directory");
Path=input();
Path = Path+"\\";

print("enter a regex to search ")
searchRegex=input();

filelist = os.listdir(Path);
for i in filelist:
    if i.endswith(".txt"):   
        with open(Path + i, 'r') as f:
            print("in "+i);
            count=0;
            print("--------------------------")
            for line in f:
                if(re.search(searchRegex,line)):
                    print(line);
                    count+=1;
            print("\nfounded in "+str(count)+" lines\n");
                    
                
                
                
            
                