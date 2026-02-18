name_list = ["zhangsan", "lisi", "wangwu"]

# 1. get value and index
print(name_list[2])
print(name_list.index("wangwu"))
# print(type(name_list.index("wangwu")))

# 2. modidy
name_list[1] = "lisi"

# 3. add
name_list.append("wangxiaoer")
name_list.insert(1, "xiaomeimei")

temp_list = ["sunwukong", "zhuerge", "shashidi"]
name_list.extend(temp_list)

# 4. del
name_list.remove("wangwu")
name_list.pop()
name_list.pop(3)
name_list.clear()

print(name_list)