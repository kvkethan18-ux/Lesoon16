n = 4
guess = input("predict: how many in the list n = 4")
points = list(range(1,n + 1))
print('  your guess', guess, 'list:', points, 'items:', len(points))

input('Predict what happens to n as it grows? press enter')
for size in[4, 10, 100, 1000]:
    print(f"n = {size:<5} List uses {size:>5} items in memory")