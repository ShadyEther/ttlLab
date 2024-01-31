#plaindrome range
def palin_check(num):
    m=num
    rev=0
    while m>0:
        rev=(rev*10)+(m%10)
        m=m//10
    return rev==num

range1=int(input("range1= "))
range2=int(input("range2= "))

for _  in range(range1,range2):
    if palin_check(_):
        print(_)

    
