xiaoming_dict = {"name": "xiaoming"}

# 1. get the value
print(xiaoming_dict["name"])

# 2. add/modify
xiaoming_dict["age"] = 18
xiaoming_dict["name"] = "xiaoxiaoming"


# 3. delete
xiaoming_dict.pop("name")

print(xiaoming_dict)
