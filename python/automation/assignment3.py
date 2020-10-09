'''
Created on Oct 9, 2020

@author: immadi pavan kalyan
'''

import re;

file1= open(r"C:\Users\lenovo\Desktop\python\test.txt", "r");

readedData=file1.read();
file1.close();


wordsToBeReplaced=re.findall(r"[A-Z]{2,}",readedData);
newReplacableWords=[];

for x in wordsToBeReplaced:
    print("enter a "+x);
    newReplacableWords.append(input());
    
updatedData=readedData;
    
for i in range(len(wordsToBeReplaced)):
    updatedData=re.sub(wordsToBeReplaced[i],newReplacableWords[i], updatedData, 1);
    
    
file2=open(r"C:\Users\lenovo\Desktop\python\newupdatedfile.txt","w");
file2.write(updatedData);
file2.close();


print("actual file data :");
print("-----------------------------------")
print(readedData);
print("\nnew updated data ");
print("-----------------------------------")
print(updatedData);
