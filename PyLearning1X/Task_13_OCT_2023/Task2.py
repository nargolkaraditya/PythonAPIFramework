# Write a Python program to calculate the area of a circle given its radius using the formula
#area=π×r^2 ( Take pie as 3.14)
Radius = int (input ("Please enter the radius of the given circle: \n"))
area_of_the_circle = 3.14 * Radius * Radius
print ("The area of the given circle is: ", area_of_the_circle)

# ternary operator to find the maximum of three numbers entered by the user.
first_Number=int(input("enter first number: \n"))
second_Number=int(input("enter second number: \n"))
third_Number=int(input("enter third number: \n"))
print("first is greater" if first_Number > second_Number and first_Number > third_Number else "second_Number is greater" if second_Number > first_Number and second_Number > third_Number else "third_Number is greater")

# Develop a Python script that calculates the square and cube of a given number
num1=int(input("enter the number: \n"))
square=num1**2
cube=num1**3
print("Square of the number :-->", square)
print("Cube of the number :-->", cube)