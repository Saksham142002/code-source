b,n,m=map(int,input().split())
keyboard=list(map(int,input().split()))
usb=list(map(int,input().split()))
c=[]
for i in range(0,n):
    for j in range(0,m):
        if keyboard[i]+usb[j]<=b:
            c.append(keyboard[i]+usb[j])
        

if not c:
    print(-1)
else:
    print(max(c))