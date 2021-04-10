n=int(input())
for j in range(0,n):
    i=int(input())
    x=0
    if i>=38:
        if(((i-3)%5)==0 ):
            x=((i-3)/5)*5+5
        elif(((i-4)%5)==0):
            x=((i-4)/5)*5+5
        else:
            x=i
    else:
            x=i
    
    print(int(x))