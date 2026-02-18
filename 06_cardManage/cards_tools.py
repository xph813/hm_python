# record all dict
card_list = []


def show_menu():
    """show menu"""

    print("*" * 50)
    print("Welcome to card management system V1.0!")
    print("")
    print("1. add card")
    print("2. show card")
    print("3. search card")
    print("*" * 50)


def add_card():
    """add card"""

    print("*" * 50)
    print("add card")

    # 1. prompt the usr to input info in detail
    name_str = input("please input card name: ")
    phone_str = input("please input phone number: ")
    qq_str = input("please input qq number: ")
    email_str = input("please input email address")


    # 2. create a new dict
    card_dict = {"name": name_str, "phone": phone_str, "qq": qq_str, "email": email_str}

    # 3. add the dict to the list
    card_list.append(card_dict)

    # 4. prompt the usr to add successfully
    print("add usr %s successfully!" % name_str)



def show_all():
    """show all cards"""

    print("*" * 50)
    print("show all cards")

    # determine if there is a record in card_list
    if len(card_list) == 0:

        print("no cards found, please add some card")

        # return
        # 1. return result
        # 2. lines after return will not perform
        # 3. return void, then just return the function
        return

    # print header
    for name in ["name", "phone", "qq", "email"]:
        print(name, end="\t\t")

    print("")

    # print dividing line
    print("=" * 50)

    # traverse card list to output dict
    for card_dict in card_list:

        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))

        # print(card_dict)


def search_card():
    """search card"""

    print("*" * 50)
    print("search card")

    # 1. prompt the usr to input the name
    find_name = input("please input card name to find: ")
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("name\t\tphone\t\tqq\t\temail\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))
            # modify and delete
            deal_card(card_dict)

            break


    # 2. traverse the cards list, prompt usr if not found
    else:
        print("%s not found" % find_name)


def deal_card(find_dict):
    """deal the card found

    :param find_dict: card tha's found
    """
    print(find_dict)

    action_str = input("please input card action: "
                       "[1] modify [2] delete [0] return to the last menu")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"],"name: ")
        find_dict["phone"] = input_card_info(find_dict["phone"],"number: ")
        find_dict["qq"] = input_card_info(find_dict["qq"],"qq: ")
        find_dict["email"] = input_card_info(find_dict["email"],"email: ")

        print("modification success!")

    elif action_str == "2":

        card_list.remove(find_dict)
        print("delete success!")


def input_card_info(dict_value, tip_message):
    """input card info

    :param dict_value: original value
    :param tip_message: hint to input
    :return: if input, return input; if not, return original value
    """
    # 1. prompt usr to input
    result_str = input(tip_message)

    # 2. determine the input
    # 1> if input, return result
    if len(result_str) > 0:
        return result_str
    # 2> if empty, return original
    else:
        return dict_value
