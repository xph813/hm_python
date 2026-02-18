class Women:

    def __init__(self,name):

        self.name = name
        self.__age = 18

    def __secret(self):

        print("%s is %d years old." % (self.name, self.__age))


xiaofang = Women("xiaofang")
# print(xiaofang.__age)

# xiaofang.__secret()


