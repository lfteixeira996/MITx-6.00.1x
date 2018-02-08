def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    lista_ret = []

    
    for i in secretWord:
        if i in lettersGuessed:
            lista_ret.append(i)
            
        else:
            lista_ret.append('_ ')
            
            
    
    lista_ret= ''.join(lista_ret)        
    return lista_ret            



print(getGuessedWord('durian', ['d','h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u']))