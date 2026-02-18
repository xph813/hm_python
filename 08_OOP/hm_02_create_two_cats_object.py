class Cat:

    def eat(self):
        print("cat likes to eat fish.")

    def drink(self):
        print("cat likes to drink.")


tom = Cat()
tom.eat()
tom.drink()

print(tom)


lazy_cat = Cat()
lazy_cat.eat()
lazy_cat.drink()

print(lazy_cat)

lazy_act2 = lazy_cat

print(lazy_act2)


