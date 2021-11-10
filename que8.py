# Question 8
# Socho aapke paas do lists hain. Ab aapko nayi list banani hai jisme dono lists ke
#  elements hone chaiye. Lekin yeh dhyan mein rakhna hai ki dono lists ke saare 
# elements sirf ek-ek baar hi hone chaiye. Agar humare paas yeh do lists hain:

 
list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
a=[]
i=0
while i<len(list1):
    if list1[i] not in list2:
        list2.append(list1[i])
    i+=1
print(sorted(list1))




list1 = [1, 5, 10, 12, 16, 20]
list2 = [1, 2, 10, 13, 16]
i=0
a=list1
while i<len(list2):
    if list2[i] not in a:
        a.append(list2[i])
    i+=1
print(a)
    

