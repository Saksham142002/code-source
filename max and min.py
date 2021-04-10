arr=list(map(int,input().split()))
arr.sort()
a=sum(arr)-arr[4]
sum1=sum(arr)-arr[0]
print(str(a)+ " "+str(sum1))