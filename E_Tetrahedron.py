import sys

def main():
    n = int(sys.stdin.readline())
    MOD = 1000000007
    
    same = 1  # same[0]
    diff = 0  # diff[0]
    
    for _ in range(n):
        new_same = (3 * diff) % MOD
        new_diff = (same + 2 * diff) % MOD
        same, diff = new_same, new_diff
    
    print(same)

main()