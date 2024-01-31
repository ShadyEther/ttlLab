# palindrome chck using func
# Nelson number chck: 222 
# Perfect check using func
# Prime check usign func

def palin_check(num):
    m=num
    rev=0
    while m>0:
        rev=(rev*10)+(m%10)
        m=m//10
    return rev==num

def nelson_check(num):
    str_num=str(num)
    for _ in str_num:
        if _!=str_num[0]:
            return False
    
    return True

# print(nelson_check(11111112))

def isPerfect( n ):
	sum = 0
	i = 1
	while i < n:
		if n % i == 0:
			sum = sum + i
		i += 1
	return (True if sum == n and n!=1 else False)

def prime_check(n):
    for i in range(2,int(num/2)):
        if n%i==0:
            return False
    return True

num=int(input("Num= "))
print("Palindrome? ",palin_check(num))
print("Nelson? ",nelson_check(num))
print("Perfect? ",isPerfect(num))
print("Prime? ",prime_check(num))