rankedc = int(input().strip())

ranked = list(map(int, input().rstrip().split()))
player_count = int(input().strip())

player = list(map(int, input().rstrip().split()))
size= len(ranked)
size1=len(player)
i=0
count=0
a=0
b=0
j=0   
for i in range(0,size):
     
         
         b=player[j]  
         print(b)     
         #ranked.push(b)
         ranked.sort()
         if ranked[j]==ranked[j+1]:
            count=count+1
         a=ranked.index(b)
        #a=a-count
        #print(a)
         #ranked.pop(b)
         j=j+1