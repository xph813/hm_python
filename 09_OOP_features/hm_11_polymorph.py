class Dog(object):

    def __init__(self, name):

        self.name = name

    def game(self):

        print("%s happily plays." % self.name)


class XiaoTianQuan(Dog):

    def game(self):
        print("%s flies to sky to play." % self.name)



class Person(object):

    def __init__(self, name):

        self.name = name

    def game_with_dog(self, dog):

        print("%s happily plays with %s." % (self.name, dog.name))

        dog.game()


# 1. create a dog object
# wangcai = Dog("wangcai")
wangcai = XiaoTianQuan("Flying wangcai")

# 2. create a xiaoming object
xiaoming = Person("xiaoming")

# 3. let xiaomin play with dog

xiaoming.game_with_dog(wangcai)


