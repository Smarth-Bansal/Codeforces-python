n, m = map(int, input().split())

cats = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
stack = [(1, -1, 0)]   # (current node, parent, consecutive cats)

while stack:
    u, parent, consecutive = stack.pop()

    if cats[u]:
        consecutive += 1
    else:
        consecutive = 0

    if consecutive > m:
        continue

    # Leaf node (except the root)
    if u != 1 and len(graph[u]) == 1:
        ans += 1
        continue

    for v in graph[u]:
        if v != parent:
            stack.append((v, u, consecutive))

print(ans)