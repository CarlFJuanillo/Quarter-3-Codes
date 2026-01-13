names = ["Me", "Lia", "Jake"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200],
]

total_steps = []
for person_steps in steps:
    total_steps.append(sum(person_steps))

max_steps = max(total_steps)
top_performer_index = total_steps.index(max_steps)
top_performer_name = names[top_performer_index]

print(f"The top performer is {top_performer_name} with {max_steps} steps.")