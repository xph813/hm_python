def print_info(name, title="", gender=True):
    """

    :param title: title
    :param name: name in the class
    :param gender: True for boys, False for girls
    """
    gender_text = "boy"

    if not gender:
        gender_text = "girl"

    print("[%s]%s is a %s" % (title, name, gender_text))

print_info("xiaoming")
print_info("laowang")
print_info("xiaomei", gender=False)

