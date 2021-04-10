q=int(input())
for i in range (0,q):
    x,y,z=map(int,input().split())
    if abs(y-z)>abs(x-z):
        print("Cat A")
    elif abs(y-z)<abs(x-z):
        print("Cat B")   
    else:
        print("Mouse C")