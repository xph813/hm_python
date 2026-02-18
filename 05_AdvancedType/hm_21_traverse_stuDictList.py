student = [
    {"name": "atu"},
    {"name": "xiaomei"}
]

# search a student in student list

find_name = "atu"

for stu_dict in student:
    print(stu_dict)
    if stu_dict["name"] == find_name:

        print("%s found" % find_name)

        # if found, then break
        break

else:
    print("soryy, %s is not found" % find_name)

print("cycle ends")
