# Write a program that calculates and displays the letter grade for a given numerical score (e.g., A, B, C, D, or F) based on the following grading scale:
# input- score - 89
# output- B

scale = int(input("Enter score: \n"))
if scale >= 90 and scale <= 100:
    print("Grade is A")
elif scale >= 80 and scale <= 89:
    print("Grade is B")
elif scale >= 70 and scale <= 79:
    print("Grade is C")
elif scale >= 60 and scale <= 69:
    print("Grade is D")
elif scale >= 0 and scale <= 59:
    print("Grade is E")
else:
    print("Invalid input")
