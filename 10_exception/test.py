# try:
#     num = int(input('please input a integer: '))
#     print(8 / num)
# except ZeroDivisionError:
#     print("zero division error.")
#
# except ValueError:
#     print("value error")

try:
    pass
except Exception as result:
    print(f'error is {result}.')
else:
    pass
finally:
    pass


def input_passwd():

    passwd = input("please input a number: ")

    if len(passwd) >= 8:

        return passwd

    raise Exception('Not long enough password.')

try:
    print(input_passwd())
except Exception as result:
    print(f'{result}.')