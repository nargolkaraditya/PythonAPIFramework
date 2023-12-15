# Traditional Method
def reverse_string(input_string):
    reverse_str = ""
    for char in input_string:
        reverse_str = char + reverse_str
    return reverse_str


original_str = "ABCD"
rev_str = reverse_string(original_str)
print(rev_str)