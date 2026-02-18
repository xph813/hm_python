# not recommended method

class Cat:

    # self is a reference of the created object
    def eat(self):
        print("%s likes to eat fish." % self.name)

    def drink(self):
        print("%s cat likes to drink." % self.name)


tom = Cat()

tom.name = "Tom"

tom.eat()
tom.drink()

print(tom)


lazy_cat = Cat()
lazy_cat.name = "Lazy Cat"

lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_act2 = lazy_cat

print(lazy_act2)


