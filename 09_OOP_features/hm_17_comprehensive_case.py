class Game(object):

    top_score = 0


    def __init__(self, player_name):

        self.player_name = player_name

    @staticmethod
    def show_help():
        print("help message: let zombie go into the door")

    @classmethod
    def show_top_score(cls):
        print("top score: %d" % cls.top_score)

    def start_game(self):

        print("%s starts game" % self.player_name)


# 1. view help message
Game.show_help()

# 2. view top scores
Game.show_top_score()

# 3. create a game object
game = Game("xiaoming")

game.start_game()



