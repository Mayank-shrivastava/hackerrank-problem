n = int(input())
scores = list(map(int, input().rstrip().split()))
maxcount = 0
mincount = 0
smax = scores[0]
smin = scores[0]
for i in scores:
    if i>smax:
        smax = i
        maxcount += 1
    if i<smin:
        smin = i
        mincount += 1    
print('{} {}'.format(maxcount,mincount))              

