print("enter a word")
x=str(input())
y=len(x)
for i in range(0,y-1):
  if(x[i]==x[(y-1)-i]):
    flag=1
  else:
    flag=0
    break;
if(flag==1):
 print("palindrome")
else:
 print("not palindrome")

