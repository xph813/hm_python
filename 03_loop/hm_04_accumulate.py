# calculate sum between 0 and 100
# 0. define result
result = 0

# 1. define a counter
i = 0

# 2. loop
while i <= 100:
    print(i)

    # sum i each time
    result += i

    # deal with counter
    i += 1

print("the sum between 0 and 100 is %d" % result)
