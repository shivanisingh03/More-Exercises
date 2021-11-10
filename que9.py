# harshad number

def thenumberis(x):
    i=1
    s=x
    sum=0
    while i<=x:
        sum=sum+x%10
        x=x//10
    print("sum",sum)
    if s%sum==0:
        print(s,"it's harshad number")
    else:
        print("not")
thenumberis(    x = int(input("enetr the number ")))











