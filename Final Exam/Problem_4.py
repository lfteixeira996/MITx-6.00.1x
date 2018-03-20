
def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    # Your code here
    
    if len(L1) != len(L2):
        return False
    
    lista1 = {}
    lista2 = {}
    
    #Create the dictionary
    for i in range(len(L1)):
        
        if(L1[i] in lista1.keys()):
            lista1[L1[i]] +=1
            
        if(L2[i] in lista2.keys()):
            lista2[L2[i]] +=1   
        
        if(L1[i] not in lista1.keys()):
            lista1[L1[i]] = 1
            
        if(L2[i] not in lista2.keys()):
            lista2[L2[i]] = 1
     
    #Both lists empty    
    if len(L1) == 0 and len(L2) == 0: 
        return (None, None, None)
        
     
    #list elements appear the same number of times in both lists
    for x in lista1:
        
        if x not in lista2:
            return False
        
        elif lista1[x] != lista2[x]:
            return False
        
        
    for x in lista2:
        
        if x not in lista1:
            return False
        
        elif lista1[x] != lista2[x]:
            return False
    
     
    '''
    the element occuring the most times
    how many times that element occurs
    the type of the element that occurs the most times
    '''
    keymax = 0     
    valmax = 0    
    for x in lista1:
         if lista1[x] > valmax:
             valmax = lista1[x]
             keymax = x
    
    tup1 = (keymax, valmax,type(keymax));
    
    #print (tup1)
    return tup1
    
    
    
    
    
    
    
    
    