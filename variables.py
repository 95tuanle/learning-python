my_int = 5
my_float = 13.2
my_str = "This is a string"
my_bool = True
my_list = [0, 1, "two", 3.2, False]
my_tuple = (0, 1, 2)
my_dict = {"one": 1, "two": 2}

print(my_int)
print(my_float)
print(my_str)
print(my_bool)
print(my_list)
print(my_tuple)
print(my_dict)

my_int = "abc"
print(my_int)

print(my_list[2])
print(my_tuple[1])

print(my_list[1:5])
print(my_list[1:5:2])

print(my_list[::-1])

print(my_dict["one"])

# print("string type" + 123)
print("string type" + str(123))


def some_function():
    global my_str
    my_str = "def"
    print(my_str)


some_function()
print(my_str)

del my_str  # print(my_str)
