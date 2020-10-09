'''
Created on Oct 9, 2020

@author: immadi pavan kalyan
'''
import re;

def myStrip(mainString, toBeRemoved=" "):
    if(toBeRemoved==" "):
        x=re.search("\w",mainString);
        startIndex=x.start();
        y=mainString.split();
        lastWord=y[len(y)-1];
        endingIndex=mainString.rfind(lastWord)+len(lastWord);
        
        return mainString[startIndex:endingIndex];
    
    else:
        updatedString="";
        charactersToBeRemoved=[]
        charactersToBeRemoved[:0]=toBeRemoved;
        for y in mainString: 
            if y not in charactersToBeRemoved:
                updatedString+=y;
                
        return updatedString;
                    
                    
        
        
        
        
print("with out arguments  : "+myStrip("        hii  this is pavan   "));
print("with arguments  :  "+myStrip("       hii this is pavan  ", "ai"));
        
        
        
        
        
        
    
