# 1. open
file = open("README", "a")

# 2. write
# r, w, a
# r+, w+, a+ is not efficient
# because the pointer changes frequently
# So, it's not recommended.
file.write("123hello")

# 3. close
file.close()


