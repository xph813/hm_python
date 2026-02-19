# 1. open
file_read = open("README")
file_write = open("README[copy]", "w")

# 2. read and write
# text = file_read.read()
# file_write.write(text)
while True:

    text = file_read.readline()

    if not text:
        break

    file_write.write(text)


# 3. close
file_write.close()
file_read.close()