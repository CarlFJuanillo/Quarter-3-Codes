names = ["Leo", "Percy", "Jason"]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = [
    [7000, 7000, 1900, 9400, 3000],
    [8000, 1800, 1900, 9300, 5000],
    [7000, 1000, 1900, 9400, 5000],
]

daily_totals = []
for day_index in range(len(days)):
    day_total = 0
    for person_steps in steps:
        day_total += person_steps[day_index]
    daily_totals.append(day_total)
for day_index, total in enumerate(daily_totals):
    print(f"Total steps on {days[day_index]}: {total}")

max_daily_steps = max(daily_totals)
most_active_day_name_day_index = daily_totals.index(max_daily_steps)
most_active_day_name = days[most_active_day_name_day_index]

print(f"The most active day is {most_active_day_name} with {max_daily_steps} steps.")