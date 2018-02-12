def myLog(x,b):
    
    exp = 2
    result = 0
    if x > b:
        while result <= x:
            result = b**exp
            exp += 1
        return exp - 2
    else:
        return 0
    
    
print(myLog(16,2))    
