import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...         
    list_ret = list(string.ascii_lowercase)
    
    for i in lettersGuessed:
        
        if i in list_ret:
            list_ret.remove(i)
    
    
    list_ret = ''.join(list_ret)
    return list_ret


print(getAvailableLetters(['a','b','z']))