def f(a,b):
    return a > b
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    #intersect: look at the common keys in d1 and d2 and apply the function f to these keys' values
    intersect = {}
    difference = {}
    for key in d1:
        if key in d2:
            difference[key] = f(d1[key],d2[key])
    #difference: a key-value pair in the difference dictionary is (a) every key-value pair in d1 whose key 
    #appears only in d1 and not in d2 or (b) every key-value pair in d2 whose key appears only in d2 and not in d1.
        else:
            intersect[key] = d1[key]
    for key in d2:
        if key not in d1:
           intersect[key] = d2[key] 
    tuple_interdiff = (difference, intersect)
    return tuple_interdiff