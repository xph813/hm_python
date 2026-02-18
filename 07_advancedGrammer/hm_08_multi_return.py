def measure():
    """measure temp and humidity"""


    print("measure starts...")
    temp = 30
    wetness = 50

    print("measure ends...")

    # the parentheses in return can be omitted
    return temp, wetness


result = measure()
print(result)

# deal with temp and humidity separately
print(result[0])
print(result[1])

# the lines above are not convenient
# we can define two variables in a tuple to get the result all at once

gl_temp, gl_wetness = result

print(gl_temp)
print(gl_wetness)


