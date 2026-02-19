file = open("README")

# we don't know how many lines here,
# so, we use infinite loop
while True:

    text = file.readline()


    # determine if we get something
    # empty string = False, if not empty = True

    """
    ‌明确类型检查‌：
    若需严格区分 None 和空字符串，建议显式判断：
    if text is None:   # 检查None
    elif not text:     # 检查空字符串
    """
    # if not text:
    if text == "":

        break


    print(text)

file.close()