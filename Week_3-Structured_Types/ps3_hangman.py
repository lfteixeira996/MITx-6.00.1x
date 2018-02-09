def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    for i in secretWord:
        
        if i not in lettersGuessed:
            return False
                
    return True 



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
    
    
def countLetters(secretWord):
    return len(secretWord)



def letterInWord(secretWord, chr1):

    if chr1 in secretWord:
        return True
    
    else:
        return False
    


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guess = 8
    lettersGuessed = []
    print('   Welcome to the game Hangman!')
    print('   I am thinking of a word that is', countLetters(secretWord), 'letters long.')

    print('   -----------')
    while guess>0:
    
        
        print('   You have', guess,'guesses left.')
        print('   Available Letters: ', getAvailableLetters(lettersGuessed) )
        chr1 = input('   Please guess a letter: ')
        
        if(chr1 in lettersGuessed):
            print("   Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed))
            print('   -----------')
            
        
        else:
            lettersGuessed.append(chr1)

            if(letterInWord(secretWord, chr1) == True):
                print('   Good guess:', getGuessedWord(secretWord, lettersGuessed) )
                print('   -----------')
                if((isWordGuessed(secretWord, lettersGuessed) == True)):
                    print('   Congratulations, you won!')
                    return 
    
            else:
                print('   Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed) )
                print('   -----------')
                guess -=1
    
    
    print('   Sorry, you ran out of guesses. The word was else.')