# stip a string
poem = ["\t登鹳雀楼",
        "王之涣\n",
        "白日依山尽\t",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10, " "))

# split a string and merge a string

poem_str= "\t登鹳雀楼\t王之涣\n白日依山尽\t黄河入海流\t欲穷千里目\n更上一层楼"

# 1. split string
poem_list = poem_str.split()
print(poem_list)

# 2. merge string
result_str = " ".join(poem_list)
print(result_str)
