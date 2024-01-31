#palindrome check and also print reverse of the number
num=int(input("num= "))
m=num

rev=0
while m>0:
    rev=(rev*10)+(m%10)
    m=m//10

print("Rev= ",rev)
if rev==num:
    print("Palindrome")
else:
    print("Non Palindrome")