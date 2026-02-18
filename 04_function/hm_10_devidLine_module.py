def print_line(char, times):
    """print single line

    :param char:  characters
    :param times:   times
    """
    print(char * times)


def print_lines(char, times):
    """print multiple lines
    :param char: characters
    :param times:  times
    """
    i = 0
    while i < 5:
        print_line(char, times)

        i += 1

name = "blackhorse"