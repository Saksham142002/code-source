t=int(input())
for i in range(0,t):
    n=str(input())
    a=list(n)
    b=[]
    c=[]
    for j in range(0,len(n)):
        if j%2==0 :
            b.append(n[j])
        else:
            c.append(n[j])
    print("".join(b)+ " "+"".join(c))