#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

num1 = int(input("Choose a number: "))
num2 = int(input("Choose another number: "))
num3 = int(input("Choose the last number: "))

if num1 >= num2 and num1 >= num3:
    print(f"the biggest number is: {num1} ")
elif num2 >= num1 and num2 >= num3:
    print(f"the biggest number is: {num2} ")
else:
    print(f"the greatest number is: {num3} ")
 
 #another statement:
if num1 <= num2 and num1 <= num3:
    print(f"the smallest number is: {num1}")
elif num2 <= num1 and num2 <= num3:
    print(f"the smallest number is: {num2}")
else:
    print(f"the smallest number is: {num3}")
