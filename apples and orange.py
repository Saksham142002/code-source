s,t=map(int,input().split())
a,b=map(int,input().split())
m,n=map(int,input().split())
apples=list(map(int,input().split()))
oranges=list(map(int,input().split()))
app=0
oro=0
for i in range(0,m):
    if s <=a+apples[i]<=t:
        app+=1
for i in range(0,n):
    if s <=b+oranges[i]<=t:
        oro+=1
print(app)
print(oro)