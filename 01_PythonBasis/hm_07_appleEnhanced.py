# 1. input price
price_str = input("price of apple : ")

# 2. input weight
weight_str = input("weight of apple : ")

# 3. calculate price
# 1> translate str into float of apple price
price_float = float(price_str)

# 2> translate str into float of apple weight
weight_float = float(weight_str)

money = price_float * weight_float

print(money)
