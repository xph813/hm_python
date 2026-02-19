class A:

    def test(self):

        print("A --- test method")

    def demo(self):
        print("A --- demo method")


class B:

    def demo(self):
        print("B --- demo method")

    def test(self):
        print("B --- test method")


class C(B, A):

    pass

c = C()

c.demo()
c.test()

# get MRO: method resolution order
print(C.__mro__)
