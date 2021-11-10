# Question 6
# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain. 
# Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek
#  baar hi aaye. Jaise:
# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"] 
# a=[]
# i=0
# while i<len(string_list):
#     c=0
#     while c<len(string_list):
#         if string_list[i]==string_list[c] not in a:
#             a.append(string_list[c])
#         c=c+1
#     i+=1
# print(a)



# string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai'] 
# i=0
# b=[]
# while i<len(string_list):
#     d=0
#     while d<len(string_list):
#         if string_list[i]==string_list[d] not in b:
#             b.append(string_list[d])
#         d=d+1
#     i+=1
# print(b)

string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"] 
index=0
count=[]
while index<len(string_list):
    next=0
    while next<len(string_list):
        if string_list[index]==string_list[next] not in count:
            count.append(string_list[next])
        next+=1
    index+=1
print(count)






