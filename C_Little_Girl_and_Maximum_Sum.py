n,q=map(int, input().split())
a=list(map(int, input().split()))
diff=[0]*(n+2)
for _ in range(q):
    l,r=map(int, input().split())
    diff[l]+=1
    diff[r+1]-=1
for i in range(1,len(diff)):
    diff[i]+=diff[i-1]
freq=diff[1:n+1]
freq.sort(reverse=True)
a.sort(reverse=True)
ans=0
for i in range(len(a)):
    ans+=a[i]*freq[i]
print(ans)