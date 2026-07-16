import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx:idx+n]))
        idx += n
        
        total = 0
        for v in a:
            total ^= v
        
        if total == 0:
            results.append("YES")
            continue
        
        # try to find 3 segments each XOR-ing to total
        found_first = -1
        found_second = -1
        cur = 0
        for i in range(n):
            cur ^= a[i]
            if cur == total:
                if found_first == -1:
                    found_first = i
                    cur = 0
                elif found_second == -1:
                    found_second = i
                    cur = 0
                    break
        
        # need first cut and second cut both before the last index
        if found_first != -1 and found_second != -1 and found_second < n - 1:
            results.append("YES")
        else:
            results.append("NO")
    
    print('\n'.join(results))

main()