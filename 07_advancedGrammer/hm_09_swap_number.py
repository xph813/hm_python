a = 6
b = 100

# solution1: use another variable
# c = a
# a = b
# b = c
#
# # solution2: not use another variable
# a = a + b
# b = a - b
# a = a - b

# solution3: python only
a, b = b,a

print(a, b)
