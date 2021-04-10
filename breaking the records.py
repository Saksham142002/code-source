n=int(input())
score=list(map(int,input().split()))
maxi=0
mini=0
max= score[0]
min= score[0]
for i in range(0,n):
    if score[i]>max:
        max=score[i]
        maxi+=1
    if score[i]<min:
        min=score[i]
        mini+=1
print(str(maxi)+" "+str(mini))