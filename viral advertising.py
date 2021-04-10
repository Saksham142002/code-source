n=int(input())
total=2
liked=5//2
for i in range(0,n-1):
    shared =liked*3
    liked=shared//2
    total+=liked
print(total)