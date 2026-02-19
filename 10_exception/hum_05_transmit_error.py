def demo1():
    return int(input("please enter an integer: "))

def demo2():
    return demo1()

# transmit error to the funct
# using the transitivity of error to catch error in main program
try:
    print(demo2())
except Exception as error:
    print("unkown error: %s." % error)

