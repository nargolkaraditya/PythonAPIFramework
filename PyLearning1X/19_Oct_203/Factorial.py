# Factorial
#factorial of 5! is 5*4*3*2*1 which is 120.

number = int(input("Enter the number: \n"))
x=1
for i in range(1,number+1):
        x*=i
        print(f'Factorial {number} is: {x}')



