n,k=map(int,input().split())
arr=list(map(int,input().split()))
if max(arr)<k:
    print(0)
if max(arr)>k:
    y=max(arr)-k
    print(y)
