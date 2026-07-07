def solve(s):
    n = len(s)
    
    def check(first, second):
        i = s.find(first)
        if i == -1:
            return False
        # search for 'second' starting after position i+1 (non-overlapping)
        j = s.find(second, i + 2)
        return j != -1
    
    if check("AB", "BA") or check("BA", "AB"):
        print("YES")
    else:
        print("NO")

s = input().strip()
solve(s)