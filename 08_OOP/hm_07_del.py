class Cat:

    def __init__(self, new_name):

        self.name = new_name

        print("%s comes." % self.name)


    def __del__(self):

        print("%s has left."% self.name)

tom = Cat("Tom")
print(tom.name)

# we can use del to delete an object.
del tom

print("-" * 50)


# Tom has left. after print