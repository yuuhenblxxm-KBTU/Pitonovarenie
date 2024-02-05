def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens

        total_legs = 2 * num_chickens + 4 * num_rabbits

        if total_legs == numlegs:
            return num_chickens, num_rabbits

    return None


numheads = 35
numlegs = 94

result = solve(numheads, numlegs)

if result:
    num_chickens, num_rabbits = result
    print(f"Number of chickens: {num_chickens}")
    print(f"Number of rabbits: {num_rabbits}")
else:
    print("No solution found.")
