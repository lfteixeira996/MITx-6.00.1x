
trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si','5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}



def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    us_num = int(us_num)
    
    if us_num>=0 and us_num<=10:
        return trans.get(str(us_num))
    
    if us_num>=11 and us_num<=19:
        return trans.get(str(10))+' '+trans.get(str(us_num-10))
    
    if us_num>=20 and us_num<=99:
        
        res = divmod(us_num, 10)
        
        quocient  = str(res[0])
        remainder = str(res[1])
        result = trans.get(quocient)+' '+trans.get(str(10))
        
        if remainder != str(0):
            result +=' '+trans.get(remainder)
        
        
        return result