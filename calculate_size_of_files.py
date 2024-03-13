from os import path, listdir


def file_info():
    result = 0
    if path.exists(".") and path.isdir("."):
        contents = listdir(".")
        for item in contents:
            # print(item)
            result += path.getsize(path.join(".", item))
    return result


if __name__ == "__main__":
    print(file_info())
