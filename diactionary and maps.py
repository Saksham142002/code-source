n=int(input())
phone={}
for i in range(0,n):
    x=input().split(" ")
    phone[x[0]]=x[1]
while 1:
    try:   
        x= input()
        if x in phone:
            print(str(x)+"="+str(phone[x]))
        else:
            print("Not found")
    except:
        break