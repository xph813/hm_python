try:
    num = int(input("please input an integer: "))

    result = 8 / num

    print(result)

except ValueError:
    print("value error")

except Exception as result:
    print("unknown error: %s." % result)

