i,j,k=map(int,input().split())
arr=[]
arr1=[]
counter=0
for x in range(i-1,j):
    x=x+1
    arr.append(x)

for y in range(0,(j-i)+1):
    r=list(map(str,str(arr[y])))
    r.reverse()
    s=int("".join(r))
    arr1.append(s)

for z in range(0,(j-i)+1):
    if ((arr[z]-arr1[z])/k)%1==0:
        counter=counter+1
print(counter)