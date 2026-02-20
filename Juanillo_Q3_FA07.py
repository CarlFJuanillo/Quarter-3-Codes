import numpy as np

names = ["Leo", "Percy", "Jason"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [7000, 7000, 1900, 9400, 3000],
    [8000, 1800, 1900, 9300, 5000],
    [7000, 1000, 1900, 9400, 5000],
])

for i in range(len(names)):
    total_steps = np.sum(steps[i])
    ave_steps = np.mean(steps[i])
    print(names[i], "Steps : ", steps[i])
    print("Total Steps : ", total_steps)
    print("Average Steps : ", ave_steps)
    print()
    

max_steps = np.max(steps)
min_steps = np.min(steps)
print("Maximum Steps : ", max_steps)
print("Minimum Steps : ", min_steps)
