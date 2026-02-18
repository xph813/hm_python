class Person:

    def __init__(self, name, age, height):

        self.name = name
        self.age = age
        self.height = height

    def run(self):

        print(f'{self.name} is running.')

    def eat(self):

        print(f'{self.name} is eating.')

xiaoming = Person('xiaoming', 26, 90)
xiaomei = Person('xiaomei', 26, 90)
print(xiaomei.age)
xiaoming.run()
xiaomei.eat()


class Cat:

    def eat(self):

        print(f'{self.name} is eating.')

    def drink(self):
        print(f'{self.name} is drinking.')

tom = Cat()

tom.name = 'Tom'
tom.eat()
tom.drink()

print(tom.name)
print(tom)

lazy_cat = Cat()
lazy_cat.name = 'Lazy Cat'

lazy_cat.eat()
lazy_cat.drink()

class Cat:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating.')

    def __del__(self):
        print(f'{self.name} has gone.')

    def __str__(self):
        return f'This is {self.name}.'

tom = Cat('Tom')
tom.eat()
print(tom)

del tom
print('-' * 50)
lazy_cat = Cat('Lazy Cat')
lazy_cat.eat()
print(lazy_cat)


class Person:

    def __init__(self, name, weight):

        self.name = name
        self.weight = weight

    def eat(self):

        self.weight += 1

    def run(self):

        self.weight -= 0.5

    def __str__(self):
        return f'This is {self.name}.'

xiaoming = Person('xiaoming', 60.0)
xiaoming.eat()
xiaoming.run()

print(xiaoming.weight)


class HouseItem:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):
        return f'This is {self.name}.'

class House:

    def __init__(self, house_type, house_area):

        self.house_type = house_type
        self.house_area = house_area
        self.free_area = self.house_area
        self.item_list = []

    def add_item(self, item):

        if self.free_area < item.area:
            return
        self.item_list.append(item.name)
        self.free_area = self.house_area - item.area

wardrobe = HouseItem('wardrobe', 4)
desk = HouseItem('desk', 4)
ximengsi = HouseItem('ximengsi', 12)

# print(wardrobe)
house = House('langshiyiting', 60)
house.add_item(wardrobe)
house.add_item(desk)
house.add_item(ximengsi)

print(house.free_area)
print(house.item_list)


class Gun:

    def __init__(self, name):

        self.name = name
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        if self.bullet_count < 1:
            print('no bullet.')
            return

        print(f'{self.name} shot.')
        self.bullet_count -= 1

class Solider:

    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):

        if self.gun is None:
            print(f"{self.name} doesn't have a gun.")
            return
        self.gun.shoot()
        self.gun.bullet_count -= 1

ak47 = Gun('ak47')
ak47.add_bullet(1)

ak47.shoot()
print(ak47.bullet_count)

class Women:

    def __init__(self, name):
        self.name = name
        self.__age = 30

    def __secret(self):
        print(f'{self.name} is {self.__age} years old.')

xiaofang = Women('xiaofang')
print(xiaofang._Women__age)
xiaofang._Women__secret()

