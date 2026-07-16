import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    a = list(map(int, data[idx:idx+n]))
    idx += n
    
    total = sum(a)
    mx = max(a)
    
    if total % 2 == 0 and mx <= total - mx:
        print("YES")
    else:
        print("NO")

main()