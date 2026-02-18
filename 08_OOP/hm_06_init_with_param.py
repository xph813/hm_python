from hm_02_create_two_cats_object import lazy_cat


class Cat:

    def __init__(self, new_name):

        print("This is initialization method.")

        # self.attribute
        # self.name = "Tom"
        self.name = new_name

    def eat(self):

        print("%s likes to eat fish" % self.name)


# automatically call __init__, when creating an object.
tom = Cat("Tom")
print(tom.name)

lazy_cat = Cat("Lazy")
print(lazy_cat.name)