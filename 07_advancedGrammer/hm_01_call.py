def test(num):

    print("inside this function, %d 's memory address is %d" % (num, id(num)))

    # 1> define a string
    result = "hello"

    print("the memory address of %s is %d" % (result, id(result)))
    # 2> return result
    return result


# 1. define a number variable
a = 10

print("the memory address of a is %d" % id(a))

# 2. call test(), it's actually transfer the call of actual argument
test(a)
