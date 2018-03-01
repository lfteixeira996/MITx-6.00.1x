def playGame(wordList):
    # TO DO... <-- Remove this comment when you code this function
    option = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
    hand = {}
    
    while 1:
        
        if option == 'e':
            return
        
        elif option == 'n':
            
            option_1 = input("Enter u to have yourself play, c to have the computer play: ")
            while option_1 != 'u' and option_1 != 'c':
                print("Invalid command.")
                option_1 = input("Enter u to have yourself play, c to have the computer play: ")
            
            if option_1 == 'u':
                hand = dealHand(HAND_SIZE)
                playHand(hand, wordList, HAND_SIZE)
                
            else:
                hand = dealHand(HAND_SIZE)
                compPlayHand(hand, wordList, HAND_SIZE)
            
        elif option == 'r':
            if len(hand) == 0:
                print("You have not played a hand yet. Please play a new hand first!")
                
            else:
                option_1 = input("Enter u to have yourself play, c to have the computer play: ")
                while option_1 != 'u' and option_1 != 'c':
                    print("Invalid command.")
                    option_1 = input("Enter u to have yourself play, c to have the computer play: ")
                
                if option_1 == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                
                else:
                    compPlayHand(hand, wordList, HAND_SIZE)
    
        else:
            print("Invalid command.")
        
        option = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")
