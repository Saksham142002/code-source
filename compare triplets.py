a=list(map(int,input().split()))
b=list(map(int,input().split()))
a_points=0
b_points=0
for i in range(0,3):
    if a[i]>b[i]:
        a_points+=1
    elif a[i]==b[i]:
        continue
    
    else:
        b_points+=1
print(str(a_points)+" "+str(b_points))