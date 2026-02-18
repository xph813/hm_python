#! /usr/bin/python3

import cards_tools

# infinite loop
while True:

    # show menu
    cards_tools.show_menu()

    action_str = input("please input desired operation: ")

    print("the operation you choose is [%s]" % action_str)

    # 1,2,3
    if action_str in ["1", "2", "3"]:

        # add
        if action_str == "1":
            cards_tools.add_card()

        # show all
        elif action_str == "2":
            cards_tools.show_all()

        # query
        elif action_str == "3":
            cards_tools.search_card()

        # pass

    # 0 quit
    elif action_str == "0":
        print("Welcome to use it again!")
        break

        # pass

    # else prompt the usr

    else:
        print("wrong input, please input again")

