try:
    num = int(input("please input an integer: "))

    result = 8 / num

    print(result)

except ZeroDivisionError:
    print("zero division error")

except ValueError:
    print("value error")

