n = int(input())
l1 = []

for i in range(n):
    c = input().split(' ')
    for i in (c):
        if c[0] == 'insert':
            l1.insert(int(c[1]),int(c[2]))
        elif c[0]  == 'remove':
            l1.remove(int(c[1]))
        elif c[0] == 'append':
            l1.append(int(c[1]))    
        elif c[0] == 'sort':
            l1.sort()
        elif c[0] == 'pop':
            l1.pop()
        elif c[0] == 'reverse':
            l1.reverse()
        else:
            print(l1)
        break                

