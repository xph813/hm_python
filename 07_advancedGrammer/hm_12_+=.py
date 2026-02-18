
def demo(num, num_list):

    print("function starts")

    num += num

    # += to a list = .extend(),
    # so it can change global value
    # num_list += num_list

    # but this is different
    num_list = num_list + num_list

    print(num)
    print(num_list)

    print("function ends")


gl_num = 9
gl_list = [1, 2, 3]

demo(gl_num,gl_list)
print(gl_num,gl_list)


