import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    trees = []
    for _ in range(n):
        x = int(input_data[idx]); idx += 1
        h = int(input_data[idx]); idx += 1
        trees.append((x, h))
    
    if n == 1:
        print(1)
        return
    
    count = 0
    last = -float('inf')  # rightmost occupied coordinate so far
    
    for i in range(n):
        x, h = trees[i]
        if x - h > last:
            # fell left
            count += 1
            last = x
        elif i == n - 1 or x + h < trees[i+1][0]:
            # fell right (last tree, or doesn't collide with next tree's position)
            count += 1
            last = x + h
        else:
            # can't fell, leave standing
            last = x
    
    print(count)

main()