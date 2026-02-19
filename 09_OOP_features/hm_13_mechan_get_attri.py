# search upward to get attributes


class Tool(object):

    # define class attribute using assignment statement
    count = 0

    def __init__(self, name):

        self.name = name

        # count the number of objects created by this class
        Tool.count += 1

tool1 = Tool("ax")
tool2 = Tool("knife")
tool3 = Tool("bucket")

print("total number of tools %d " % Tool.count)


# search upward to get attributes
# Suggest using class.attribute to get class attributes
print(tool1.count)

# a problem using object.attribute to get class attributes
tool3.count = 99

# assignment statement is setting a value,
# So it won't change Tool.count.
# In short, object.attribute can get the class attribute, but can't change the value.
print(tool3.count)

print(Tool.count)

