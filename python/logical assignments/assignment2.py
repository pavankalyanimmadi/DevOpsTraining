'''
Created on Oct 8, 2020

@author: Immadi pavan kalyan
'''

def collatz(number):
    if number%2==0:
        result=number//2;
        print(result);
        return result;
    else:
        result=3*number+1;
        print(result);
        return result;
    


result=0;
while result!=1:
    try:
        print("enter a number");
        number=int(input());
        result=collatz(number);
        
    except:
        print("entered value must be an integer");
    

