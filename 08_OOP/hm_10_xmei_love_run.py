class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def __str__(self):

        return "my name is %s, my weight is %.2f kg" % (self.name, self.weight)

    def run(self):

        print("%s loves running, cause it's good for your health" % self.name)
        self.weight -= 0.5

    def eat(self):

        print("%s is faggot, and will run after this meal." % self.name)
        self.weight += 1

xiaoming = Person("xiaoming", 75.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)

# xiaomei loves running

xiaomei = Person("xiaomei", 45.0)

xiaomei.eat()
xiaomei.run()

print(xiaomei)

