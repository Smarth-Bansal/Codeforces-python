import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    t = int(data[idx]); idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx]); a = int(data[idx+1]); b = int(data[idx+2])
        idx += 3
        
        found = False
        if a == 1:
            if (n - 1) % b == 0:
                found = True
        else:
            x = 1
            while x <= n:
                if (n - x) % b == 0:
                    found = True
                    break
                x *= a
        
        results.append("Yes" if found else "No")
    
    print('\n'.join(results))

main()