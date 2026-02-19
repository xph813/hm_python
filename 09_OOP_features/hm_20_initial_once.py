# the times of new equals init
# so in last code, initialize not only once


class MusicPlayer(object):
    # define a variable to record the first object
    instance = None

    # define another variable to record if initialized or not
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1. determine instance is empty or not
        if cls.instance is None:
            # 2. if not, create one
            cls.instance = super().__new__(cls)

        # 3. return instance
        return cls.instance

    def __init__(self):

        # 1. determine it's initialized or not

        # notice: not cls.init_flag,
        # because it's not transferred
        if MusicPlayer.init_flag:
            return

        # 2. if not, initialize
        else:
            print("initialize player")

        # 3. modify init_flag
        MusicPlayer.init_flag = True


# 1. create many objects to see address

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)


