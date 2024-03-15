import calendar

c = calendar.TextCalendar(calendar.MONDAY)
st = c.formatmonth(2022, 1, 0, 0)
print(st)

hc = calendar.HTMLCalendar(calendar.MONDAY)
st = hc.formatmonth(2022, 1)
print(st)

for i in c.itermonthdays(2022, 8):
    print(i)

for name in calendar.month_name:
    print(name)

print()

for day in calendar.day_name:
    print(day)

print()

print("Team meetings will be on: ")
for m in range(1, 13):
    cal = calendar.monthcalendar(2022, m)
    week_one = cal[0]
    week_two = cal[1]

    if week_one[calendar.FRIDAY] != 0:
        meet_day = week_one[calendar.FRIDAY]
    else:
        meet_day = week_two[calendar.FRIDAY]

    print(calendar.month_name[m], meet_day)
