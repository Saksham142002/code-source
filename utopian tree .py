t=int(input())
for j in range(0,t):
    n=int(input())
    h=1
    for i in range(0,n+1):
        if i==0:
            h=1
            
        elif i%2==0:
            h=h+1
            
        else:
            h=h*2
                   
    print(h)   