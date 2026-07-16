for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    possible = [False] * (n + 1)

    for i in range(n):
        s = a[i]
        for j in range(i + 1, n):
            s += a[j]
            if s > n:
                break
            possible[s] = True

    ans = 0
    for x in a:
        if possible[x]:
            ans += 1

    print(ans)