class Animal:

    def eat(self):

        print("Eat---")

    def drink(self):

        print("Drink---")

    def run(self):

        print("Run---")

    def sleep(self):

        print("Sleep---")


class Dog(Animal):

    def bark(self):
        print("Bark---")


class XiaoTianQuan(Dog):

    def fly(self):

        print("Fly---")

    def bark(self):

        # 1. rewrite
        print("Bark like dog")

        # 2. super() to extend
        super().bark()

        # parent.method()  not recommended
        # Dog.bark(self)

        # 3. others
        print("f^&(&%*(^")


xtq = XiaoTianQuan()

xtq.bark()

