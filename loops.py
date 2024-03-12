def main():
    x = 0

    while x < 5:
        print(x)
        x += 1

    print("")

    for x in range(5, 10):
        print(x)

    print("")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)

    print("")

    for x in range(5, 10):
        if x == 7:
            break
        print(x)

    print("")

    for x in range(5, 10):
        if x % 2 == 0:
            continue
        print(x)

    print("")

    for i, d in enumerate(days):
        print(i, d, sep="")


main()
