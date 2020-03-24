grcount = int(input().strip())
grades = []
for i in range(grcount):
    marks = int(input().strip())
    grades.append(marks)
r = 0    
for i in grades:
    if i<38:
        print(i)
    else:
        dummy = i
        while i%5!=0:
            i += 1
        if i - dummy < 3:
            print(i)  
        else:
            print(dummy)           
