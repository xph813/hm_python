#
row = 1

while row <= 5:

    # the number of the printed stars are equal row
    # add another loop to deal with column
    col = 1

    while col <= row:
        # print("%d" % col)
        print("*", end=" ")
        col += 1

    # print("line no.%d" % row)

    # line break after output each line
    print("")
    row += 1