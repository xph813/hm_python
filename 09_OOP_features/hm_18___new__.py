class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):

        # 1. new will be automatically called, when creating a new object
        print("create an object, allocate space.")

        # 2. allocate space for the object
        # call __new__ from base class--object, because it has method to create a spsace
        # ‌强制 cls 参数‌：因实例化必须明确目标类，这是Python对象模型的设计约束
        # 若不重写 __new__，默认调用 object.__new__(cls)

        instance = super().__new__(cls)

        # instance is a class not other data type
        # instance is a call, recoding address
        print(type(instance))

        # 3. return address, so we can initialize
        return instance

    def __init__(self):

        print("initialize player.")


player = MusicPlayer()

print(player)
