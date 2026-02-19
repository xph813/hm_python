# 1. open
file = open("README")

# 2. read
text = file.read()

print(text)
print("-" * 50)
print(len(text))

# after .read(), pointer will move to the last
# so .read() again, nothing turns back
text = file.read()
print(text)
print(len(text))



# 3. close
file.close()