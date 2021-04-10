x=str(input())
arr=list(x.split(":"))
s=list(arr[2])
if s[2]=="P" :
    if arr[0]=="12":
        d=arr[0]
    else:
        d=int(arr[0])+12
if s[2]=="A":
    if arr[0]=="12":
       d="00"
    else:
       d=arr[0]
print(str(d)+":"+str(arr[1])+":"+str(s[0])+str(s[1]))