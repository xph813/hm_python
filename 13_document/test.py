file_read = open('hello.txt')
file_write = open('hi.txt', 'w')

while True:

    text = file_read.readline()

    if not text:
        break

    file_write.write(text)
    print(text)

file_write.close()
file_read.close()