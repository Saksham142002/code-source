
n = int(input())
a = list(map(int, input().split()))
b=[]
for i in range(0,n):
    for j in range(0,n):
        if a[i]==a[j]:
            if i!=j:
                d=j-i
                b.append(abs(d))
if len(b)==0:
    print(-1)
else:
    print(min(b))