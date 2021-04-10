t=int(input())
for i in range(0,t):
	n=int(input())
	arr=list(map(int,input().split()))
	arr.sort()
	x=arr[0]
	y=arr[1]
	z=arr[n-1]
	print(abs(x-y)+abs(y-z)+abs(z-x))
	