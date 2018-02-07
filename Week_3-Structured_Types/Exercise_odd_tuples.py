# -*- coding: utf-8 -*-
"""
Spyder Editor

Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of 
the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating
oddTuples on this input would return the tuple ('I', 'a', 'tuple').

"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    ret = ()
    x = 1
    for i in aTup:
        
        if(x%2!=0):
            ret = ret+(i,)
    
        x+=1
    return ret
    
    
    
a = ()

aTup = (1,2,3,4,5)
a = oddTuples(aTup)    

print("",a)
