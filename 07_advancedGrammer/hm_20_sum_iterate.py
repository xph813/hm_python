

def sum_numbers(num):

    # 1. exit
    if num == 1:
        return 1

    # 2. sum  sn= sn-1 + n
    temp = sum_numbers(num - 1)

    return temp + num

result = sum_numbers(100)
print(result)

