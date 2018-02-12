def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    # Your code here
    ret = 0
    for i in range(0, len(listA)):
        ret += listA[i]*listB[i]
        
    return ret    

listA = [1, 2, 3]
listB = [4, 5, 6]

print(dotProduct(listA, listB))
