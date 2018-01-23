#Assume that two variables, varA and varB, are assigned values, 
#either numbers or strings.

#Write a piece of Python code that evaluates varA and varB, 
#and then prints out one of the following messages:

#"string involved" if either varA or varB are strings

#"bigger" if varA is larger than varB

#"equal" if varA is equal to varB

#"smaller" if varA is smaller than varB

VarA = 8
VarB='a'


if(type(VarA) is str or type(VarB) is str):
    print('string involved')
    
elif(VarA > VarB):
    print('bigger')    
    
elif(VarA == VarB):
    print('equal')     
    
else:
    print('smaller')   