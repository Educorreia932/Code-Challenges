N = int(input()) # Number of members in the organization team

days = {}

for i in range(N):
    day = int(input())

    if day not in days:
        days[day] = 1

    else:
        days[day] += 1

mostChosen = max(days.values())

selectedDays = [k for (k, v) in days.items() if v == mostChosen]
selectedDays.sort()

print(selectedDays[0])
