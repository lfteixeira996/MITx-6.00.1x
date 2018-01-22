#Assume s is a string of lower case characters.

#Write a program that prints the number of times the string 'bob' occurs in s. 
#For example, if s = 'azcbobobegghakl', then your program should print

#Number of times bob occurs is: 2

num_times = 0

for x in range (0, len(s)-2):
    
    if s[x] == 'b' and s[x+1] == 'o'and s[x+2] == 'b' and x<len(s)-2:
        num_times = num_times+1
        
   

print("Number of times bob occurs is ", num_times)  