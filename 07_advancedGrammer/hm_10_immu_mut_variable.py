# using assignment statement will not change global variables
# but method will if pass mutable variable into th function

def demo(num, num_list):

    print("code inside function")

    num = 100

    num_list.append(num)

    print(num)
    print("finished")

gl_num = 99
gl_num_list = [1, 2, 3]

demo(gl_num, gl_num_list)
print(gl_num, gl_num_list)


