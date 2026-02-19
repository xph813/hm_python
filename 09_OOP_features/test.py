class Women:

    def __init__(self, name):

        self.__age = 30
        self.name = name

    def __test(self):

        print(f'I am {self.__age} years old.')

    def demo(self):

        print(f'I am {self.__age} years old.')

class XiaoFang(Women):

    pass

# xiaofang = XiaoFang('xiaofang')
# # print(xiaofang.__age)
# xiaofang.demo()


class MusicPlayer:

    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):

        # print('Hihihi')

        if cls.instance is None:

            cls.instance = super().__new__(cls)

        return cls.instance


    def __init__(self):

        if MusicPlayer.init_flag:

            return

        print('hellohello')
        MusicPlayer.init_flag = True

player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)