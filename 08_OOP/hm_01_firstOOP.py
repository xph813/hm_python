class Cat:

    def eat(self):
        print("cat likes to eat fish.")

    def drink(self):
        print("cat likes to drink.")


tom = Cat()
tom.eat()
tom.drink()

print(tom)
# hexadecimal address
print("%x" % id(tom))


