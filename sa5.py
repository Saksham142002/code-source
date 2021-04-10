mylist= ["banana,apple,mango"]
print("enter a fruit")
x=input()
if x in mylist:
	print(mylist)
else:
	mylist.append(x)
	y=sorted(mylist)
print(y)

