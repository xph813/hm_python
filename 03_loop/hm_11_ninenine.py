# nine-nine-multiplication sheet
i = 1


# It's like printing stars each line, just replace each star with equation

while i <= 9:

    j = 1

    while j <= i:
        print("%d * %d = %d" %(i, j, i*j), end="\t")
        j += 1

    # print(i)
    print("")

    i += 1
