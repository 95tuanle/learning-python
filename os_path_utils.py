import datetime
import os
import time
from os import path


def main():
    print(os.name)

    print("Item exists: " + str(path.exists("text-file.txt")))
    print("Item is a file: " + str(path.isfile("text-file.txt")))
    print("Item is a directory: " + str(path.isdir("text-file.txt")))

    print("Item path: " + str(path.realpath("text-file.txt")))
    print("Item path and name: " + str(path.split(path.realpath("text-file.txt"))))
    split = path.split(path.realpath("text-file.txt"))
    print(split[0])
    print(split[1])

    t = time.ctime(path.getmtime("text-file.txt"))
    print(path.getmtime("text-file.txt"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("text-file.txt")))

    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("text-file.txt"))
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


if __name__ == "__main__":
    main()
