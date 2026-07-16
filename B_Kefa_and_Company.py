import sys

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    d = int(input_data[idx]); idx += 1
    
    friends = []
    for _ in range(n):
        m = int(input_data[idx]); idx += 1
        s = int(input_data[idx]); idx += 1
        friends.append((m, s))
    
    friends.sort(key=lambda x: x[0])
    
    left = 0
    current_sum = 0
    best = 0
    
    for right in range(n):
        current_sum += friends[right][1]
        while friends[right][0] - friends[left][0] >= d:
            current_sum -= friends[left][1]
            left += 1
        if current_sum > best:
            best = current_sum
    
    print(best)

main()