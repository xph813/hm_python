xiaoming_dict = {"name": "xiaoming",
                 "age": 18}

# 1. count the number of dict
print(len(xiaoming_dict))

# 2. merge dict
temp_dict = {"height": 1.75,
             "age": 20}

xiaoming_dict.update(temp_dict)

xiaoming_dict.clear()

print(xiaoming_dict)

