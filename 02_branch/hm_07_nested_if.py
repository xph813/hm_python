# define has_ticket knife_length
has_ticket = True

knife_length = 10

# if has_ticket, go aboard
if has_ticket:
    print("welcome ")

    # if knife_length >= 20, not allowed
    if knife_length > 20:
        print("your knife is %.2f long" % knife_length)
        print("not allowed")

    # shorter than 20, welcome
    else:
        print("welcome")

else:
    print("Buy a ticket")