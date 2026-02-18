hello_str = "hello world"

# 1. determine if it starts with str
print(hello_str.startswith("Hello"))

# 2. determine if it ends with str
print(hello_str.endswith("world"))

# 3. find sudstring
print(hello_str.find("llo"))
# difference between .index and .find
# .find if it doesn't have the string, then return -1
print(hello_str.find("abc"))

# 4. replace substring
# notice: replace will not change orginal string
print(hello_str.replace("world", "pyhton"))
print(hello_str)


