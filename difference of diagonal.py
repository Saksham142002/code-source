n=int(input())
arr=[]
for i in range(0,n):
    row=list(map(int,input().split()))
    arr.append(row)
d1=0
d2=0
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            d1+=arr[i][j]
        if i==(n-j-1):
            d2+=arr[i][j]
print(abs(d1-d2))