# code-with-John
#Question 1 Write a program that print all the odd numbers between variable A and variable B
var_A = 307
var_B = 587

if var_A % 2 == 0:
    var_A += 1
while var_A <= var_B:
    print(var_A)
    var_A += 2

#Question 2 Write a program goven Variable S, print all even characters

#using enumeration concept
#The enumerate() function in Python is a built-in function that allows you to iterate over an iterable (such as a list, tuple, or string) while also keeping track of the index of each item in the iterable.
s = input("Enter your favorite fruit: ")
for index, character in  enumerate(s):
    if (index%2 == 0):
        print(character)
