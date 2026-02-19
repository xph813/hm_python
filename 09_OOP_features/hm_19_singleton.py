class MusicPlayer(object):

    # define a variable to record the first object
    instance = None

    def __new__(cls, *args, **kwargs):

        # 1. determine instance is empty or not
        if cls.instance is None:
        # 2. if not, create one
            cls.instance = super().__new__(cls)
        
        # 3. return instance
        return cls.instance


# 1. create many objects to see address

player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)


