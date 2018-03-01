#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function 
    handCopy = hand.copy()
    if word in wordList: 
        for item in word:
            if handCopy.get(item, 0) == 0:
                return False
                
            else:
                handCopy[item] -= 1
                
        return True        
        
    
    return False 