#Question 1 Write a program that print all the odd numbers between variable A and variable B

A = int(input("Enter first number: "))
B = int(input("Enter second number: "))

while A <= B:
    if A % 2 != 0:
        print(A)
    A+=1
    
#Question 2 Write a program given a variable s, print all the even characters
s = input("Enter string: ")
print(s[0 :: 2])