# Ab aap ek program likhoge jo ki user se ek integer input lega aur fir uska 
# factorial print karega. Agar user 3 dalega to 6 print karega, 7 dalega toh 5040 
# print karega aur aise hi dusre numbers ke lie. Note: Abhi ke liye yeh soch lo ki 
# user sirf positive integers hi dalega. Negative integers kabhi nahi dalega.




number=int(input("enter the number "))
index=1
count=1
while index<=number:
    print(index)
    count=count*index
    index=index+1
print(count)













