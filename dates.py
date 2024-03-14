from datetime import date, datetime


def main():
    today = date.today()
    print("Today's date is", today)

    print("Date components:", today.day, today.month, today.year)

    print("Today's weekday # is:", today.weekday())
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    print("Which is a:", days[today.weekday()])

    today = datetime.now()
    print("The current date and time is", today)

    t = datetime.time(datetime.now())
    print("The current time is", t)


if __name__ == "__main__":
    main()
