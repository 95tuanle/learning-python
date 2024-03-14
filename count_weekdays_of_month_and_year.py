import calendar


def count_days(year, month, whichday):
    result = 0
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        if week[whichday] != 0:
            result += 1
    return result


def main():
    print("There are", count_days(2022, 8, calendar.FRIDAY), "Fridays in August 2022")
    print("There are", count_days(2022, 8, calendar.SATURDAY), "Saturdays in August 2022")
    print("There are", count_days(2022, 8, calendar.SUNDAY), "Sundays in August 2022")
    print("There are", count_days(2022, 8, calendar.MONDAY), "Mondays in August 2022")


if __name__ == "__main__":
    main()
