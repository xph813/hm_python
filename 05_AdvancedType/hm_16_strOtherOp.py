# 1. determine if it's a space
space_str = "  \t\n\r"

print(space_str.isspace())

# 2. determine if a string only has num
# num_str = "1.1"
num_str = "\u00b2"

print(num_str)
print(num_str.isdecimal())# pure number
print(num_str.isdigit())# unicode
print(num_str.isnumeric())# all number including chinese



