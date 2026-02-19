class A:

    def __init__(self):

        self.num1 = 1
        self.__num2 = 2

    def __test(self):

        print("private method %d %d" % (self.num1, self.__num2))



class B(A):

    def demo(self):

        # can't get parent's private attributes and metthods
        # print("get parent's private attribute %d" % self.__num2)

        # self.__test()
        pass


b = B()

print(b)

# print(b.__num2)
# b.__test()
b.demo()


