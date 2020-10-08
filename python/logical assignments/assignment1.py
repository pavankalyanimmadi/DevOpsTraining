'''
Created on Oct 8, 2020

@author: immadi pavan kalyan
'''

#len() fucnrion testing

x="hiii"
sampleList=["hi","hello",1];
sampleDictionary={"apples":5,"bananas":10};

print("length of string : "+str(len(x)));
print("length of sample list : "+str(len(sampleList)));
print("length of sample dictionary : "+str((len(sampleDictionary))));
print("");



#round function testing

print("round value of 51.6 : "+str(round(51.6)));
print("round value of 51.4 : "+str(round(51.4)));
print("round value of 51.5 : "+str(round(51.5)));
print("round value of 2.665 to 2 decimals : "+str(round(2.665,2)));
print("")


  
# abs() built-in function 
  
# floating point number 
float = -54.26
print('Absolute value of float -54.26 is:', abs(float)) 
  
# An integer 
int = -94
print('Absolute value of integer -94 is:', abs(int)) 
  
# A complex number 
complex = (3 - 4j) 
print('Absolute value or Magnitude of 3-4j complex is:', abs(complex)) 