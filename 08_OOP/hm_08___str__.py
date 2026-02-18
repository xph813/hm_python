class Cat:

    def __init__(self, new_name):
        self.name = new_name

        print("%s comes." % self.name)

    def __del__(self):
        print("%s has left." % self.name)

    def __str__(self):

        # string is mandatory.
        return "I'm a cat[%s]!" % self.name


tom = Cat("Tom")
print(tom)

