class A:

    def __init__(self):

        self.num1 = 1
        self.__num2 = 2

    def __test(self):

        print("private method %d %d" % (self.num1, self.__num2))

    def test(self):

        print("parent's public method %d" % self.__num2)
        self.__test()

class B(A):

    def demo(self):

        # 1. can't get parent's private attributes and metthods
        # print("get parent's private attribute %d" % self.__num2)

        # self.__test()

        # 2. get parent's public attributes and methods
        print("parent's public attribute %d" % self.num1)
        print("parent's public method")

        # 3. get parent's private attributes with parent's public method
        self.test()

        pass


b = B()
print(b)

b.demo()
print(b.num1)
b.test()

# can't get parent's private method
# print(b.__num2)
# b.__test()




