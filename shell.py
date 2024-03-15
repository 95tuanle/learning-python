import os
import shutil
from os import path
from zipfile import ZipFile


def main():
    if path.exists("text-file.txt"):
        # if path.exists("text-file.txt.bak"):
        src = path.realpath("text-file.txt")

        dst = src + ".bak"
        shutil.copy(src, dst)

        os.rename("text-file.txt", "newfile.txt")

        root_dir, tail = path.split(src)
        print("root dir: " + root_dir)
        print("tail: " + tail)

        shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("test-zip.zip", "w") as new_zip:
            new_zip.write("newfile.txt")
            new_zip.write("text-file.txt.bak")


if __name__ == "__main__":
    main()
