

marks = [[45, 21, 42, 63], [12, 42, 42, 53], 
[42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]] 
i=0
a=[]
while i<len(marks):
    j=0
    m=marks[i][j]
    while j<len(marks[i]):
        if m<marks[i][j]:
            m=marks[i][j]
            a.append(m)
        j+=1
    i+=1
print(a)





















