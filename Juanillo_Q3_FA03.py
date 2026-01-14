import numpy as np

names = ["Leo", "Percy", "Jason"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [7000, 7000, 1900, 9400, 3000],
    [8000, 1800, 1900, 9300, 5000],
    [7000, 1000, 1900, 9400, 5000],
])

for i in range(len(names)):
    total_steps = steps[i].sum()
    avg_steps = steps[i].mean()
    min_steps = steps[i].min()
    max_steps = steps[i].max()

    print(names[i], "- Total Steps:", int(total_steps), "|", "Average:", int(avg_steps), "|", "Min:", int(min_steps), "|", "Max:", int(max_steps))
