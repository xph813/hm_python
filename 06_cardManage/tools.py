card_list = []

def welcome():
    """
    welcome page
    """
    print('*' * 50)
    print('Welcome to use card management system')
    print('')
    print('1. add a card')
    print('2. show all cards')
    print('3. find a card')
    print('')
    print('0. quit the system')
    print('*' * 50)


def add_card():
    """
    add a card
    """
    print('-' * 50)
    print('add a card')

    name = input('Enter card name: ')
    qq = input('Enter qq number: ')
    phone = input('Enter phone number: ')
    mail = input('Enter mail address: ')

    temp_dict = {'name': name, 'qq': qq, 'phone': phone, 'mail': mail}
    card_list.append(temp_dict)

    print(f'{name} added successfully')


def show_all_cards():
    """
    show all cards
    """
    print('-' * 50)
    print('show all cards')

    if len(card_list) == 0:
        print('No card now, please enter 1 to create a new card')
        return

    print('*' * 50)
    for title in ['name', 'qq', 'phone', 'mail']:
        print(f'{title}\t\t\t', end='')
    print('')
    print('=' * 50)

    for card in card_list:

        for key in ['name', 'qq', 'phone', 'mail']:
            print(f'{card[key]}\t\t\t', end='')
        print('')

    # print('*' * 50)


def find_card(name):
    """
    find a card by name, and deal with it
    :param name: name of the card
    :return: no return
    """
    print('-' * 50)
    print('find a card')
    for card in card_list:

        if card['name'] == name:

            action = input(f'{name} was found, '
                           f'please enter your action: 1. modify 2. delete 0. exit to last page  ')

            deal_card(card, action)

            return
            # break is also good

    else:
        print('card not found')


def deal_card(card, action):

    if action == '1':
        card['name'] = input_info_card(card['name'], 'Enter card name: ')
        card['qq'] = input_info_card(card['qq'], 'Enter qq number: ')
        card['phone'] = input_info_card(card['phone'], 'Enter phone number: ')
        card['mail'] = input_info_card(card['mail'], 'Enter mail address: ')
        print(f'{card['name']} modified successfully!')

    elif action == '2':
        card_list.remove(card)
        print(f'{card["name"]} removed successfully!')

def input_info_card(value, message):
    """
    reload input function
    :param value: value of card key
    :param message: tips for modifier
    :return: modified value if modified, else original value
    """
    new_value = input(message)

    if len(new_value) == 0:
        return value
    else:
        return new_value




