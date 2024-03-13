def main():
    # my_file = open("text-file.txt", "w+")  # w+ will create a file if it doesn't exist
    # my_file = open("text-file.txt", "a+")  # a+ will append to the file if it exists
    # for i in range(10):
    #     my_file.write("This is line %d\n" % (i + 1))
    # my_file.close()
    my_file = open("text-file.txt", "r")
    if my_file.mode == "r":
        # contents = my_file.read()
        # print(contents)
        fl = my_file.readlines()
        for x in fl:
            print(x)


if __name__ == "__main__":
    main()
