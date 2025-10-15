'''8.Write a program to accept percentage from the user and display the grade according to the following criteria:
Marks Grade > 90 A > 80 and <= 90 B >= 60 and <= 80 C below 60 D'''
grade=int(input("enter percentage"))
if grade>90:
    print("A")
elif grade>80 and grade<=90:
    print("B")
elif grade>=60 and grade<=80:
    print("c")
else:
    print("D")
