# calculate the sum of even numbers between 0 and 100
# 1. loop to calculate
# 2. deal with result

# 1. define result
result = 0

i = 0

while i <= 100:

    # determine i is an even
    if i % 2 == 0:
        print(i)
        result += i

    i += 1

print("sum of even numbs between 0 and 100 is %d" % result)
