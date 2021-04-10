n,t=map(int,input().split())
width=list(map(int,input().split()))
for b in range(0,t):
    i,j=map(int,input().split())
    f=width[i:j+1]
    print(min(f))