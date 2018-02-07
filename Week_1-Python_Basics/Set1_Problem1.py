#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

num_vogal = 0

for x in range (0, len(s)):
    
    if s[x] in ('a', 'e', 'i', 'o', 'u'):
        num_vogal = num_vogal+1
        
   

print("Number of vowels: ", num_vogal)  
