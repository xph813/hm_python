class House_item:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] covers an area of %.2f" % (self.name, self.area)


class House:

    def __init__(self, house_type, area):

        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):

        return ("house type: %s\ntotal area: %.2f[free area: %.2f]\nfunitures: %s"
                % (self.house_type, self.area,
                   self.free_area, self.item_list))

    def add_item(self, item):



        print("adding %s" % item)


# 1. create furniture

bed = House_item("ximengsi", 4)
chest = House_item("yigui", 2)
table = House_item("canzhuo", 1.5)

print(bed)
print(chest)
print(table)

# 2. create a house

myhome = House("tworooms", 60)

myhome.add_item(bed)
myhome.add_item(chest)
myhome.add_item(table)

print(myhome)
