# add the sum of digits and count no of digits in the number
num=int(input("num= "))
m=num
digits=0
sum_of_digits=0
while m>0:
    digits+=1
    sum_of_digits=sum_of_digits+(m%10)
    m//=10

print("Number of digits: ",digits)
print("Sum of digits: ",sum_of_digits)