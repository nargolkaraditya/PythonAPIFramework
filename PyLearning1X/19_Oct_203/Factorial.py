# Factorial
#factorial of 5! is 5*4*3*2*1 which is 120.

number = int(input("Enter the number: \n"))
if number < 0:
    print("Factorial is not possible!")
else:
    fact = 1
    for i in range(1,number+1):
        fact = fact * i

print("Factorial number is", fact)



