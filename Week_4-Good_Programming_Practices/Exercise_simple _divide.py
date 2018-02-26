# -*- coding: utf-8 -*-
"""
Exercise: simple divide

"""

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide( item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   
    try:
        return item / denom
    
    except ZeroDivisionError:
        return 0
        

        
    except Exception as ex:
        print(ex)
    
    

print(fancy_divide([0, 2, 4], 1))