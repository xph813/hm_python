class Cat:

    # self is a reference of the created object
    def eat(self):
        print("%s likes to eat fish." % self.name)

    def drink(self):
        print("%s cat likes to drink." % self.name)


tom = Cat()

# tom.name = "Tom"


tom.eat()
tom.drink()

# it won't perform if set attribute outside
tom.name = "Tom"

