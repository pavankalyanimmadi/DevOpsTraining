'''
Created on Oct 8, 2020

@author: Immadi pavan kalyan
'''

def printTable(tableData):
    insidelist=tableData[0];
    for y in range(len(insidelist)):
        line="";
        for x in range(len(tableData)):
            line+=tableData[x][y]+" ";  
        
        print(line);
    
    


tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']];
 
printTable(tableData);