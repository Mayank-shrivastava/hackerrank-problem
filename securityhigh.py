s1 = input()
s2 = input()
n = input()
password = ''
if len(s1) > len(s2):
    while len(password)!=8:
        for i in range(len(s2[:4])):
            for j in range(len(s2[:4])):
                if i == j:
                    password = password + s1[i] + s2[j]
        break
    
elif len(s2) > len(s1):
    while len(password)!=8:
        for i in range(len(s1[:4])):
            for j in range(len(s1[:4])):
                if i == j:
                    password = password + s1[i] + s2[j]
        break
    
a = 0
while len(password)!=10:
    password = password + n[a]
    a += 1
    
print(password)    
    
    
