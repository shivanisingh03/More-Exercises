# Question 7
# Socho aapke paas 2 lists hain. Aapne aisa code likhna hain jisse ek nayi list 
# banne jisme inn dono lists ke woh item hone chaiye ho dono list mein aa rahe hain.
#  Socho aapki do list yeh hain:

 
list1 = [1, 342, 75, 23, 98]
list2 = [75, 23, 98, 12, 78, 10, 1] 
index=0
sum=[]
while index<len(list1):
    s1=0
    while s1<len(list2):
        if list1[index]==list2[s1]:
            sum.append(list1[index])
        s1+=1
    index+=1
print(sum)


