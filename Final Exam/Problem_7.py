

'''
With a dict:  |    With a myDict:
-------------------------------------------------------------------------------
d = {}             md = myDict()        # initialize a new object using 
                                          your choice of implementation

d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair

print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1

del(d[1])          md.delete(1)         # use delete method to remove 
                                          key,value pair associated with key 1                                       
'''                                          


class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        #FILL THIS IN
        self.dict = {}
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        #FILL THIS IN
        self.dict[k] = v
            
        
    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN
        if self.dict[k] == None:
            raise ValueError
        return self.dict[k]
        
    def delete(self, k):
        """ k, immutable object """   
        #FILL THIS IN
        return self.dict.__delitem__(k)