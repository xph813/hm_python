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

    # def eat(self):
    #
    #     print("Eat")
    #
    # def drink(self):
    #
    #     print("Drink")
    #
    # def run(self):
    #
    #     print("Run")
    #
    # def sleep(self):
    #
    #     print("Sleep")

    def bark(self):

        print("Bark")


wangcai = Dog()
wangcai.eat()
wangcai.drink()
wangcai.run()
wangcai.sleep()
wangcai.bark()

