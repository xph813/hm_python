class House_item:

    def __init__(self, name, area):

        self.name = name
        self.area = area

    def __str__(self):

        return "[%s] covers an area of %.2f" % (self.name, self.area)




# 1. create furnitures

bed = House_item("ximengsi", 4)
chest = House_item("yigui", 2)
table = House_item("canzhuo", 1.5)

print(bed)
print(chest)
print(table)

