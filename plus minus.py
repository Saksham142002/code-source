n=int(input())
arr=list(map(int,input().split()))
positive=0
negative=0 
zero=0
for i in arr:
    if i>0:
        positive+=1
    elif i<0:
        negative+=1
    else:
        zero+=1    
print(float(positive/n))
print(float(negative/n))
print(float(zero/n))