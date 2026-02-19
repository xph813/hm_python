def input_password():

    # 1. prompt user to input password
    pwd = input("Please enter your password: ")

    # 2. determine the length of the password
    if len(pwd) >= 8:
        return pwd

    # 3. < 8, raise exception
    print("raise exception explicitly.")

    # 1> create an exception object
    ex = Exception("length is not long enough.")

    # 2> raise exception actively
    raise ex

    # notice: if not return value, return none
    return None

try:
    print(input_password())
except Exception as result:
    print(result)

