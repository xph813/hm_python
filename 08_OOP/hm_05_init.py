class Cat:

    def __init__(self):

        print("This is initialization method.")

        # self.attribute
        self.name = "Tom"
    def eat(self):

        print("%s likes to eat fish" % self.name)


# automatically call __init__, when creating an object.
tom = Cat()
print(tom.name)

tom.eat()