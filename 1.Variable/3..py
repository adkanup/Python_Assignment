# Write a Python program that declares two variables, num1 and num2, and assigns them integer values. Swap the values of the variables without using a third variable, and then print the values of num1 and num2 to the console

num1=int(input("Enter a first integer:"))
num2=int(input("Enter a second integer:"))

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("After Swapping \n Value of first integer and second integer:",num1,num2)
