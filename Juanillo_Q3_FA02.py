import numpy as np

names = ["Leo", "Percy", "Jason"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

steps = np.array([
    [7000, 7000, 1900, 9400, 3000],
    [8000, 1800, 1900, 9300, 5000],
    [7000, 1000, 1900, 9400, 5000],
])

print("Step Count Table")
print("Name | Mon | Tue | Wed | Thu | Fri")
for i in range(len(names)):
    print(names[i],":", steps[i])  
