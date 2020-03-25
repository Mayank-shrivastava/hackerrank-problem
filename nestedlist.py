n = int(input())
marksheet = []
for i in range(n):
    marksheet.append([input(),float(input())])
marksheet.sort(key = lambda x:(x[1],x[0]))
#first sort wrt marks and then alphabetically
names = [i[0] for i in marksheet]
marks = [i[1] for i in marksheet]
minmarks = min(marks)
while marks[0] == minmarks:
    marks.remove(marks[0])
    names.remove(names[0])
for i in range(0,len(marks)):
    if marks[i]==min(marks):
        print(names[i])     

