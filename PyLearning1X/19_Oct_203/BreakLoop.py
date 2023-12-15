# Example using break to exit a loop when i == 51 while printing the values from 1 to 100

for i in range(1, 101):
    if i == 51:
        break
    print(i)

i = 1
while i <= 100:
    print(i)
    if i >= 51:
        break
    i = i +1

