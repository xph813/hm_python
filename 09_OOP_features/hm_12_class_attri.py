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

print(Tool.count)

