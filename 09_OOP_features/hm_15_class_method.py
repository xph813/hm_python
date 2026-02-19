class Tool(object):

    # define class attribute using assignment statement
    count = 0

    @classmethod
    def show_tool_count(cls):
        print("the total number of tools is %d" % cls.count)

        pass

    def __init__(self, name):

        self.name = name

        # count the number of objects created by this class
        Tool.count += 1


# create a tool object
tool1 = Tool("ax")
tool2 = Tool("hammer")

Tool.show_tool_count()

# tool1.show_tool_count()

