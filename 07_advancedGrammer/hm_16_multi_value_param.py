
def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)

# demo(1)
demo(1,2, 4, 5, 6, name="xiaoming", age=18)

# unpack
# gl_nums = (1, 2, 3)
# gl_person = {"name": "xiaoming", "age": 18}
# demo(1,*gl_nums, **gl_person)

