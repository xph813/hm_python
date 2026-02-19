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



xtq = XiaoTianQuan()

xtq.fly()
xtq.bark()
xtq.eat()
