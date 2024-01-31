#armstrong check
num=int(input("num= "))
m=num
digits=0
while m>0:
    digits+=1
    m//=10

m=num
sum_of_digits=0
while m>0:
    sum_of_digits=sum_of_digits+((m%10)**digits)
    m//=10
# print(sum_of_digits)
if sum_of_digits==num:
    print("Armstrong")

else:
    print("Non Armstrong")