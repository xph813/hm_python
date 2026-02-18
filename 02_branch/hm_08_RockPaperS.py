# import random
import random

# input rock paper scissors
player = int(input("please input RPS: "))

# computer randomly put out RPS
computer = random.randint(1, 3)

print("player %d - computer %d " % (player,computer))

# compare wins and losses
# human win
# if (()
#     or ()
#     or ()):
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("human win, computer loss")

# draw
elif player == computer:
    print("draw")

# else human loss
else:
    print("we will play untill human wins")
