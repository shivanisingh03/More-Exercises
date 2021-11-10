
# output:-['NavGurukul', 'is', 'an', 'alternative', 'to', 'higher', 'education', 'reducing', 'the', 'barriers', 'of', 'current', 
#'formal', 'education', 'system']




# method 1

sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
s=sentence.split(" ")
print(s)


# method 2

sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
b="-".join(sentence)
print(b)



# method 3

sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system" 
s=[]
m=""
for i in sentence:
    if i==" ":
        s.append(m)
        m=" "
    else:
        m+=i
if m:
    s.append(m)
print(s)
































