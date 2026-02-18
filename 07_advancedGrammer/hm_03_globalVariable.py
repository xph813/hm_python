# glocal variable
num = 10


def demo1():

    # modify glocal variable
    # in python, we can't modify global variable
    # if use assignment statement,
    # it is a local variableand can only be used inside the function,
    # but it won't change the global variable

    num = 99
    print("demo1 ==> %d" % num)


def demo2():

    print("demo2 ==> %d" % num)


demo1()
demo2()