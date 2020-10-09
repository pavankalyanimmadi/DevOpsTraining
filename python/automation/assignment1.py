import re;

password1=input("enter your password")
strongPassword=True;


lengthregex=re.compile("\w{8,}");
lowerregex=re.compile("[a-z]+");
upperRegex=re.compile("[A-Z]+");
digitRegex=re.compile("\d")


lengthcheck=re.findall(lengthregex, password1);
lowercaseCheck=re.findall(lowerregex,password1);
uppercaseCheck=re.findall(upperRegex, password1);
digitcheck=re.findall(digitRegex,password1);



if len(lengthcheck)==0:
    strongPassword=False;
    print("password should contain atleast 8 characters");
    
if len(lowercaseCheck)==0:
    strongPassword=False;
    print("password should contain atleast one lower case character");
    
if len(uppercaseCheck)==0:
    strongPassword=False;
    print("password should contain atleast one upper case character");
    
if len(digitcheck)==0:
    strongPassword=False;
    print("password should contain atleast one digit");
    
    
if(strongPassword):
    print("you have entered strong password")
    
    

    

    

