'''
Created on Oct 8, 2020

@author: Immadi pavan kalyan
'''



gridvalue = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]


insidelistLength=gridvalue[0];

for y in range(len(insidelistLength)):
    line="";
    for x in range(len(gridvalue)):
        line+=gridvalue[x][y]; 
        
    print(line);
        
    