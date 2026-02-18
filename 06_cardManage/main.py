#! /usr/bin/python3
import tools

while True:

    # 1. welcome page
    tools.welcome()
    action_str = input('please enter what you want to do: ')

    # 2. other actions
    if action_str in ['1', '2', '3']:

        print(f'what you choose is {action_str}')
        if action_str == '1':
            # 1. create a new card
            tools.add_card()

        elif action_str == '2':
            # 2. show all cards
            tools.show_all_cards()
        elif action_str == '3':
            # 3. modify a card
            name = input('please enter the name of your card: ')
            tools.find_card(name)

    elif action_str == '0':
        print('quit the system, welcome next time')
        break

    else:
        print('invalid input, please try again')
