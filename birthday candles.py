n=int(input())
candles=list(map(int,input().split()))
y=max(candles)
counter=0
for i in candles:
    if i==y:
        counter+=1
print(counter) 