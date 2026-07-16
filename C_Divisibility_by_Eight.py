s = input()

for num in range(0, 1000, 8):
    target = str(num)

    j = 0
    for ch in s:
        if j < len(target) and ch == target[j]:
            j += 1

    if j == len(target):
        print("YES")
        print(target)
        exit()

print("NO")