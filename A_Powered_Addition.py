import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx]); idx += 1
    results = []
    for _ in range(t):
        n = int(input_data[idx]); idx += 1
        a = input_data[idx:idx+n]
        a = list(map(int, a))
        idx += n
        
        prev = a[0]
        max_diff = 0
        for i in range(1, n):
            need = prev - a[i]
            if need > 0:
                if need > max_diff:
                    max_diff = need
                prev = a[i] + need
            else:
                prev = a[i]
        
        T = 0
        while (1 << T) - 1 < max_diff:
            T += 1
        results.append(str(T))
    
    print('\n'.join(results))

main()