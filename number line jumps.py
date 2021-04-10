x1,v1,x2,v2=map(int,input().split())
if x1-x2==0:
    print("YES")
    quit()
if v2-v1==0:
    print("NO")
    quit()
if((x1-x2)%(v2-v1)==0 and (x1-x2)//(v2-v1)>=0):
    print("YES")
    quit()
print("NO")