#7. Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.
number=int(input("enter number"))
lastdigit=number%10
if lastdigit%3==0:
    print("divisible by 3")
else:
    print("lastDigit of a number is not divisible by 3")

