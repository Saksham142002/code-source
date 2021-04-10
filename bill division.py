bill=[]
n,k=map(int,input().split())
bill= list(map(int,input().split()))
    
b=int(input())   
bill.pop(k)
d=bill
ans=int(sum(d)/2)


if ans==b:
   print("Bon Appetit")
else:
    y=b-ans
    print(y)