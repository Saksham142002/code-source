n=int(input())
arr=list(map(int,input().split()))
b=[]
for i in range(0,n):
    a=arr[n-(i+1)]
    b.append(a)
    print(b[i],end=" ")