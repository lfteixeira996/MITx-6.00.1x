'''

Exercise: biggest

'''


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    max = 0
    # Your Code Here
    for key in aDict.keys():
        
        count =  len(aDict[key])
        
        if count>max:
            max = count
            max_key = key
        
    
    return (max_key,max)
    
    

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')    

print(animals)
print(biggest(animals))